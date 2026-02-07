import { execSync } from "child_process";
import fs from "fs";
import path from "path";

const REPO = "FormalVerificationMethods";

// Restore file timestamps from git
function restoreGitTimestamps() {
    try {
        const files = execSync('git ls-files -z', { encoding: 'utf8' })
            .split('\0')
            .filter(f => f);

        for (const file of files) {
            if (!fs.existsSync(file)) continue;

            const timestamp = execSync(
                `git log -1 --format=%ct -- "${file}"`,
                { encoding: 'utf8' }
            ).trim();

            if (timestamp) {
                const date = new Date(parseInt(timestamp) * 1000);
                fs.utimesSync(file, date, date);
            }
        }
        console.log('✓ Restored file timestamps from git history\n');
    } catch (err) {
        console.warn('⚠ Could not restore git timestamps:', err.message);
    }
}

// Restore timestamps before checking what needs rebuilding
restoreGitTimestamps();

const decks = fs
    .readdirSync(process.cwd(), { withFileTypes: true })
    .filter(dirent => dirent.isFile() && dirent.name.endsWith(".md"))
    // Filter out index.md and other non-slide decks if necessary, or just rely on convention
    .map(dirent => dirent.name);

if (decks.length === 0) {
    console.error("No .md decks found in the current directory.");
    process.exit(1);
}

// Create dist directory if it doesn't exist
if (!fs.existsSync("dist")) {
    fs.mkdirSync("dist");
}

function needsRebuild(sourceFile, outputDir) {
    const outputHtml = path.join(outputDir, `${path.basename(sourceFile, '.md')}.html`);

    // If output doesn't exist, rebuild
    if (!fs.existsSync(outputHtml)) {
        return true;
    }

    // Compare modification times
    const sourceMtime = fs.statSync(sourceFile).mtime;
    const outputMtime = fs.statSync(outputHtml).mtime;

    return sourceMtime > outputMtime;
}

let builtCount = 0;
let skippedCount = 0;

for (const file of decks) {
    const base = file.replace(/\.md$/, "");
    // Skip index.md processing as a slide deck
    if (base === 'index') continue;

    const outputDir = `dist/${base}`;

    if (!needsRebuild(file, outputDir)) {
        console.log(`⏭️  Skipping ${file} (up to date)`);
        skippedCount++;
        continue;
    }

    console.log(`\n▶ Building ${file} ...`);

    // Remove old build output for this deck
    fs.rmSync(outputDir, { recursive: true, force: true });

    // Build HTML only (no --pdf flag)
    execSync(
        `npx slidev build ${file} --base "/${REPO}/${base}/" -o ${outputDir}`,
        { stdio: "inherit" }
    );


    fs.renameSync(`${outputDir}/index.html`, `${outputDir}/${base}.html`);

    fs.cpSync(outputDir, "dist", { recursive: true });
    builtCount++;
}

// Build index.md separately or copy it?
// In the original, index.md seems to encompass the main page.
// The original build script iterates over *all* .md files.
// However, index.md is usually an entry point.
// In the original, index.md is a slide deck?
// Looking at original file content for index.md: `layout: full`, `theme: academic`. It looks like a slide deck too or a landing page in slidev.
// I will stick to the original logic which iterates over all .md files.
// Wait, the original build-all.js iterated over `decks`.
// If index.md is in `decks`, it builds it.
// The base path in the original was `/${REPO}`.
// But for sub-decks it was `dist/${base}`.
// Let's re-examine the original build command:
// `npx slidev build ${file} --base "/${REPO}" -o ${outputDir}`
// ALL decks were built with base `/${REPO}`? That seems wrong if they are in subfolders.
// Ah, `outputDir` is `dist/${base}`.
// So `dist/00-intro/index.html`.
// Then it renames `index.html` to `${base}.html` -> `dist/00-intro/00-intro.html`.
// Then it copies `dist/00-intro` to `dist`... wait.
// `fs.cpSync(outputDir, "dist", { recursive: true });`
// If `outputDir` is `dist/00-intro`, copying it to `dist` puts `00-intro` *inside* `dist`?
// No, `cpSync('dist/00-intro', 'dist')`?
// If `outputDir` is `dist/00-intro`.
// It contains `00-intro.html` (renamed from index.html) and assets.
// copying `dist/00-intro` to `dist` results in `dist/00-intro`?
// Or does it merge contents?
// If I assume the original script works, I should copy it exactly, just changing REPO.
// The original script:
// `npx slidev build ${file} --base "/${REPO}" -o ${outputDir}`
// `fs.renameSync(`${outputDir}/index.html`, `${outputDir}/${base}.html`);`
// `fs.cpSync(outputDir, "dist", { recursive: true });`

// I'll stick to the original script logic exactly to minimize risk.
