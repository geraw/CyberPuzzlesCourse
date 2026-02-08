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

<div class="grid grid-cols-3 gap-1 text-center font-mono text-xs mb-4">
  <!-- Top: Up -->
  <div></div>
  <div class="border border-gray-400 p-1 bg-yellow-100">
    <div>2&nbsp;&nbsp;3</div>
    <div>Up</div>
    <div>0&nbsp;&nbsp;1</div>
  </div>
  <div></div>

  <!-- Mid: L F R B -->
  <div class="border border-gray-400 p-1 bg-orange-100">
    <div>2&nbsp;&nbsp;0</div>
    <div>Left</div>
    <div>6&nbsp;&nbsp;4</div>
  </div>
  <div class="border border-gray-400 p-1 bg-green-100">
    <div>0&nbsp;&nbsp;1</div>
    <div>Front</div>
    <div>4&nbsp;&nbsp;5</div>
  </div>
  <div class="border border-gray-400 p-1 bg-red-100">
    <div>1&nbsp;&nbsp;3</div>
    <div>Right</div>
    <div>5&nbsp;&nbsp;7</div>
  </div>

  <!-- Bot: Down -->
  <div></div>
  <div class="border border-gray-400 p-1 bg-white">
    <div>4&nbsp;&nbsp;5</div>
    <div>Down</div>
    <div>6&nbsp;&nbsp;7</div>
  </div>
  <div class="border border-gray-400 p-1 bg-blue-100">
    <div>3&nbsp;&nbsp;2</div>
    <div>Back</div>
    <div>7&nbsp;&nbsp;6</div>
  </div>
</div>

<div class="bg-blue-50 p-2 rounded text-xs w-full">
  <b>דוגמה:</b> פינה מס' $0$ היא הפינה הקדמית-שמאלית-עליונה (Front-Up-Left).
  <br>
  אם $s = \langle (3, 1), \dots \rangle$, זה אומר שבפינה $0$ נמצאת הקוביה שהייתה במקור בפינה $3$, והיא מסובבת "פעם אחת".
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
* אוריינטציה: $+1$ (עם השעון)

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
* אוריינטציה: $+1$ (עם השעון)

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
* אוריינטציה: $+1$ (עם השעון)

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

