---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: true
htmlAttrs:
  dir: rtl
  lang: heb
drawings:
  enabled: true
info: |
  ## מערכות מעברים (Transition Systems)
  מרצה: גרא וייס
---

# מידול מערכות חומרה ותוכנה 

##  הרצאה בקורס מבוא לאימות תוכנה <br> בשיטות פורמאליות
הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**<br>



<img src="https://in.bgu.ac.il/marketing/DocLib/Pages/graphics/just-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# מידול מעגלי חומרה ותוכניות מחשב

חלק זה מדגים את השימוש במערכות מעברים על ידי הרחבה על מידול של **מעגלי חומרה (סינכרוניים)** ו**מערכות סדרתיות תלויות-נתונים** – סוג של תוכניות מחשב סדרתיות פשוטות.

בשני המקרים, הרעיון הבסיסי הוא:
* **מצבים (States)** מייצגים תצורות אחסון אפשריות (כלומר, הערכות של ה"משתנים" הרלוונטיים).
* **שינויי מצב (Transitions)** מייצגים שינויים ב"משתנים" אלו.

את המונח **"משתנה"** יש להבין במובן הרחב ביותר:
* **עבור תוכניות מחשב:** משתנה יכול להיות משתנה בקרה (כמו מונה פקודות - Program Counter) או משתנה תוכנית רגיל.
* **עבור מעגלים:** משתנה יכול לייצג, למשל, אוגר (Register) או ביט קלט חשמלי.

---

# דוגמה: מעגל חומרה סדרתי

נבחן מעגל סדרתי עם משתנה קלט $x$, משתנה פלט $y$, ואוגר $r$.


* **פונקציית הפלט $y$:** $\quad \lambda_y = \neg(x \oplus r)$ 
* **עדכון האוגר $r$:** $\quad \delta_r = x \vee r$ 


**מודל מערכת המעברים:**
* **מצבים:** $S = \text{Eval}(x, r) = \{\langle x=0,r=0 \rangle, \langle 1,0 \rangle, \langle 0,1 \rangle, \langle 1,1 \rangle\}$
* **מצבים התחלתיים:** $I = \{\langle 0,0 \rangle, \langle 1,0 \rangle\}$ (ללא הנחה על קלט ראשוני).
* הקבוצה $Act$ מושמטת (אינה רלוונטית כאן).

**פונקציית התיוג** (עבור $AP = \{x, y, r\}$):
* $L(\langle 0,0 \rangle) = \{y\}, \qquad L(\langle 1,0 \rangle) = \{x\}$
* $L(\langle 0,1 \rangle) = \{r\}, \qquad L(\langle 1,1 \rangle) = \{x, r, y\}$



<div class="flex flex-col items-center justify-center transform scale-[0.75] origin-top absolute top-80 left-40 -translate-x-1/2 -translate-y-1/2 ">

<!-- Logic Circuit SVG -->
<svg width="350" height="200" viewBox="0 0 350 200" xmlns="http://www.w3.org/2000/svg">
  <style>
    .wire { stroke: #333; stroke-width: 2; fill: none; }
    .gate { fill: #f8fafc; stroke: #333; stroke-width: 2; }
    .join { fill: #333; }
    .txt { font-family: ui-sans-serif, system-ui, sans-serif; fill: #333; }
  </style>

  <!-- Input x -->
  <text x="15" y="36" style="font-size: 20px;" font-style="italic" class="txt">x</text>
  <path class="wire" d="M 20 30 L 115 30" />
  
  <!-- Branch to OR -->
  <circle cx="55" cy="30" r="3.5" class="join" />
  <path class="wire" d="M 55 30 L 55 90 L 115 90" />

  <!-- XOR Gate at (100, 20) -->
  <g transform="translate(100,10)">
    <path class="wire" d="M 0 10 Q 15 30 0 50" />
    <path class="gate" d="M 10 10 Q 40 10 60 30 Q 40 50 10 50 Q 25 30 10 10 Z" />
    <path class="wire" d="M 5 10 Q 20 30 5 50" />
  </g>
  <text x="144" y="44" style="font-size: 15px;" font-style="italic" class="txt">xor</text>

  <!-- OR Gate at (100, 70) -->
  <g transform="translate(100,70)">
    <path class="gate" d="M 10 10 Q 40 10 60 30 Q 40 50 10 50 Q 25 30 10 10 Z" />
  </g>
  <text x="140" y="105" style="font-size: 15px;" font-style="italic" class="txt">or</text>

  <!-- Wire XOR to NOT -->
  <path class="wire" d="M 160 40 L 220 40" />

  <!-- NOT Gate at (220, 25) -->
  <g transform="translate(220,25)">
    <path class="gate" d="M 0 0 L 30 15 L 0 30 Z" />
    <circle cx="34" cy="15" r="4" class="gate" />
  </g>
  <text x="240" y="44" style="font-size: 12px;" font-style="italic" class="txt">not</text>

  <!-- Output y -->
  <path class="wire" d="M 258 40 L 325 40" />
  <text x="335" y="46" style="font-size: 20px;" font-style="italic" class="txt">y</text>

  <!-- Wire OR to Register -->
  <path class="wire" d="M 160 100 L 180 100 L 180 155 L 205 155" />

  <!-- Register r at (200, 140) -->
  <g transform="translate(205,140)">
    <rect x="0" y="0" width="40" height="30" rx="3" class="gate" />
    <text x="20" y="21" style="font-size: 18px;" font-style="italic" text-anchor="middle" class="txt">r</text>
  </g>

  <!-- Feedback wire from Register -->
  <path class="wire" d="M 245 155 L 265 155 L 265 185 L 35 185 L 35 110 L 115 110" />
  <circle cx="35" cy="110" r="3.5" class="join" />
  <path class="wire" d="M 35 110 L 35 50 L 115 50" />
</svg>


<br>
<br>
<br>

<!-- Transition System Diagram -->
<div class="-mt-6 w-full flex justify-center">
<TransitionSystemD3  
  :width="400" :height="250"
  :states="[
    { id: 's0', text: '$x{=}0 \\land r{=}0$', label: '\{y\}', initial: true, initialDirection: 'top', x: 80, y: 50, width: 110 },
    { id: 's1', text: '$x{=}1 \\land r{=}0$', label: '\{x\}', initial: true, initialDirection: 'top', x: 320, y: 50, width: 140 },
    { id: 's2', text: '$x{=}0 \\land r{=}1$', label: '\{r\}', labelY: 30, x: 80, y: 200, width: 140 },
    { id: 's3', text: '$x{=}1 \\land r{=}1$', label: '\{x,r,y\}', labelY: 30, x: 320, y: 200, width: 140 }
  ]"
  :transitions="[
    { source: 's0', target: 's0', action: ' ', loopDirection: '90eg' },
    { source: 's0', target: 's1', action: ' ' },
    { source: 's1', target: 's2', action: ' ' },
    { source: 's1', target: 's3', action: ' ' },
    { source: 's2', target: 's2', action: ' ', loopDirection: '90deg' },
    { source: 's2', target: 's3', action: ' ', curve: 0.15 },
    { source: 's3', target: 's2', action: ' ', curve: 0.15 },
    { source: 's3', target: 's3', action: ' ', loopDirection: '90deg' }
  ]"
/>
</div>
</div>


---

# הכללה: מידול מעגלי חומרה סדרתיים

ניתן להכליל את הגישה שראינו עבור מעגלי חומרה סדרתיים שרירותיים עם:
*   $n$ ביטים של קלט: $x_1, \dots, x_n$
*   $m$ ביטים של פלט: $y_1, \dots, y_m$
*   $k$ אוגרים (Registers): $r_1, \dots, r_k$

**העקרונות המנחים:**
*   **מצבים:** מייצגים את הערכות (Evaluations) של $n+k$ ביטי הקלט והאוגרים.
*   **פלטים:** נקבעים לפי ערכי הקלט והאוגרים (פונקציות מיתוג).
*   **מעברים:** מייצגים את התנהגות המעגל, כאשר ערכי הקלט משתנים באופן אי-דטרמיניסטי על ידי הסביבה.
*   **ערכים התחלתיים:** ערכי האוגרים התחלתיים נתונים ($c_{0,1}, \dots, c_{0,k}$). הקלטים התחלתיים יכולים להיות כל דבר.

---

# המודל הפורמלי: מערכת המעברים $TS$

מערכת המעברים $TS = (S, Act, \to, I, AP, L)$ הממדלת מעגל זה:

1.  **מרחב המצבים:** $S = Eval(x_1, \dots, x_n, r_1, \dots, r_k) \cong \{0, 1\}^{n+k}$.

2.  **מצבים התחלתיים:** האוגרים מקבלים את ערכם ההתחלתי, והקלטים שרירותיים:
    $$I = \{(a_1, \dots, a_n, c_{0,1}, \dots, c_{0,k}) \mid a_1, \dots, a_n \in \{0, 1\}\}$$
3.  **פעולות:** קבוצת הפעולות אינה רלוונטית, נבחר $Act = \{\tau\}$.
4.  **פסוקים אטומיים:** $AP = \{x_1, \dots, x_n, y_1, \dots, y_m, r_1, \dots, r_k\}$.

---

# תיוג ומעברים

5.  **פונקציית התיוג $L$:** לכל מצב $s$, התיוג כולל את המשתנים שערכם 1:
    $$L(a_1, \dots, a_n, c_1, \dots, c_k) = \{x_i \mid a_i = 1\} \cup \{r_j \mid c_j = 1\} \cup \{y_i \mid s \models \lambda_{y_i} = 1\}$$
    כאשר $\lambda_{y_i}$ היא פונקציית המיתוג של ביט הפלט $y_i$.

6.  **מעברים:** מייצגים את עדכון האוגרים לפי פונקציות המעבר $\delta_{r_j}$:
    $$( \underbrace{a_1, \dots, a_n}_{\text{input}}, \underbrace{c_1, \dots, c_k}_{\text{register}} ) \xrightarrow{\tau} (a'_1, \dots, a'_n, c'_1, \dots, c'_k)$$
    אם ורק אם $c'_j = \delta_{r_j}(a_1, \dots, a_n, c_1, \dots, c_k)$ לכל $j$.

    **שימו לב:** אין הגבלה על ערכי הקלט החדשים $a'_1, \dots, a'_n$ (שינוי אי-דטרמיניסטי).

---

# סימולציה: פריסת מערכת המעברים

ניתן לממש את "פריסת" המערכת בעזרת קוד פשוט. הקוד עובר על כל מרחב המצבים ומחשב את המעברים והתיוגים.

<PyodideRunner src="/extract_ts.py" />

---

# מערכות תלויות-נתונים (Data-Dependent Systems)

פעולות הניתנות לביצוע במערכת תלויה בנתונים נובעות בדרך כלל מהסתעפות מותנית (conditional branching).

**דוגמה:**  
<div class="flex justify-center text-2xl font-mono bg-slate-100 dark:bg-slate-800 p-4 rounded-lg shadow-inner">

**if** x%2 = 1 **then** x := x + 1 **else** x := 2·x **fi**

</div>

עקרונית, במידול קטע תוכנית זה כמערכת מעברים:
*   ניתן **להשמיט** את התנאים ולהחליפם באי-דטרמיניזם.

    *   *חיסרון:* מוביל למערכת מופשטת מדי שבה קשה לאמת תכונות רלוונטיות.

*   לחלופין, ניתן להשתמש ב**מעברים מותנים** (conditional transitions).

    *   את הגרף המתקבל (המתויג בתנאים) ניתן **לפרוס (unfold)** למערכת מעברים שניתנת לאימות.

* נדגים את שתי הגישות.

---

# דוגמה: גרף תוכנית של רובוט

<div class="absolute top-20 left-10 text-[11px] bg-white/90 dark:bg-slate-900/90 p-1.5 rounded-lg border border-slate-200 dark:border-slate-700 shadow-xl z-20 compact-table">

<style>
.compact-table table { margin: 0 !important; border-collapse: collapse; }
.compact-table th, .compact-table td { padding: 3px 4px !important; line-height: 2 !important; }
</style>

**פעולות והשפעות:**

| פעולה | השפעה |
| :--- | :--- |
| **$N$**  | $y {\leftarrow} y{-}1;\,\, bat {\leftarrow} bat{-}1$ |
| **$NE$** | $x {\leftarrow} x{-}1;\,\, y {\leftarrow} y{-}1;\,\, bat {\leftarrow} bat{-}1$ |
| **$E$**  | $x {\leftarrow} x{-}1;\,\, bat {\leftarrow} bat{-}1$ |
| **$SE$** | $x {\leftarrow} x{-}1;\,\, y {\leftarrow} y{+}1;\,\, bat {\leftarrow} bat{-}1$ |
| **$S$**  | $y {\leftarrow} y{+}1;\,\, bat {\leftarrow} bat{-}1$ |
| **$SW$** | $x {\leftarrow} x{+}1;\,\, y {\leftarrow} y{+}1;\,\, bat {\leftarrow} bat{-}1$ |
| **$W$**  | $x {\leftarrow} x{+}1;\,\, bat {\leftarrow} bat{-}1$ |
| **$NW$** | $x {\leftarrow} x{+}1;\,\, y {\leftarrow} y{-}1;\,\, bat {\leftarrow} bat{-}1$ |
| **$CH$** | $bat {\leftarrow} bat{+}1$ |
| **$TR$** | $bat {\leftarrow} bat{-}10$ |

</div>


<div class="flex justify-center mt-5 ml-60">
<TransitionSystemD3  
  :width="600" :height="250"
  :states="[
    { id: 'load', text: 'טעינה', x: 300, y: 50, width: 80, initial: true, initialDirection: 'top', initialText: '$bat=100 \\land x=0 \\land y=0$', initialTextWidth: 200 },
    { id: 'cart', text: 'תזוזה בצירים', x: 100, y: 180, width: 140 },
    { id: 'diag', text: 'תזוזה באלכסון', x: 500, y: 180, width: 140 }
  ]"
  :transitions="[
    { source: 'load', target: 'load', action: '$bat < 100 : CH$', actionWidth: 200,  loopDirection: '90deg' },
    { source: 'load', target: 'cart', action: '$bat > 10 : $  $nothing$', actionX: -20 },
    { source: 'load', target: 'diag', action: '$bat > 10 : $  $nothing$' },
    { source: 'cart', target: 'diag', action: '$TR$ $bat > 10 : $' },
    { source: 'diag', target: 'cart', action: '$TR$ $bat > 10 : $' },
    { source: 'cart', target: 'load', action: '$x=0 \\land y=0 : $ $nothing$', curve: -0.5, actionWidth: 150, actionX: -50 },
    { source: 'diag', target: 'load', action: '$x=0 \\land y=0 : $ $nothing$', curve: 0.5, actionWidth: 150, actionX: 10 },
    { source: 'cart', target: 'cart', action: 
    '$x<10 \\land bat>0 :  E$ <br> $x>0 \\land bat>0 :  W$ <br> $y<10 \\land bat>0 :  N$ <br> $y>0 \\land bat>0 :  S$', loopDirection: '90deg', actionWidth: 150, actionHeight: 40, actionY: 30 },
    { source: 'diag', target: 'diag', action: 
    '$x<10 \\land y>0 \\land bat>0 :  NE$ <br> $x>0 \\land y>0 \\land bat>0 :  NW$ <br> $y<10 \\land x>0 \\land bat>0 :  SE$ <br> $y<10 \\land x<10 \\land bat>0 :  SW$', loopDirection: '90deg', actionWidth: 250, actionHeight: 40, actionY: 30 },
  ]"
/>
</div>



