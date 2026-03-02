<template>
  <svg viewBox="0 0 520 320" class="w-full h-full" aria-label="U move animation">
    <defs>
      <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto">
        <path d="M0,0 L10,5 L0,10 z" fill="currentColor" />
      </marker>
    </defs>

    <!-- מסגרת -->
    <rect x="20" y="20" width="480" height="280" rx="18" fill="none" stroke="currentColor" opacity="0.25"/>

    <!-- נקודות (4 עליונות + 4 תחתונות) -->
    <g fill="currentColor" opacity="0.9">
      <!-- top -->
      <circle cx="170" cy="100" r="10"/>
      <circle cx="350" cy="100" r="10"/>
      <circle cx="350" cy="180" r="10" opacity="0.25"/>
      <circle cx="170" cy="180" r="10" opacity="0.25"/>

      <!-- bottom (faded) -->
      <circle cx="170" cy="240" r="10" opacity="0.25"/>
      <circle cx="350" cy="240" r="10" opacity="0.25"/>
      <circle cx="350" cy="280" r="0" opacity="0"/>
      <circle cx="170" cy="280" r="0" opacity="0"/>
    </g>

    <!-- כותרת -->
    <text x="40" y="55" fill="currentColor" font-size="18" opacity="0.9">U: סיבוב שכבה עליונה</text>

    <!-- ריבוע עליון מודגש -->
    <rect x="140" y="70" width="240" height="140" rx="16"
          fill="none" stroke="currentColor" opacity="0.35" stroke-width="3"/>

    <!-- חיצים למחזור (0→1→2→3→0 על הריבוע העליון) -->
    <g stroke="currentColor" stroke-width="4" fill="none" opacity="0.75" marker-end="url(#arrow)">
      <path d="M180 90 C240 60, 280 60, 340 90"/>
      <path d="M360 120 C390 150, 390 170, 360 200"/>
      <path d="M340 220 C280 250, 240 250, 180 220"/>
      <path d="M160 200 C130 170, 130 150, 160 120"/>
    </g>

    <!-- נקודה שמסתובבת לאורך המסלול -->
    <path id="uPath" d="M180 90 C240 60, 280 60, 340 90
                        C390 120, 390 180, 360 200
                        C340 220, 280 250, 180 220
                        C130 200, 130 150, 160 120
                        C170 110, 175 100, 180 90" fill="none" stroke="none"/>
    <circle r="9" fill="currentColor">
      <animateMotion dur="2.2s" repeatCount="indefinite" rotate="auto">
        <mpath href="#uPath" />
      </animateMotion>
    </circle>
  </svg>
</template>
