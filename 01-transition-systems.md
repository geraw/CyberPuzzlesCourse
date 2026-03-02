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

# מערכות מעברים <br> (Transition Systems)

##  הרצאה בקורס מבוא לאימות תוכנה <br> בשיטות פורמאליות
הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**<br>


<img src="https://in.bgu.ac.il/marketing/DocLib/Pages/graphics/just-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# נושאי הקורס 

<div class="flex justify-center">
  <img src="/images/course_topics_diagram_v2_mine.png" class="h-110 w-140"  /> 
</div>
 
---

#  בדיקות מודל (Model Checking)
 

<div class="flex justify-center">
  <img src="/images/model-checking-4.png" class="h-110 w-180"  /> 
</div>


---

# מערכת מעברים – Transition System

בקורס זה נתאר מערכות תגובתיות באמצעות מודל מתמטי הנקרא "מערכות מעברים".

<div class="grid grid-cols-2 gap-8">

<div>

מערכת מעברים נתונה על-ידי $\langle S, Act, \to, I, AP, L \rangle$ באשר:

- $S$ היא קבוצת המצבים.

- $I \subseteq S$ היא קבוצת המצבים ההתחלתיים.
- $Act$ היא קבוצת הפעולות.
- $\to \subseteq S \times Act \times S$ הוא יחס המעברים.
- $AP$ היא קבוצת הפסוקים האטומיים.
- $L\colon S \to 2^{AP}$ היא פונקצית התיוג.

</div>

<div class="flex flex-col items-center justify-start -mt-30">

<TransitionSystemD3  
  :states="[
    { id: 's0', text: '$s_0$', label: '$\\{p\\}$', initial: true, x: 442, y: 202 },
    { id: 's1', text: '$s_1$', label: '$\\{q\\}$', x: 229, y: 271 },
    { id: 's2', text: '$s_2$', label: '$\\{p,q\\}$', x: 269, y: 136 }
  ]"
  :transitions="[
    { source: 's0', target: 's1', action: '$\\alpha$' },
    { source: 's1', target: 's2', action: '$\\beta$' },
    { source: 's2', target: 's0', action: '$\\gamma$' },
    { source: 's2', target: 's2', action: '$\\delta$' }
  ]"
/>

<div dir="ltr" class="text-xs text-center -mt-16">

$S = \{s_0, s_1, s_2\}$, $\mathit{Act} = \{\alpha, \beta, \gamma, \delta\}$, $I = \{s_0\}$, $\mathit{AP} = \{p, q\}$

$\to = \{(s_0, \alpha, s_1), (s_1, \beta, s_2), (s_2, \gamma, s_0), (s_2, \delta, s_2)\}$

$L(s_0) = \{p\}, L(s_1) = \{q\}, L(s_2) = \{p,q\}$

</div>

</div>

</div>

---


# דוגמה: קוביה הונגרית

* קבוצת המצבים היא אוסף הקונפיגורציות האפשריות של הקוביה: $S$ (גודל המרחב כ-$4.3 \times 10^{19}$)
* פעולות: סיבוב של אחת הפאות ב-90 מעלות: $Act = \{U, D, L, R, F, B\}$
* פונקציית המעבר $\rightarrow \subseteq S \times Act \times S$:
    * לכל מצב $s$ ופעולה $\alpha$, המצב הבא הוא התוצאה של הפעלת הסיבוב $\alpha$ על $s$.
* המצב ההתחלתי הוא קונפיגורציה מבולגנת נתונה: $I = \{s_{start}\}$
* קבוצת פסוקים אטומים המכילה פסוק יחיד "מסודר": $AP = \{Sorted\}$
* פונקציית התיוג:
  $$ L(s) = \begin{cases} \{Sorted\}, & \text{if } s \text{ is solved} \\ \emptyset, & \text{otherwise} \end{cases} $$

<div class="mt-8 p-4 bg-yellow-100 rounded text-center">

  <b>שאלה:</b> האם קיימת סדרת פעולות שמובילה למצב מתוייג עם $Sorted$? (כן, לכל היותר 20 מהלכים)

</div>

---

# קידוד המצב בקוביה 2x2

<div class="grid grid-cols-2 gap-8 text-sm">
<div>

**המצבים:** $S$ היא קבוצת ה-8-יות של זוגות:
$$ s = \langle (p_0, r_0), (p_1, r_1), \dots, (p_7, r_7) \rangle $$

*   **האינדקסים $0..7$:** מייצגים את **8 הפינות הפיזיות** של הקוביה (Slots).
*   **הערכים $(p_i, r_i)$:**
    *   $p_i \in \{0..7\}$: איזה קוביה (Piece) נמצאת כרגע בפינה $i$.
    *   $r_i \in \{0,1,2\}$: האוריינטציה (סיבוב) של הקוביה בפינה $i$.
        *   $0$: הפאה הראשית (למשל Up/Down) פונה לכיוון $z$ (למעלה/למטה).
        *   $1$: מסובבת עם השעון.
        *   $2$: מסובבת נגד השעון.

**הפעולות:** $Act = \{U, F, R\}$
*   כל פעולה מחליפה מיקומים של 4 קוביות.
*   ומעדכנת את האוריינטציה שלהן ($r \pm 1 \pmod 3$).

</div>
<div class="flex flex-col items-center">

**מיפוי הפינות (דוגמה):**

<div class="grid grid-cols-2 gap-8 items-center justify-center">

<div class="flex flex-col items-center">
  <div class="text-xs font-bold mb-2">מצב לדוגמה (אחרי $R$):</div>
  <svg width="140" height="150" viewBox="0 0 100 110">
     <g stroke="black" stroke-width="0.5" stroke-linejoin="round">
      <!-- UP Face -->
      <!-- Left col (0, 2) remains White -->
      <path d="M25 22.5 L0 35 L25 47.5 L50 35 Z" fill="white"/>
      <path d="M50 35 L25 47.5 L50 60 L75 47.5 Z" fill="white"/>
      
      <!-- Right col (1, 3) comes from Front (Green) -->
      <path d="M75 22.5 L50 35 L75 47.5 L100 35 Z" fill="#22c55e"/> <!-- Back-Right -->
      <path d="M50 35 L25 47.5 L50 60 L75 47.5 Z" fill="#22c55e"/> <!-- Front-Right -->
      
      <!-- FRONT Face -->
      <!-- Left col (0, 4) remains Green -->
      <path d="M0 35 L25 47.5 L25 72.5 L0 60 Z" fill="#22c55e"/> <!-- Top-Left -->
      <path d="M0 60 L25 72.5 L25 97.5 L0 85 Z" fill="#22c55e"/> <!-- Bot-Left -->

      <!-- Right col (1, 5) comes from Down (Yellow) -->
      <path d="M25 47.5 L50 60 L50 85 L25 72.5 Z" fill="#eab308"/> <!-- Top-Right -->
      <path d="M25 72.5 L50 85 L50 110 L25 97.5 Z" fill="#eab308"/> <!-- Bot-Right -->

      <!-- RIGHT Face (Red) -->
      <path d="M50 60 L75 47.5 L75 72.5 L50 85 Z" fill="#ef4444"/>
      <path d="M75 47.5 L100 35 L100 60 L75 72.5 Z" fill="#ef4444"/>
      <path d="M50 85 L75 72.5 L75 97.5 L50 110 Z" fill="#ef4444"/>
      <path d="M75 72.5 L100 60 L100 85 L75 97.5 Z" fill="#ef4444"/>
    </g>
    <!-- Numbers overlay -->
    <g font-size="5" font-family="sans-serif" text-anchor="middle" fill="black" font-weight="bold" stroke="white" stroke-width="0.2">
      <text x="50" y="25">2</text>
      <text x="25" y="37">0</text>
      <text x="90" y="60">3</text>
      <text x="60" y="75">1</text>
      <text x="25" y="85">4</text>
      <text x="60" y="97">5</text>
      <text x="90" y="85">7</text>
    </g>
  </svg>
</div>

<div class="text-sm bg-blue-50 p-3 rounded">
  <b>וקטור המצב $s$:</b>
  $$ s = \langle (0,0), \color{red}{(5,1)}, (2,0), \color{red}{(1,2)}, (4,0), \color{red}{(7,2)}, (6,0), \color{red}{(3,1)} \rangle $$
  
  <b>הסבר:</b>
  <ul class="list-disc pl-4 mt-2 text-xs">
    <li>במיקום <b>1</b> (קדמי-ימני-עליון) נמצאת כעת קוביה מס' <b>5</b> (שהגיעה מלמטה).</li>
    <li>האוריינטציה שלה היא <b>1</b> (מסובבת עם השעון), כי הצבע הצהוב (שהיה למטה) פונה כעת ימינה.</li>
  </ul>
</div>

</div>

</div>
</div>

---

# הגדרת הפעולות (Transition Relations)

<div class="grid grid-cols-3 gap-4 text-sm items-start">

<!-- UP Action -->
<div class="flex flex-col items-center">

<div class="mb-2 text-center" dir="rtl">

**הפעולה $U$ (Up):** <br /> סיבוב הפאה העליונה.

<div class="text-xs text-right mt-1">

* מיקומים: $0 \to 2 \to 3 \to 1 \to 0$
* אוריינטציה: ללא שינוי ($+0$)

</div>
</div>

<svg width="100" height="110" viewBox="0 0 100 110">
<g stroke="black" stroke-width="0.5" stroke-linejoin="round">
<path d="M50 10 L25 22.5 L50 35 L75 22.5 Z" fill="white" />
<path d="M25 22.5 L0 35 L25 47.5 L50 35 Z" fill="white" />
<path d="M75 22.5 L50 35 L75 47.5 L100 35 Z" fill="white" />
<path d="M50 35 L25 47.5 L50 60 L75 47.5 Z" fill="white" />
<path d="M0 35 L25 47.5 L25 72.5 L0 60 Z" fill="#fb923c" />
<path d="M0 60 L25 72.5 L25 97.5 L0 85 Z" fill="#fb923c" />
<path d="M25 47.5 L50 60 L50 85 L25 72.5 Z" fill="#4ade80" />
<path d="M25 72.5 L50 85 L50 110 L25 97.5 Z" fill="#4ade80" />
<path d="M50 60 L75 47.5 L75 72.5 L50 85 Z" fill="#f87171" />
<path d="M75 47.5 L100 35 L100 60 L75 72.5 Z" fill="#f87171" />
<path d="M50 85 L75 72.5 L75 97.5 L50 110 Z" fill="#f87171" />
<path d="M75 72.5 L100 60 L100 85 L75 97.5 Z" fill="#f87171" />
<path d="M30 15 Q 50 5, 70 15" stroke="blue" stroke-width="3" fill="none" />
<polygon points="70,15 62,11 62,19" fill="blue" stroke="none" transform="rotate(-15 70 15)" />
</g>
<g font-size="5" font-family="sans-serif" text-anchor="middle" fill="black" font-weight="bold" stroke="white" stroke-width="0.2">
<text x="50" y="25">2</text>
<text x="25" y="37">0</text>
<text x="75" y="37">3</text>
<text x="50" y="50">1</text>
</g>
</svg>
</div>

<!-- FRONT Action -->
<div class="flex flex-col items-center">

<div class="mb-2 text-center" dir="rtl">

**הפעולה $F$ (Front):** <br /> סיבוב הפאה הקדמית.

<div class="text-xs text-right mt-1">

* מיקומים: $0 \to 1 \to 5 \to 4 \to 0$
* אוריינטציה: $\{0,1\} \to -1, \{4,5\} \to +1$

</div>
</div>

<svg width="100" height="110" viewBox="0 0 100 110">
<g stroke="black" stroke-width="0.5" stroke-linejoin="round" opacity="0.4">
<path d="M50 10 L25 22.5 L50 35 L75 22.5 Z" fill="white" />
<path d="M25 22.5 L0 35 L25 47.5 L50 35 Z" fill="white" />
<path d="M75 22.5 L50 35 L75 47.5 L100 35 Z" fill="white" />
<path d="M50 35 L25 47.5 L50 60 L75 47.5 Z" fill="white" />
<path d="M0 35 L25 47.5 L25 72.5 L0 60 Z" fill="#4ade80" />
<path d="M25 47.5 L50 60 L50 85 L25 72.5 Z" fill="#4ade80" />
<path d="M0 60 L25 72.5 L25 97.5 L0 85 Z" fill="#4ade80" />
<path d="M25 72.5 L50 85 L50 110 L25 97.5 Z" fill="#4ade80" />
<path d="M50 60 L75 47.5 L75 72.5 L50 85 Z" fill="#f87171" />
<path d="M75 47.5 L100 35 L100 60 L75 72.5 Z" fill="#f87171" />
<path d="M50 85 L75 72.5 L75 97.5 L50 110 Z" fill="#f87171" />
<path d="M75 72.5 L100 60 L100 85 L75 97.5 Z" fill="#f87171" />
</g>
<g stroke="black" stroke-width="1.5" stroke-linejoin="round">
<path d="M0 35 L25 47.5 L25 72.5 L0 60 Z" fill="#4ade80" />
<path d="M25 47.5 L50 60 L50 85 L25 72.5 Z" fill="#4ade80" />
<path d="M0 60 L25 72.5 L25 97.5 L0 85 Z" fill="#4ade80" />
<path d="M25 72.5 L50 85 L50 110 L25 97.5 Z" fill="#4ade80" />
</g>
<path d="M10 50 Q 25 35, 40 50" stroke="blue" stroke-width="3" fill="none" />
<polygon points="40,50 32,46 32,54" fill="blue" stroke="none" transform="rotate(45 40 50)" />
<g font-size="5" font-family="sans-serif" text-anchor="middle" fill="black" font-weight="bold" stroke="white" stroke-width="0.2">
<text x="10" y="57">0</text>
<text x="40" y="74">1</text>
<text x="10" y="85">4</text>
<text x="40" y="100">5</text>
</g>
</svg>
</div>

<!-- RIGHT Action -->
<div class="flex flex-col items-center">

<div class="mb-2 text-center" dir="rtl">

**הפעולה $R$ (Right):** <br /> סיבוב הפאה הימנית.

<div class="text-xs text-right mt-1">

* מיקומים: $1 \to 3 \to 7 \to 5 \to 1$
* אוריינטציה: $\{1,3\} \to -1, \{5,7\} \to +1$

</div>
</div>

<svg width="100" height="110" viewBox="0 0 100 110">
<g stroke="black" stroke-width="0.5" stroke-linejoin="round" opacity="0.4">
<path d="M50 10 L25 22.5 L50 35 L75 22.5 Z" fill="white" />
<path d="M25 22.5 L0 35 L25 47.5 L50 35 Z" fill="white" />
<path d="M75 22.5 L50 35 L75 47.5 L100 35 Z" fill="white" /> 
<path d="M50 35 L25 47.5 L50 60 L75 47.5 Z" fill="white" />
<path d="M0 35 L25 47.5 L25 72.5 L0 60 Z" fill="#4ade80" />
<path d="M25 47.5 L50 60 L50 85 L25 72.5 Z" fill="#4ade80" />
<path d="M0 60 L25 72.5 L25 97.5 L0 85 Z" fill="#4ade80" />
<path d="M25 72.5 L50 85 L50 110 L25 97.5 Z" fill="#4ade80" />
<path d="M50 60 L75 47.5 L75 72.5 L50 85 Z" fill="#f87171" />
<path d="M75 47.5 L100 35 L100 60 L75 72.5 Z" fill="#f87171" />
<path d="M50 85 L75 72.5 L75 97.5 L50 110 Z" fill="#f87171" />
<path d="M75 72.5 L100 60 L100 85 L75 97.5 Z" fill="#f87171" />
</g>
<g stroke="black" stroke-width="1.5" stroke-linejoin="round">
<path d="M50 60 L75 47.5 L75 72.5 L50 85 Z" fill="#f87171" />
<path d="M75 47.5 L100 35 L100 60 L75 72.5 Z" fill="#f87171" />
<path d="M50 85 L75 72.5 L75 97.5 L50 110 Z" fill="#f87171" />
<path d="M75 72.5 L100 60 L100 85 L75 97.5 Z" fill="#f87171" />
</g>
<path d="M60 60 Q 75 45, 90 60" stroke="blue" stroke-width="3" fill="none" />
<polygon points="90,60 82,56 82,64" fill="blue" stroke="none" transform="rotate(45 90 60)" />
<g font-size="5" font-family="sans-serif" text-anchor="middle" fill="black" font-weight="bold" stroke="white" stroke-width="0.2">
<text x="90" y="60">3</text>
<text x="60" y="75">1</text>
<text x="60" y="97">5</text>
<text x="90" y="85">7</text>
</g>
</svg>
</div>

</div>

<div class="mt-8 p-4 bg-blue-50 text-sm rounded shadow border-l-4 border-blue-500" dir="rtl">

<b>הערה לגבי האוריינטציה $(r)$:</b> <br />
סיבוב הפאות העליונה/תחתונה שומר על הצבע הלבן/צהוב בפאה העליונה/תחתונה, ולכן האוריינטציה לא משתנה $(+0)$.
לעומת זאת, סיבוב פאה צדדית (כמו $F$ או $R$) גורם לפינות "להתגלגל", כך שהצבע שהיה למעלה עובר לצד. זה מתבטא בשינוי אוריינטציה של $+1$ (עם השעון) או $-1$ (נגד כיוון השעון).

</div>

---

# סמנטיקה: ריצות ומקטעי ריצות

* **מקטע ריצה סופי:** רצף מתחלף של מצבים ופעולות המסתיים במצב:
  $$\rho = s_0 \alpha_1 s_1 \alpha_2 \dots \alpha_n s_n$$
  כך ש- $s_i \xrightarrow{\alpha_{i+1}} s_{i+1}$ לכל $0 \le i < n$.

* **מקטע ריצה אינסופי:** רצף אינסופי של מצבים ופעולות:
  $$\rho = s_0 \alpha_1 s_1 \alpha_2 \dots$$
  כך ש- $s_i \xrightarrow{\alpha_{i+1}} s_{i+1}$ לכל $i \ge 0$.

---

# שקילות מערכות מעברים

* התנהגות המערכת תוגדר באמצעות תיאור קבוצת הריצות שלה.
* נרצה לבדוק אם כל (סדרות התיוגים של) הריצות של המערכת "חוקיות".
* **שקילות:** שתי מערכות מעברים יקראו שקולות אם קבוצת הסדרות הנ"ל שוות.

---

<style>
.slidev-layout { direction: rtl; text-align: right; }
.katex-display, .katex { direction: ltr; } /* נוסחאות נשארות LTR */
code, pre { direction: ltr; text-align: left; }
.small { font-size: 0.9em; opacity: 0.95; }
.note { opacity: 0.8; font-size: 0.9em; }
.card {
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 14px;
  padding: 14px 16px;
  background: rgba(255,255,255,0.04);
}
.grid2 { display: grid; grid-template-columns: 1.2fr 1fr; gap: 18px; align-items: center; }
</style>

# מודל לקובייה הונגרית 2×2  
## מערכת מעברים — מצבים, פעולות, והדגמות ויזואליות

<div class="mt-6 grid2">
  <div class="card">
    <div class="small">
      מה נראה היום:
      <ul>
        <li>איך מייצגים מצב של 2×2 בצורה קומפקטית</li>
        <li>איך מגדירים פעולות U / R / F כמיפוי דטרמיניסטי בין מצבים</li>
        <li>הדגמות: קובייה 3D אינטראקטיבית + אנימציות SVG של המהלכים</li>
      </ul>
    </div>
    <div class="note">לא נכנסים לחבורות/תיאוריה עמוקה—רק מודל שימושי וברור.</div>
  </div>

  <div class="card">
    <Cube2x2 class="h-64" />
    <div class="note mt-2">גרור עם העכבר לסיבוב. גלגלת = זום.</div>
  </div>
</div>

---

# אינטואיציה: Slots מול Pieces

<div class="card">
<ul>
  <li><b>Slots (0..7)</b> — 8 מיקומים פיזיים קבועים (פינות) על הקובייה.</li>
  <li><b>Pieces (0..7)</b> — 8 חתיכות הפינה עצמן.</li>
</ul>

כל מצב אומר:
<ul>
  <li>איזו חתיכה יושבת בכל פינה</li>
  <li>ואיך היא “מסובבת” בתוך אותה פינה</li>
</ul>
</div>

---

# מספור הפינות (Slots) — בחירה קבועה

<div class="card">
נשתמש במספור סטנדרטי לפי מצב פתור (רק כדי שיהיה עקבי):

<ul>
  <li>0 = UFR (למעלה־קדימה־ימין)</li>
  <li>1 = URB (למעלה־ימין־אחורה)</li>
  <li>2 = UBL (למעלה־אחורה־שמאל)</li>
  <li>3 = ULF (למעלה־שמאל־קדימה)</li>
  <li>4 = DFR (למטה־קדימה־ימין)</li>
  <li>5 = DRB (למטה־ימין־אחורה)</li>
  <li>6 = DBL (למטה־אחורה־שמאל)</li>
  <li>7 = DLF (למטה־שמאל־קדימה)</li>
</ul>
</div>

---

# ייצוג מצב

<div class="card">
מצב הוא 8־ייה של זוגות:
\[
s = \langle (p_0,r_0), (p_1,r_1), \dots, (p_7,r_7) \rangle
\]

לכל פינה \(i\):
<ul>
  <li>\(p_i \in \{0..7\}\): איזו <b>חתיכה</b> נמצאת כרגע ב־slot \(i\)</li>
  <li>\(r_i \in \{0,1,2\}\): האוריינטציה שלה (Twist) מודולו 3</li>
</ul>
</div>

<div class="note mt-2">
אפשר לחשוב על זה כמו "לוח" עם 8 תאים: בכל תא כתוב מי יושב שם + איך הוא מסובב.
</div>

---

# פעולות: U / R / F

<div class="card">
נבחר את קבוצת הפעולות:
\[
Act=\{U,F,R\}
\]

כל פעולה:
<ul>
  <li>מחליפה מיקומים של <b>4 פינות</b> (מחזור)</li>
  <li>ומעדכנת אוריינטציה של אותן פינות ב־\(\pm 1 \pmod 3\) לפי הכללים של הקובייה</li>
</ul>
</div>

---

# “מה זה אומר פורמלית?” (בלי להעמיס)

<div class="card">
נגדיר לכל פעולה \(a\) פונקציה דטרמיניסטית:
\[
\delta_a: S \to S
\]

ואז המעבר הוא פשוט:
\[
s \xrightarrow{a} s' \iff s'=\delta_a(s)
\]

הפואנטה: זה בדיוק "מכונת מצבים" שבה כל צעד הוא U/R/F.
</div>

---

# הדגמה אינטראקטיבית: הקובייה מסתובבת בלייב

<div class="card">
<Cube2x2 class="h-96" />
</div>

<div class="note mt-2">
זה שקף “להרגיש את המודל”: פעולה היא פשוט מעבר—אפשר לחבר אחר כך גם כפתורים שמפעילים U/R/F על המצב.
</div>

---

# אנימציית מהלך U (סיבוב שכבת העליונה)

<div class="grid2">
  <div class="card">
    <h3>U</h3>
    <ul>
      <li>מסובב את ארבע פינות השכבה העליונה במחזור.</li>
      <li>ויזואלית: הריבוע העליון מסתובב.</li>
    </ul>
  </div>
  <div class="card">
    <MoveU class="w-full h-72" />
  </div>
</div>

---

# אנימציית מהלך R (סיבוב הפאה הימנית)

<div class="grid2">
  <div class="card">
    <h3>R</h3>
    <ul>
      <li>מסובב את ארבע הפינות שעל "עמודת ימין".</li>
      <li>ויזואלית: הצד הימני מתחלף במחזור.</li>
    </ul>
  </div>
  <div class="card">
    <MoveR class="w-full h-72" />
  </div>
</div>

---

# אנימציית מהלך F (סיבוב הפאה הקדמית)

<div class="grid2">
  <div class="card">
    <h3>F</h3>
    <ul>
      <li>מסובב את ארבע הפינות של הפאה הקדמית.</li>
      <li>ויזואלית: השורה הקדמית מתחלפת במחזור.</li>
    </ul>
  </div>
  <div class="card">
    <MoveF class="w-full h-72" />
  </div>
</div>

---

# סיכום

<div class="card">
מה קיבלנו:
<ul>
  <li><b>מצב</b> = 8־ייה של (איזה piece, איזה twist).</li>
  <li><b>פעולה</b> = מעבר דטרמיניסטי שמזיז 4 פינות ומעדכן twist.</li>
  <li><b>מערכת מעברים</b> = בסיס מצוין לחיפוש מסלולים, בדיקת תכונות, או הדמיה.</li>
</ul>
</div>

<div class="note mt-2">
אם תרצה בשלב הבא: אני יכול להוסיף לשקף האינטראקטיבי כפתורים שמפעילים U/R/F על מצב פנימי ומציגים את המצב בטבלה.
</div>
