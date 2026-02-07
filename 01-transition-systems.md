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

<VennDiagram 
  annotationText="נתחיל כאן"
  :annotationX="100"
  :annotationY="190"
  :annotationRotate="0"
  :arrowPath="'M40,195 Q40,240 90,280'"
  :topText="['שפות לתיאור', 'מערכות', '(תגובתיות)']"
  :leftText="[ 'אלגוריתמים', 'לאימות', 'model-checking']" 
  :rightText="['שפות לתיאור', 'דרישות', '(תכונות של', 'מערכות)']"
/>

---

#  בדיקות מודל (Model Checking)


<div class="flex justify-center">
  <img src="/images/model-checking-4.png" class="h-110" />
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

<div class="flex items-center justify-center">

<TransitionSystemD3  
  :states="[
    { id: 's0', text: '$s_0$', label: '$\\{p\\}$',  initial: true },
    { id: 's1', text: '$s_1$', label: '$\\{q\\}$'},
    { id: 's2', text: '$s_2$', label: '$\\{p,q\\}$'}
  ]"
  :transitions="[
    { source: 's0', target: 's1', action: '$\\alpha$' },
    { source: 's1', target: 's2', action: '$\\beta$' },
    { source: 's2', target: 's0', action: '$\\gamma$' },
    { source: 's2', target: 's2', action: '$\\delta$' }
  ]"
  :auto="true"
  :width="300"
  :height="300" 
/>

</div>

</div>

---

# דוגמה: מערכת מעברים פשוטה

שקול את המערכת הבאה עבור משתנה $x \in \{0, 1\}$:

- **מצבים:** $S = \{s_0, s_1\}$
- **מצבים התחלתיים:** $I = \{s_0\}$
- **מעברים:** $(s_0, \text{inc}, s_1), (s_1, \text{dec}, s_0)$
- **תיוג:** $L(s_0) = \{x=0\}$, $L(s_1) = \{x=1\}$

---

# דוגמה: מערכת מעברים אינסופית

* קבוצת המצבים היא קבוצת המספרים הטבעיים (כולל 0): $S = \mathbb{N}$
* שתי פעולות: הגדלה ב-1 וכפל ב-2: $Act = \{inc, double\}$
* פונקציית המעבר $\rightarrow \subseteq S \times Act \times S$:
    * (פעולת ההגדלה) $(s, inc, s+1) \quad \forall s \in \mathbb{N}$
    * (פעולת הכפל) $(s, double, 2s) \quad \forall s \in \mathbb{N}$
* המצב ההתחלתי הוא 0: $I = \{0\}$
* קבוצת פסוקים אטומים המכילה פסוק יחיד $P$: $AP = \{P\}$
* פונקציית התיוג:
  $$ L(s) = \begin{cases} \{P\}, & \text{if } \exists k \ge 0 \text{ s.t. } s = 3^k \\ \emptyset, & \text{otherwise} \end{cases} $$

<div class="mt-8 p-4 bg-yellow-100 rounded text-center">
  <b>שאלה:</b> האם קיימת סדרת פעולות שמובילה למצב מתוייג עם $P$ (כלומר, חזקת 3)?
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

