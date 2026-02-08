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
  <img src="/images/course_topics_diagram_final.png" class="h-110 w-140"  /> 
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

