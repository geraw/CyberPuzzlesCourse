<template>
  <svg viewBox="0 0 520 320" class="w-full h-full" aria-label="R move animation">
    <defs>
      <marker id="arrowR" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto">
        <path d="M0,0 L10,5 L0,10 z" fill="currentColor" />
      </marker>
    </defs>

    <rect x="20" y="20" width="480" height="280" rx="18" fill="none" stroke="currentColor" opacity="0.25"/>
    <text x="40" y="55" fill="currentColor" font-size="18" opacity="0.9">R: סיבוב הפאה הימנית</text>

    <!-- גריד 2x2 “עליון” + “תחתון” כריבועים -->
    <g stroke="currentColor" fill="none" opacity="0.25">
      <rect x="140" y="70" width="240" height="140" rx="16" stroke-width="3"/>
      <rect x="140" y="210" width="240" height="70" rx="16" stroke-width="2"/>
    </g>

    <!-- הדגשת העמודה הימנית -->
    <rect x="270" y="70" width="110" height="210" rx="16"
          fill="none" stroke="currentColor" opacity="0.40" stroke-width="4"/>

    <!-- נקודות ארבע הפינות המשתתפות במחזור (ימין-עליון, ימין-אמצע, ימין-תחתון-ימין, ימין-תחתון-שמאל כאנלוגיה) -->
    <g fill="currentColor" opacity="0.9">
      <circle cx="350" cy="100" r="10"/>
      <circle cx="350" cy="180" r="10"/>
      <circle cx="350" cy="240" r="10"/>
      <circle cx="290" cy="240" r="10" opacity="0.35"/>
    </g>

    <!-- חיצים למחזור לאורך “עמודת ימין” -->
    <g stroke="currentColor" stroke-width="4" fill="none" opacity="0.75" marker-end="url(#arrowR)">
      <path d="M350 110 C390 140, 390 160, 350 190"/>
      <path d="M350 190 C390 215, 390 230, 360 245"/>
      <path d="M340 245 C310 265, 300 265, 295 250"/>
      <path d="M295 230 C280 200, 305 140, 335 110"/>
    </g>

    <path id="rPath" d="M350 110 C390 140, 390 160, 350 190
                        C390 215, 390 230, 360 245
                        C340 245, 310 265, 295 250
                        C280 235, 300 170, 335 110
                        C342 102, 346 100, 350 110" fill="none" stroke="none"/>
    <circle r="9" fill="currentColor">
      <animateMotion dur="2.2s" repeatCount="indefinite" rotate="auto">
        <mpath href="#rPath" />
      </animateMotion>
    </circle>
  </svg>
</template>
