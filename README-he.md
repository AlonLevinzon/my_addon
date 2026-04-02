# תבנית addon כתוביות עבריות ל-Stremio

זהו addon סטטי ופשוט מאוד ל-Stremio.

הוא עובד דרך GitHub Pages, בלי שרת ביתי ובלי מחשב שצריך להישאר דולק.

## מה יש כאן

- `manifest.json` — קובץ הזיהוי של ה-addon
- `subtitles/movie/tt0111161.json` — דוגמה לסרט אחד לפי IMDb ID
- `files/tt0111161.he.srt` — קובץ כתוביות לדוגמה
- `tools/create_movie_subtitle_json.py` — סקריפט עזר ליצירת קובץ JSON חדש לסרט

## איך להעלות את זה ל-GitHub Pages

### 1. פתח repository חדש ב-GitHub
לדוגמה:
`stremio-hebrew-subtitles`

### 2. העלה אליו את כל הקבצים שבתיקייה הזאת

### 3. הפעל GitHub Pages
ב-GitHub:
- היכנס ל-Settings
- לחץ Pages
- תחת Build and deployment בחר:
  - Source: `Deploy from a branch`
  - Branch: `main`
  - Folder: `/ (root)`

אחרי כמה דקות תהיה לך כתובת בערך כזאת:

`https://YOUR_USERNAME.github.io/YOUR_REPO`

## מה צריך לשנות לפני ההתקנה ב-Stremio

### 1. ערוך את `manifest.json`
החלף את:
- `com.yourname.hebrewsubtitles` למשהו משלך
- `My Hebrew Subtitles` לשם שאתה רוצה

### 2. ערוך את קובץ ה-JSON של הסרט
בקובץ:
`subtitles/movie/tt0111161.json`

החלף את:
`https://YOUR_USERNAME.github.io/YOUR_REPO/files/tt0111161.he.srt`

לכתובת האמיתית שלך ב-GitHub Pages.

דוגמה:
`https://alonlevinzon.github.io/stremio-hebrew-subtitles/files/tt0111161.he.srt`

### 3. החלף את קובץ ה-SRT
בקובץ:
`files/tt0111161.he.srt`

שים את הכתוביות האמיתיות שלך.

## איך מוסיפים סרט חדש

נניח שיש לך סרט עם IMDb ID:
`tt1375666`

### אפשרות ידנית

1. שים קובץ כתוביות בתיקייה `files`
   לדוגמה:
   `files/tt1375666.he.srt`

2. צור קובץ חדש:
   `subtitles/movie/tt1375666.json`

3. שים בו את התוכן הבא:

```json
{
  "subtitles": [
    {
      "id": "tt1375666-he-1",
      "lang": "heb",
      "url": "https://YOUR_USERNAME.github.io/YOUR_REPO/files/tt1375666.he.srt"
    }
  ],
  "cacheMaxAge": 300,
  "staleRevalidate": 3600,
  "staleError": 86400
}
```

### אפשרות עם הסקריפט

הרץ מתוך התיקייה הראשית:

```bash
python tools/create_movie_subtitle_json.py tt1375666 https://YOUR_USERNAME.github.io/YOUR_REPO tt1375666.he.srt
```

## איך מתקינים ב-Stremio

אחרי ש-GitHub Pages פעיל:

הכתובת להתקנה היא:

`https://YOUR_USERNAME.github.io/YOUR_REPO/manifest.json`

את הכתובת הזאת פותחים בדפדפן במחשב שבו מחובר Stremio, ולוחצים Install.
אם אותו חשבון Stremio מחובר גם בטלוויזיה, ה-addon יופיע גם שם.

## מגבלה חשובה

התבנית הזאת כרגע מוגדרת ל-`movie` בלבד.
כלומר היא מיועדת לסרטים.

אם תרצה בהמשך, אפשר להרחיב גם ל-`series`.
