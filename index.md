---
# הגדרות ערכת נושא ועיצוב
theme: seriph
background: https://get.wallhere.com/photo/white-background-minimalism-circuit-board-blue-circuits-technology-1563214.jpg
class: text-center
highlighter: shiki
lineNumbers: true
dir: rtl
drawings:
  enabled: true

# הגדרות סגנון מותאמות אישית (CSS)
style: |
  .slidev-layout h1 {
    color: #003366; /* כחול בן גוריון */
  }
  .bgu-logo {
    position: absolute;
    top: 20px;
    left: 20px;
    width: 80px;
  }
  .department-footer {
    position: absolute;
    bottom: 10px;
    right: 20px;
    font-size: 0.8em;
    color: #666;
  }
---

# מבוא לאימות תוכנה בשיטות פורמאליות
### המחלקה למדעי המחשב | אוניברסיטת בן-גוריון 

**מרצה: גרא וייס**

<img src="https://in.bgu.ac.il/marketing/DocLib/Pages/visual-identity/BGU_Logo_Heb_Eng_V_Color.png" class="bgu-logo" />

<div class="department-footer">המחלקה למדעי המחשב | BGU CS</div>

---

# מהות השיטה הפורמלית

אימות פורמלי מתמקד בסריקה שיטתית של מרחב המצבים. 

במערכות מקביליות, אנו מתמודדים עם בעיית ה**שזירה (Interleaving)**.
מספר הריצות האפשריות $M$ עבור $N$ תהליכים כאשר לכל תהליך $n_i$ פעולות מחושב כך:

$$M = \frac{(\sum_{i=1}^{N} n_i)!}{\prod_{i=1}^{N} (n_i!)}$$ 



---
layout: default
---

# למה להשקיע באימות תוכנה?

* **עלות כלכלית**: שגיאות תוכנה עולות כ-60 מיליארד דולר בשנה בארה"ב בלבד.
* **בטיחות**: הסתמכות גוברת על מערכות קריטיות כמו כורים אטומיים ורכבים אוטונומיים.
* **אמינות**: במערכות מורכבות, בדיקות (Testing) רגילות לא מכסות את כל מקרי הקצה.

> "אימות (Verification) הוא הבדיקה שאנחנו בונים את הדבר נכון".

---