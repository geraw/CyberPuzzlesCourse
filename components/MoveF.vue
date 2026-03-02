<template>
  <svg viewBox="0 0 520 320" class="w-full h-full" aria-label="F move animation">
    <defs>
      <marker id="arrowF" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto">
        <path d="M0,0 L10,5 L0,10 z" fill="currentColor" />
      </marker>
    </defs>

    <rect x="20" y="20" width="480" height="280" rx="18" fill="none" stroke="currentColor" opacity="0.25"/>
    <text x="40" y="55" fill="currentColor" font-size="18" opacity="0.9">F: סיבוב הפאה הקדמית</text>

    <!-- “הפאה הקדמית” כמלבן -->
    <rect x="140" y="85" width="240" height="190" rx="18"
          fill="none" stroke="currentColor" opacity="0.38" stroke-width="4"/>

    <!-- ארבע הפינות של הפאה הקדמית (מופשט) -->
    <g fill="currentColor" opacity="0.9">
      <circle cx="170" cy="115" r="10"/>
      <circle cx="350" cy="115" r="10"/>
      <circle cx="350" cy="245" r="10"/>
      <circle cx="170" cy="245" r="10"/>
    </g>

    <!-- חיצים סביב המסגרת -->
    <g stroke="currentColor" stroke-width="4" fill="none" opacity="0.75" marker-end="url(#arrowF)">
      <path d="M180 110 C240 80, 280 80, 340 110"/>
      <path d="M350 130 C390 170, 390 190, 350 230"/>
      <path d="M340 250 C280 280, 240 280, 180 250"/>
      <path d="M170 230 C130 190, 130 170, 170 130"/>
    </g>

    <path id="fPath" d="M180 110 C240 80, 280 80, 340 110
                        C390 150, 390 200, 350 230
                        C340 250, 280 280, 180 250
                        C130 220, 130 150, 170 130
                        C175 120, 178 115, 180 110" fill="none" stroke="none"/>
    <circle r="9" fill="currentColor">
      <animateMotion dur="2.2s" repeatCount="indefinite" rotate="auto">
        <mpath href="#fPath" />
      </animateMotion>
    </circle>
  </svg>
</template>
