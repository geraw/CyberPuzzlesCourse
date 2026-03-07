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

# התנהגות אינטואיטיבית ואי-דטרמיניזם

לשם נוחות, נסמן $s \xrightarrow{\alpha} s'$ במקום $(s, \alpha, s') \in\ \to$. 

ההתנהגות של מערכת מעברים מתוארת באופן הבא:

* המערכת מתחילה במצב התחלתי כלשהו $s_0 \in I$ ומתפתחת על פי יחס המעברים $\to$.
  
* בכל שלב, אם $s$ הוא המצב הנוכחי, מעבר יוצא $s \xrightarrow{\alpha} s'$ נבחר באופן אי-דטרמיניסטי ומבוצע.
  כלומר, הפעולה $\alpha$ מתבצעת והמערכת עוברת מ-$s$ למצב $s'$.
* תהליך זה חוזר על עצמו במצב $s'$, ומסתיים רק כאשר נתקלים במצב שאין ממנו מעברים יוצאים.

<div class="mt-8 p-4 bg-blue-50 text-base rounded shadow border-l-4 border-blue-500" dir="rtl">

<b>אי-דטרמיניזם, לא הסתברות:</b> <br/>
חשוב להבין שבמקרה שלמצב יש יותר ממעבר יוצא אחד, המעבר הבא נבחר באופן <b>אי-דטרמיניסטי טהור</b>.
כלומר, תוצאת הבחירה אינה ידועה מראש, ולכן <b>לא ניתן להביע שום טענה על ההסתברות או הסבירות שמעבר מסוים ייבחר</b>.<br>
באופן דומה, כאשר קבוצת המצבים ההתחלתיים כוללת יותר ממצב אחד, מצב הפתיחה נבחר אי-דטרמיניסטית.

</div>

---

# פונקציית התיוג (Labeling Function)

פונקציית התיוג $L \colon S \to 2^{AP}$ מקשרת בין קבוצת פסוקים אטומיים $L(s) \in 2^{AP}$ לכל מצב $s \in S$. 

באופן אינטואיטיבי, $L(s)$ מייצגת בדיוק את אותם פסוקים אטומיים $a \in AP$ שמתקיימים במצב $s$.

* בהינתן ש-$\Phi$ היא נוסחת לוגיקה פסוקית, נאמר ש-$s$ מקיים את הנוסחה $\Phi$ אם ההשמה שמושרה על ידי הקבוצה $L(s)$ הופכת את הנוסחה לאמיתית. 

* כלומר, נסמן:
$$ s \models \Phi \quad \text{iff} \quad L(s) \models \Phi $$   

* **השמה שמושרה על ידי קבוצה:** כל פסוק מקבל ערך True אם הוא שייך לקבוצה, ו-False אם הוא לא שייך לקבוצה.

<div class="mt-8 p-4 bg-yellow-100 rounded text-center">


<b>משמעות:</b> פונקציית התיוג מעניקה לשמות המצבים את המשמעות מנקודת המבט של התכונות שניתן להביע על המערכת. היא הופכת את מצבי המערכת מ"סתם משתנים" לייצוג לוגי הניתן לאימות.

</div>


---

# דוגמה: רובוט במבוך

נניח רובוט שנע בתוך מבוך המיוצג כרשת משבצות $4 \times 4$.
המצבים של המערכת הם הקואורדינטות של הרובוט: $S = \{ (i,j) \mid 1 \le i \le 4, 1 \le j \le 4 \}$.
פעולות המעבר האפשריות הן תזוזה לאחת מארבעת הכיוונים (למשבצות פנויות בלבד).

נגדיר שני פסוקים אטומיים: $AP = \{\text{TH}, \text{EH}\}$.   (קיצור של- **T**op**H**alf, **R**ight**H**alf)

פונקציית התיוג $L$ מתרגמת את המטריקה של הרשת לתכונות לוגיות פשוטות :
- רובוט נמצא בחצי העליון של הרשת: $\text{TH} \in L((i,j)) \iff j \ge 3$
- רובוט נמצא בחצי הימני של הרשת: $\text{RH} \in L((i,j)) \iff i \ge 3$

<div class="grid grid-cols-2 gap-4 mt-6">
<div>

* **לדוגמה:**
  - $L((4,4)) = \{\text{TH}, \text{RH}\}$

  - $L((1,1)) = \emptyset$
  - $L((3,1)) = \{\text{RH}\}$

</div>
<div>

* **אימות תכונות:**
  - ניתן לשאול : 
"האם הרובוט יכול להגיע למצב  
$s \models\text{TH} \land \text{RH}$ מבלי לעבור אף פעם במצב  $s \models \neg\text{RH}$?"
  - הפרדה בין האימות למבנה הפנימי של המערכת
</div>
</div>

---

# דוגמה: מסלול במבוך

נבחן שני מסלולים אפשריים במערכת המעברים של הרובוט מרגע ההתחלה $(3,1)$.
המטרה: **להגיע ל-$TH \land RH$ (כלומר $i \ge 3, j \ge 3$) מבלי לצאת מה-$RH$ ($i \ge 3$)**.

<div class="grid grid-cols-2 gap-4 mt-4">
<div>

<div class="bg-green-100 p-2 rounded text-center mb-2 text-sm font-bold border border-green-400">
✅ מסלול עומד בדרישה
</div>

<TransitionSystemD3  
  :width="400" :height="200"
  :states="[
    { id: 's0', text: '$(3,1)$', label: '$\\{RH\\}$', initial: true, initialDirection: 'right', x: 200, y: 180 },
    { id: 's1', text: '$(3,2)$', label: '$\\{RH\\}$', x: 200, y: 90 },
    { id: 's2', text: '$(3,3)$', label: '$\\{TH, RH\\}$', x: 200, y: 0 }
  ]"
  :transitions="[
    { source: 's0', target: 's1', action: '$Up$' },
    { source: 's1', target: 's2', action: '$Up$' }
  ]"
/>

<div class="text-xs text-center mt-2" dir="ltr">

$L: \{RH\} \to \{RH\} \to \{TH,RH\}$

</div>
<div class="text-sm text-center mt-1">
הרובוט נע צפונה פעמיים, נשאר בחצי הימני כל הדרך עד למטרה.
</div>

</div>
<div>

<div class="bg-red-100 p-2 rounded text-center mb-2 text-sm font-bold border border-red-400">
❌ מסלול אינו עומד בדרישה
</div>

<TransitionSystemD3  
  :width="400" :height="200" 
  :states="[
    { id: 's0', text: '$(3,1)$', label: '$\\{RH\\}$', initial: true, initialDirection: 'right',  x: 280, y: 180 },
    { id: 's1', text: '$(2,1)$', label: '$\\emptyset$', x: 120, y: 180 },
    { id: 's2', text: '$(2,2)$', label: '$\\emptyset$', x: 120, y: 90 },
    { id: 's3', text: '$(2,3)$', label: '$\\{TH\\}$', x: 120, y: 0 },
    { id: 's4', text: '$(3,3)$', label: '$\\{TH, RH\\}$', x: 280, y: 0 }
  ]"
  :transitions="[
    { source: 's0', target: 's1', action: '$Left$' },
    { source: 's1', target: 's2', action: '$Up$' },
    { source: 's2', target: 's3', action: '$Up$' },
    { source: 's3', target: 's4', action: '$Right$' }
  ]"
/>

<div class="text-xs text-center mt-2" dir="ltr">

$L: \{RH\} \to \emptyset \to \emptyset \to \{TH\} \to \{TH,RH\}$

</div>
<div class="text-sm text-center mt-1">
הרובוט עוקף מכשול דרך החצי השמאלי, תוך הפרת הדרישה.
</div>

</div>
</div>

---


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

