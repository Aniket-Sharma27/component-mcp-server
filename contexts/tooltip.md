---
realComponent: ion-tooltip
description: A transient overlay that displays contextual information anchored to an HTML element with automatic positioning and re-positioning behavior using the popup component internally
themes: [modern-light-ds, modern-dark-ds]
apiTypes: ["element", "service"]
serviceApi:
  serviceName: TooltipService
  importPath: "../tooltip/tooltipService"
  methods:
    - name: createTooltip
      signature: "createTooltip<T extends ITooltip | IDsTooltip>(tooltipElement: string | HTMLElement, tooltipAnchor: HTMLElement, tooltipOptions: IDsTooltipOptions | ITooltipOptions): T"
      configInterface:
        - field: intent
          type: "TooltipIntent"
          required: false
          description: "Semantic intent affecting tooltip styling: 'neutral' | 'secondary' | 'negative' | 'positive' | 'warning' | 'info'"
        - field: content
          type: "string"
          required: false
          description: "Tooltip message content as text string"
        - field: showIcon
          type: "boolean"
          required: false
          description: "Whether to show intent-based icon in tooltip"
        - field: hideCaret
          type: "boolean"
          required: false
          description: "Whether to hide the tooltip caret/arrow"
        - field: placement
          type: "TooltipPlacement"
          required: false
          description: "Position relative to anchor: 'auto' | 'top' | 'topStart' | 'topEnd' | 'right' | 'rightStart' | 'rightEnd' | 'bottom' | 'bottomStart' | 'bottomEnd' | 'left' | 'leftStart' | 'leftEnd' | 'cursor'"
        - field: fallbackPlacementBehavior
          type: "FallbackPlacementBehavior"
          required: false
          description: "Repositioning behavior: 'flip' | 'shift' | 'flip-shift' | 'none'"
        - field: offset
          type: "string"
          required: false
          description: "Spacing between tooltip and anchor in pixels"
        - field: inheritParentWidth
          type: "string"
          required: false
          description: "Width inheritance behavior as MQ design string or boolean value"
        - field: trigger
          type: "TooltipTrigger"
          required: false
          description: "Display trigger: 'hover' | 'press' | 'manual'"
        - field: open
          type: "boolean"
          required: false
          description: "Initial visibility state (only for manual trigger)"
        - field: openDelay
          type: "number"
          required: false
          description: "Delay before showing tooltip in milliseconds"
        - field: closeDelay
          type: "number"
          required: false
          description: "Delay before hiding tooltip in milliseconds"
        - field: autoFocus
          type: "boolean"
          required: false
          description: "Whether focus moves to first interactive element in tooltip"
        - field: enableFocus
          type: "boolean"
          required: false
          description: "Whether focus management is enabled"
        - field: originAnchorId
          type: "string"
          required: false
          description: "ID of anchor element for accessibility"
        - field: cursorPosition
          type: "{x: number, y: number}"
          required: false
          description: "Manual cursor position coordinates for placement=cursor"
      returns: "IDsTooltip | ITooltip object with properties and methods including intent, open, content, offset, openDelay, closeDelay, inheritParentWidth, fallbackPlacementBehavior, hideCaret, placement, showIcon, trigger, onOpen, onClose, destroy(), forceOpen(), flash()"
props:
  - name: intent
    type: enum
    category: visual
    required: false
    default: "neutral"
    values: [neutral, secondary, positive, warning, negative, info]
    designTokens:
      neutral:
        light:
          resolvesTo: "#030c1e"
          tokenChain: "tooltip container background -> --ion-comp-tooltip-container-color-bg-neutral -> --ion-comp-popover-container-color-bg -> variable for popover background (#030c1e)"
          appliesToCssProperty: "background-color"
      positive:
        light:
          resolvesTo: "#030c1e"
          tokenChain: "tooltip container background -> --ion-comp-tooltip-container-color-bg-positive -> --ion-comp-popover-container-color-bg -> variable for popover background (#030c1e)"
          appliesToCssProperty: "background-color"
      warning:
        light:
          resolvesTo: "#030c1e"
          tokenChain: "tooltip container background -> --ion-comp-tooltip-container-color-bg-warning -> --ion-comp-popover-container-color-bg -> variable for popover background (#030c1e)"
          appliesToCssProperty: "background-color"
      negative:
        light:
          resolvesTo: "#030c1e"
          tokenChain: "tooltip container background -> --ion-comp-tooltip-container-color-bg-negative -> --ion-comp-popover-container-color-bg -> variable for popover background (#030c1e)"
          appliesToCssProperty: "background-color"
      info:
        light:
          resolvesTo: "#030c1e"
          tokenChain: "tooltip container background -> --ion-comp-tooltip-container-color-bg-info -> --ion-comp-popover-container-color-bg -> variable for popover background (#030c1e)"
          appliesToCssProperty: "background-color"
      secondary:
        light:
          resolvesTo: "#030c1e"
          tokenChain: "tooltip container background -> --ion-comp-tooltip-container-color-bg-secondary (not defined, falls back to popover default) -> --ion-comp-popover-container-color-bg -> variable for popover background (#030c1e)"
          appliesToCssProperty: "background-color"
  - name: content
    type: string
    category: content
    required: false
    default: ""
    values: []
    designTokens: {}
  - name: showIcon
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens:
      true:
        light:
          resolvesTo: "#030c1e"
          tokenChain: "tooltip icon color -> --ion-comp-tooltip-icon-color-fg-{intent} -> --ion-cont-color-text-icon-base-bold -> --ion-cont-color-role-light-text-icon-1050 -> --ion-lit-color-palette-light-navy-1050 -> #030c1e (for neutral intent) or intent-specific color for other intents"
          appliesToCssProperty: "color"
  - name: hideCaret
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens:
      false:
        light:
          resolvesTo: "#030c1e"
          tokenChain: "tooltip caret border -> --ion-comp-tooltip-caret-color-border-{intent} -> --ion-cont-color-ui-status-{intent} (varies by intent) or --ion-cont-color-role-light-text-icon-800 for neutral"
          appliesToCssProperty: "border-color"
  - name: placement
    type: enum
    category: visual
    required: false
    default: "bottom"
    values: [auto, top, topStart, topEnd, right, rightStart, rightEnd, bottom, bottomStart, bottomEnd, left, leftStart, leftEnd, cursor]
    designTokens: {}
  - name: fallbackPlacementBehavior
    type: enum
    category: behavioral
    required: false
    default: "flip-shift"
    values: [flip, shift, flip-shift, none]
    designTokens: {}
  - name: offset
    type: "MQ<string>"
    category: visual
    required: false
    default: "0"
    values: []
    designTokens: {}
  - name: inheritParentWidth
    type: "MQ<string>"
    category: visual
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: trigger
    type: enum
    category: behavioral
    required: false
    default: "hover"
    values: [hover, press, manual]
    designTokens: {}
  - name: open
    type: boolean
    category: behavioral
    required: false
    default: false
    values: []
    designTokens: {}
  - name: autoFocus
    type: boolean
    category: behavioral
    required: false
    default: false
    values: []
    designTokens: {}
  - name: enableFocus
    type: boolean
    category: behavioral
    required: false
    default: false
    values: []
    designTokens: {}
  - name: openDelay
    type: number
    category: behavioral
    required: false
    default: 200
    values: []
    designTokens: {}
  - name: closeDelay
    type: number
    category: behavioral
    required: false
    default: 0
    values: []
    designTokens: {}
  - name: originAnchorId
    type: string
    category: accessibility
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: cursorPosition
    type: "{x: number, y: number}"
    category: behavioral
    required: false
    default: "none found"
    values: []
    designTokens: {}
events:
  - name: openChange
    payloadType: "CustomEvent<boolean>"
    firesWhen: "Whenever the tooltip visibility changes (both opening and closing)"
    detailAccess: "event.detail (boolean) - true when opening, false when closing"
    bindingSyntax: (openChange)="onTooltipVisibilityChange($event)"
  - name: onOpen
    payloadType: "CustomEvent<void>"
    firesWhen: "When the tooltip becomes visible after any openDelay has completed"
    detailAccess: "void, event.detail is undefined"
    bindingSyntax: (onOpen)="onTooltipOpen($event)"
  - name: onClose
    payloadType: "CustomEvent<void>"
    firesWhen: "When the tooltip becomes hidden after any closeDelay has completed"
    detailAccess: "void, event.detail is undefined"
    bindingSyntax: (onClose)="onTooltipClose($event)"
jointTokens:
  - combination: "intent=positive, showIcon=true"
    resolvesTo: "#2dc168"
    tokenChain: "tooltip icon color -> --ion-comp-tooltip-icon-color-fg-positive -> --ion-cont-color-ui-status-positive -> --ion-lit-color-leonardo-base-positive (#2dc168)"
    appliesToCssProperty: "color"
  - combination: "intent=negative, showIcon=true"
    resolvesTo: "#c70000"
    tokenChain: "tooltip icon color -> --ion-comp-tooltip-icon-color-fg-negative -> --ion-cont-color-ui-status-negative -> --ion-lit-color-leonardo-base-negative (#c70000)"
    appliesToCssProperty: "color"
  - combination: "intent=warning, showIcon=true"
    resolvesTo: "#fe7f2a"
    tokenChain: "tooltip icon color -> --ion-comp-tooltip-icon-color-fg-warning -> --ion-cont-color-ui-status-warning -> --ion-lit-color-leonardo-base-warning (#fe7f2a)"
    appliesToCssProperty: "color"
  - combination: "intent=info, showIcon=true"
    resolvesTo: "#007de0"
    tokenChain: "tooltip icon color -> --ion-comp-tooltip-icon-color-fg-info -> --ion-cont-color-ui-status-info -> --ion-lit-color-leonardo-base-info (#007de0)"
    appliesToCssProperty: "color"
  - combination: "intent=neutral, hideCaret=false"
    resolvesTo: "#3a4455"
    tokenChain: "tooltip caret border -> --ion-comp-tooltip-caret-color-border-neutral -> --ion-cont-color-ui-status-neutral -> --ion-cont-color-role-light-text-icon-800 -> --ion-lit-color-palette-light-navy-800 (#3a4455)"
    appliesToCssProperty: "border-color"
  - combination: "intent=positive, hideCaret=false"
    resolvesTo: "#2dc168"
    tokenChain: "tooltip caret border -> --ion-comp-tooltip-caret-color-border-positive -> --ion-cont-color-ui-status-positive -> --ion-lit-color-leonardo-base-positive (#2dc168)"
    appliesToCssProperty: "border-color"
  - combination: "intent=negative, hideCaret=false"
    resolvesTo: "#c70000"
    tokenChain: "tooltip caret border -> --ion-comp-tooltip-caret-color-border-negative -> --ion-cont-color-ui-status-negative -> --ion-lit-color-leonardo-base-negative (#c70000)"
    appliesToCssProperty: "border-color"
  - combination: "intent=warning, hideCaret=false"
    resolvesTo: "#fe7f2a"
    tokenChain: "tooltip caret border -> --ion-comp-tooltip-caret-color-border-warning -> --ion-cont-color-ui-status-warning -> --ion-lit-color-leonardo-base-warning (#fe7f2a)"
    appliesToCssProperty: "border-color"
  - combination: "intent=info, hideCaret=false"
    resolvesTo: "#007de0"
    tokenChain: "tooltip caret border -> --ion-comp-tooltip-caret-color-border-info -> --ion-cont-color-ui-status-info -> --ion-lit-color-leonardo-base-info (#007de0)"
    appliesToCssProperty: "border-color"
propInteractions:
  - When trigger="manual", the open prop controls tooltip visibility and must be used to show/hide
  - When trigger="hover", tooltip shows on mouseenter and hides on mouseleave (with optional delays)
  - When trigger="press", tooltip shows on click and hides on blur or click outside
  - When placement="cursor", cursorPosition prop can be used to manually set tooltip position
  - When placement="cursor", mouse movement on anchor element updates tooltip position with 200ms debounce
  - showIcon only works with content prop (string content), not with slotted tooltip content
  - inheritParentWidth string value of "true" (case-sensitive) enables width matching to anchor element
  - offset value affects spacing between tooltip and anchor element
  - fallbackPlacementBehavior affects how tooltip repositions when original placement doesn't fit viewport
  - openDelay only applies to hover trigger (delay before showing)
  - closeDelay applies to both hover and press triggers (delay before hiding)
  - enableFocus and autoFocus props work together for focus management in tooltip content
  - originAnchorId is used with accessibilityType popup option for ARIA relationships
  - content prop override: content passed through slot="tooltipContent" overrides the content prop value
  - For lazy loading, *ionLazyLoadContent directive can be used on tooltip content slot
  - hideCaret controls visibility of tooltip caret/arrow element (default visible)
needsReview:
  - "Dark theme-specific design tokens not found for intent-based tooltip styling - all traced tokens use light theme palette colors (--ion-lit-color-palette-light-*) and don't have corresponding dark theme (--ion-lit-color-palette-dark-*) variant definitions in provided ds_tokens.css"
  - "Design token resolved values for tooltip container background color only traced light theme - actual resolved hex value for --ion-comp-popover-container-color-bg not found in ds_tokens.css (only variable name captured)"
  - "Design token resolved values for tooltip container border radius, border width, box-shadow, padding not traced from provided token files"
  - "Intent value 'secondary' in tooltip intent type appears in interface but specific design token mapping not found (only neutral, positive, warning, negative, info tooltips have explicit token definitions)"
  - "Design token resolved values for tooltip message typography not traced to final pixel values - only CSS variable names captured (--ion-comp-tooltip-message-typography, etc.)"
  - "Design token resolved values for tooltip icon sizing not traced from token files"
  - "Design token resolved values for tooltip container spacing (gap between icon and text) not traced to final pixel values"
  - "No token mapping found for trigger behavioral prop (hover/press/manual)"
  - "No token mapping found for offset, openDelay, closeDelay behavioral props"
  - "No token mapping found for placement positioning behavior aside from fallbackPlacementBehavior"
  - "Design token resolved values for cursor placement behavior not traced"
  - "Token-based spacing values for tooltip content not traced"
  - "Tooltip caret sizing tokens not traced to final resolved values in provided token files"
  - "Interaction between showIcon prop and icon positioning/sizing not fully explored through token system"
  - "Design tokens for tooltip icon specific sizing not traced - only icon color tokens found"
  - "No explicit design token mapping for different anchor element widths when inheritParentWidth is used"
  - "Design token resolved values for tooltip container max-width not traced (default 640px mentioned in code)"
---

## Usage Notes

Boolean props on this component must always be passed with an explicit string value — e.g. `showIcon="true"` or `[showIcon]="isIconShown"` — never as bare attribute presence (e.g. `showIcon` alone, with no value). Bare attribute presence is a native HTML convention this component does NOT support; it will not be interpreted as true.

## intent

Controls the semantic meaning and color scheme of the tooltip for different content types.

**Visual cues:**
- neutral: Dark navy (#030c1e), default neutral information (default)
- positive: Green (#2dc168), success or positive status
- warning: Orange (#fe7f2a), caution or warning messages  
- negative: Red (#c70000), error or negative status
- info: Blue (#007de0), informational messages
- secondary: Fallback to default popover background styling

**When to use:**
- neutral: General tooltips, hints, or help text (default)
- positive: Success messages, confirmation states, positive feedback
- warning: Caution messages, potential issues, alerts requiring attention
- negative: Error states, destructive actions, critical feedback
- info: Additional information, explanatory notes, guidance
- secondary: For secondary or less important tooltip states

**Color behavior:**
- Intent affects tooltip container border color
- Intent affects tooltip icon color when showIcon=true
- Intent affects tooltip caret border color when hideCaret=false
- Intent affects message/icon text color for non-neutral intents
- Tooltip background uses default popover background for all intents

**Note:** For intent-specific icon and caret colors, see jointTokens section above.

## content

Controls the tooltip message content displayed as text. This prop drives the core informational content of the tooltip.

**Visual cues:**
- When set with showIcon=true, displays formatted text with intent-based icon
- When set with showIcon=false, displays plain text only
- Supports simple string content only

**When to use:**
- For simple text-based tooltips that don't require complex markup
- When you want automatic icon display based on intent (with showIcon=true)
- For basic informational tooltips with straightforward text

**Content override:**
- If content is provided through slot="tooltipContent", the slotted content will be shown instead of content prop
- The content prop is ignored when custom slotted content is present

## showIcon

Controls whether the tooltip displays an intent-based icon alongside the message content.

**Visual cues:**
- true: Shows intent-specific icon before the message content
- false: Displays message text only without icon (default)

**When to use:**
- true: When visual reinforcement of tooltip intent is helpful for quick recognition
- false: When icon is unnecessary or creates visual clutter (default)

**Visual property:** This affects the presence of an intent-specific icon element and its color is governed by the intent prop.

**Limitations:**
- Only works when content is provided through the content prop (string content)
- Does not work with custom slotted content (slot="tooltipContent")
- Icon styling is determined by the intent prop with specific colors for each intent

## hideCaret

Controls whether the tooltip displays a directional caret (arrow element) pointing toward the anchor element.

**Visual cues:**
- true: Caret arrow is hidden, tooltip appears as plain box
- false: Caret arrow displayed pointing from tooltip to anchor (default)

**When to use:**
- true: When caret creates visual clutter or isn't needed for context
- false: When directional caret helps establish visual relationship between tooltip and anchor (default)

**Visual property:** Controls visibility of the CSS caret shape with border color determined by intent.

**Note:** The caret border color is intent-specific and resolved through design tokens (see jointTokens section).

## placement

Controls where the tooltip appears relative to its anchor element. This prop drives the visual positioning of the tooltip.

**Visual cues:**
- top/topStart/topEnd: Tooltip appears above the anchor
- right/rightStart/rightEnd: Tooltip appears to the right of the anchor
- bottom/bottomStart/bottomEnd: Tooltip appears below the anchor (default)
- left/leftStart/leftEnd: Tooltip appears to the left of the anchor
- auto: System automatically chooses placement (typically defaults to bottom)
- cursor: Tooltip follows mouse cursor position

**When to use:**
- auto: When unsure which placement works best or want automatic decision
- Directional values (top, bottom, etc.): When you need specific visual positioning
- Including -start/-end modifiers: When you want horizontal alignment with anchor edges
- cursor: For tooltips that follow mouse movement position

**Behavioral notes:**
- When placement="cursor", cursorPosition prop can be used for manual positioning
- When placement="cursor", tooltip position updates on mouse movement with 200ms debounce
- Placement affects available space and may trigger fallbackPlacementBehavior

## fallbackPlacementBehavior

Controls how the tooltip repositions when the specified placement doesn't have enough available space.

**Visual cues:**
- flip: Tooltip flips to opposite side of anchor when original placement doesn't fit
- shift: Tooltip shifts along edges when close to viewport boundaries
- flip-shift: Combines both flip and shift behaviors (default)
- none: Disables automatic repositioning, keeps original placement regardless of space

**When to use:**
- flip: When wanting alternative positions on opposite side but not edge adjustments
- shift: When wanting edge adjustments but maintain general placement direction
- flip-shift: When wanting maximum adaptability to keep tooltip visible (default)
- none: When position should be fixed regardless of available space

**Behavioral property:** This is not derivable from visual design and affects positioning behavior.

## offset

Controls the spacing distance between the tooltip and its anchor element, in pixels. This prop drives the visual gap separation.

**Visual cues:**
- "0": Minimal spacing, tooltip appears close to anchor (default)
- "10", "20", etc.: Increased gap between anchor and tooltip (in pixels)
- Higher values create more separation for visual clarity

**When to use:**
- "0" or small values: Standard spacing when tooltip should appear near anchor
- "10"-"20": When tooltip needs clear visual separation from anchor
- Larger values: When tooltip needs significant spacing for visual hierarchy

**MQ design string support:**
- Can use as MQ design string: xs=0;sm=0;md=10;lg=10;xl=10;xxl=10

## inheritParentWidth

Controls whether the tooltip width matches the anchor element's width. This prop drives the tooltip's max-width constraint.

**Visual cues:**
- "false": Tooltip width determined by content or default max-width (default)
- "true": Tooltip width matches anchor element width

**When to use:**
- "false": When tooltip should size based on its own content requirements (default)
- "true": When tooltip should maintain visual alignment with trigger element width

**Design string support:**
- Use as MQ design string: xs=false;sm=false;md=true;lg=true;xl=false;xxl=false
- String value "true" (case-sensitive) enables width matching

**Behavioral notes:**
- Tooltip default max-width is 640px when inheritParentWidth="false"
- When inheritParentWidth="true", width is set to anchor element's width in pixels

## trigger

Controls what user interaction causes the tooltip to become visible.

**Visual cues:**
- hover: Tooltip appears on mouseenter, disappears on mouseleave (default)
- press: Tooltip appears on click, disappears on blur
- manual: Tooltip visibility controlled by open prop

**When to use:**
- hover: Standard tooltip behavior for information that appears during navigation
- press: For tooltips that should appear on click and stay until explicitly dismissed
- manual: For programmatic control through the open prop

**Behavioral property:** This is not derivable from visual design and affects interaction behavior.

## open

Controls the visibility state of the tooltip when trigger="manual".

**Visual cues:**
- false: Tooltip is hidden (default)
- true: Tooltip is visible

**When to use:**
- Bind this prop to control when tooltip appears based on application state
- Toggle value programmatically to show/hide tooltip from other UI elements

**Behavioral notes:**
- Only works when trigger="manual"
- Setting open=true triggers showing after openDelay elapses
- Setting open=false triggers closing after closeDelay elapses

## autoFocus

Controls whether focus automatically moves to the first interactive element within the tooltip when it opens.

**Visual cues:**
- true: Focus automatically moves into tooltip when opened
- false: Focus stays on triggering element (default)

**When to use:**
- true: Important for accessibility when tooltip contains interactive elements requiring keyboard interaction
- false: When tooltip is informational only or focus should remain on trigger for continued interaction

**Behavioral property:** This is not derivable from visual design and affects focus management behavior.

## enableFocus

Controls whether focus management is enabled for the tooltip.

**Visual cues:**
- true: Focus management enabled for keyboard navigation through tooltip content
- false: Focus management disabled (default)

**When to use:**
- true: For tooltips with interactive content requiring keyboard accessibility
- false: For purely informational tooltips where keyboard navigation isn't needed

**Behavioral property:** This is not derivable from visual design and affects accessibility behavior.

## openDelay

Controls the delay (in milliseconds) before the tooltip actually becomes visible after the trigger occurs.

**Visual cues:**
- 0 or 100: Tooltip appears immediately when triggered
- 200: 200ms delay before tooltip appears (default)
- Higher values: Tooltip appears after specified delay

**When to use:**
- 0-100ms: Standard responsive tooltip behavior
- 200ms: Default delayed appearance to prevent accidental triggering
- 500-1000ms: When gradual appearance is desired for UX experience

**Behavioral property:** This is not derivable from visual design and affects timing behavior.

## closeDelay

Controls the delay (in milliseconds) before the tooltip actually disappears after dismissing trigger occurs.

**Visual cues:**
- 0: Tooltip disappears immediately when dismissed (default)
- 100: 100ms delay before tooltip disappears
- Higher values: Tooltip disappears after specified delay

**When to use:**
- 0: Standard responsive tooltip behavior (default)
- 100-500ms: When gradual disappearance is desired (giving users time to cancel accidental dismissal)

**Behavioral property:** This is not derivable from visual design and affects timing behavior.

## originAnchorId

Specifies the ID of the anchor element for accessibility relationship establishment.

**Behavioral property:** This is not derivable from visual design and affects accessibility behavior.

**When to use:**
- Required for proper ARIA relationships when using focus-managed tooltip patterns
- Helps screen readers understand the connection between trigger and tooltip
- Used with accessibility popup option to establish proper accessibility semantics

## cursorPosition

Controls manual cursor position coordinates when placement="cursor".

**Visual cues:**
- {x: number, y: number}: Specifies pixel coordinates for tooltip position

**When to use:**
- Only applicable when placement="cursor"
- For programmatically controlling tooltip position
- Updates with 200ms debounce on mouse movement

**Behavioral notes:**
- When placement="cursor", tooltip position updates on mouse movement
- This prop provides manual override of automatic cursor following
- Used internally for automatic cursor tracking but can be set manually

## Events

### openChange

Emitted whenever the tooltip visibility changes (both when opening and closing).

**Emitted args:** CustomEvent<boolean>

**Detail access:** event.detail (boolean) - true when opening, false when closing

**When to use:**
- To track all tooltip visibility state changes in one place
- To sync application state with tooltip visibility
- To conditionally execute different logic for open vs. close actions

**How to use:**
```typescript
onTooltipVisibilityChange(event: CustomEvent<boolean>): void {
  if (event.detail) {
    console.log('Tooltip is now open');
    // Handle open-specific logic
  } else {
    console.log('Tooltip is now closed');
    // Handle close-specific logic
  }
}
```

**Binding syntax:**
```html
<ion-tooltip (openChange)="onTooltipVisibilityChange($event)" [content]="text" trigger="hover">
  <ion-button intent="primary">Tooltip Anchor</ion-button>
</ion-tooltip>
```

### onOpen

Emitted when the tooltip becomes visible after any openDelay has completed.

**Emitted args:** CustomEvent<void>

**Detail access:** void (no payload data). event.detail is undefined

**When to use:**
- To perform actions when tooltip first appears
- To animate content entry or initialize tooltip-internal state
- To track tooltip visibility for analytics or debugging

**How to use:**
```typescript
onTooltipOpen(event: CustomEvent<void>): void {
  console.log('Tooltip opened');
  // Perform initialization or start animations
  // Note: event.detail is undefined (void)
}
```

**Binding syntax:**
```html
<ion-tooltip (onOpen)="onTooltipOpen($event)" [content]="text" trigger="hover">
  <ion-button intent="primary">Tooltip Anchor</ion-button>
</ion-tooltip>
```

### onClose

Emitted when the tooltip becomes hidden after any closeDelay has completed.

**Emitted args:** CustomEvent<void>

**Detail access:** void (no payload data). event.detail is undefined

**When to use:**
- To clean up tooltip-internal state when dismissed
- To animate content exit or track analytics
- To synchronize with application state when tooltip closes

**How to use:**
```typescript
onTooltipClose(event: CustomEvent<void>): void {
  console.log('Tooltip closed');
  // Perform cleanup or analytics tracking
  // Note: event.detail is undefined (void)
}
```

**Binding syntax:**
```html
<ion-tooltip (onClose)="onTooltipClose($event)" [content]="text" trigger="hover">
  <ion-button intent="primary">Tooltip Anchor</ion-button>
</ion-tooltip>
```

**Complete event binding example:**
```typescript
export class MyComponent implements OnInit {
  text = "This is a tooltip";
  eventLogs: string = "";

  onTooltipOpen(event: CustomEvent<void>): void {
    console.log('Tooltip opened');
    this.log('Tooltip opened');
    // Note: event.detail is undefined (void)
  }

  onTooltipClose(event: CustomEvent<void>): void {
    console.log('Tooltip closed');
    this.log('Tooltip closed');
    // Note: event.detail is undefined (void)
  }

  onTooltipVisibilityChange(event: CustomEvent<boolean>): void {
    if (event.detail) {
      console.log('Tooltip is now open');
    } else {
      console.log('Tooltip is now closed');
    }
  }

  log(text: string) {
    this.eventLogs = text + '\n' + this.eventLogs;
  }
}
```

```html
<ion-tooltip [content]="text"
             trigger="hover"
             placement="bottom"
             (onOpen)="onTooltipOpen($event)"
             (onClose)="onTooltipClose($event)"
             (openChange)="onTooltipVisibilityChange($event)">
  <ion-button intent="primary">Tooltip Anchor</ion-button>
</ion-tooltip>
```

## Service API

### createTooltip

Creates and returns a tooltip instance with programmatically controlled visibility and behavior.

**Config interface:**
- tooltipElement: string | HTMLElement - The content to display inside the tooltip (text string or DOM element)
- tooltipAnchor: HTMLElement - The element that acts as the anchor/trigger for the tooltip
- options: IDsTooltipOptions | ITooltipOptions - Configuration object with the following optional properties:
  - intent: TooltipIntent - Semantic intent affecting styling: 'neutral' | 'secondary' | 'negative' | 'positive' | 'warning' | 'info'
  - content: string - Tooltip message content as text
  - showIcon: boolean - Whether to show intent-based icon
  - hideCaret: boolean - Whether to hide the tooltip caret
  - placement: TooltipPlacement - Position: 'auto' | 'top' | 'topStart' | 'topEnd' | 'right' | 'rightStart' | 'rightEnd' | 'bottom' | 'bottomStart' | 'bottomEnd' | 'left' | 'leftStart' | 'leftEnd' | 'cursor'
  - fallbackPlacementBehavior: FallbackPlacementBehavior - Repositioning: 'flip' | 'shift' | 'flip-shift' | 'none'
  - offset: string - Spacing pixels between tooltip and anchor
  - inheritParentWidth: string - Width behavior as MQ string or boolean
  - trigger: TooltipTrigger - Trigger: 'hover' | 'press' | 'manual'
  - open: boolean - Initial visibility state (manual trigger only)
  - openDelay: number - Delay before showing (milliseconds)
  - closeDelay: number - Delay before hiding (milliseconds)
  - autoFocus: boolean - Focus first interactive element on open
  - enableFocus: boolean - Enable focus management
  - originAnchorId: string - Anchor element ID for ARIA
  - cursorPosition: {x: number, y: number} - Manual positioning coordinates

**Returns:** IDsTooltip | ITooltip object with properties and methods:
- intent: TooltipIntent - Tooltip intent
- open: boolean - Tooltip visibility state
- content: string - Tooltip content text
- offset: string - Spacing offset value
- openDelay: number - Opening delay
- closeDelay: number - Closing delay
- inheritParentWidth: string - Parent width inheritance
- fallbackPlacementBehavior: FallbackPlacementBehavior - Repositioning behavior
- hideCaret: boolean - Caret visibility
- placement: TooltipPlacement - Current placement
- showIcon: boolean - Icon visibility
- trigger: TooltipTrigger - Trigger mode
- onOpen: Event<void> - Event that fires when tooltip opens (design system mode only)
- onClose: Event<void> - Event that fires when tooltip closes
- destroy(): void - Release resources and remove from DOM
- forceOpen(): void - Force tooltip to open (internal method)
- flash(duration?: number): void - Briefly show tooltip (internal method)

**Payload shape:** Service callbacks (onOpen, onClose) use bare Event<void> callbacks without CustomEvent wrapping. Service methods work directly with TypeScript objects, not DOM events - no .detail access needed.

**When to use:**
- When tooltip content or anchor is not known in advance at template time
- When creating tooltip from component logic based on runtime conditions
- When the same tooltip needs to be opened from multiple places programmatically
- For imperatively controlled tooltip patterns like context menus triggered by right-click
- When you need to manage tooltip lifecycle independently of Angular templates
- When building reusable utility functions that need to manage tooltips

**How to use:**
```typescript
import { TooltipService } from '@ionweb/sdk/toolkit';

export class MyComponent implements OnDestroy {
  private tooltipInstance: ionweb.toolkit.IDsTooltip;

  constructor(private tooltipService: TooltipService) {}

  createTooltip(event: MouseEvent) {
    // Clean up existing instance
    if (this.tooltipInstance) {
      this.tooltipInstance.destroy();
    }

    // Create new tooltip
    const options: ionweb.toolkit.IDsTooltipOptions = {
      intent: "neutral",
      offset: "0",
      hideCaret: false,
      open: true,
      openDelay: 100,
      closeDelay: 100,
      trigger: 'press'
    };

    this.tooltipInstance = this.tooltipService.createTooltip(
      "This is tooltip created using tooltip service",
      event.target as HTMLElement,
      options
    );

    // Add event handlers - no .detail needed (plain Event<void>)
    this.tooltipInstance.onOpen?.add(() => {
      console.log('Tooltip opened via service');
    });

    this.tooltipInstance.onClose?.add(() => {
      console.log('Tooltip closed via service');
      this.tooltipInstance.destroy();
      this.tooltipInstance = undefined;
    });
  }

  ngOnDestroy(): void {
    if (this.tooltipInstance) {
      this.tooltipInstance.destroy();
    }
  }
}
```

**Alternative usage with HTML element content:**
```typescript
createHtmlTooltip(event: MouseEvent) {
  const tooltipContent = document.createElement('div');
  tooltipContent.innerHTML = '<strong>Custom HTML Content</strong><p>This is a rich tooltip</p>';

  const options = {
    intent: 'positive',
    showIcon: true,
    placement: 'bottom' as const,
    hideCaret: false
  };

  this.tooltipInstance = this.tooltipService.createTooltip(
    tooltipContent,
    event.target as HTMLElement,
    options
  );
}
```

## When to use which approach

**Choose `<ion-tooltip>` (element API) when:**
- Tooltip structure and anchor are known at template definition time
- Declarative control through Angular template syntax is preferred
- Tooltip is tightly coupled to a specific trigger element
- Simple event handling through Angular @Output() bindings is sufficient
- Tooltip content is embedded directly in template markup
- Using lazy loading with *ionLazyLoadContent directive

**Choose `TooltipService.createTooltip` (service API) when:**
- Tooltip content or anchor depends on runtime values not known in advance
- You need to open the same tooltip from multiple places programmatically
- Imperative control is needed from component logic rather than template
- Creating tooltip patterns triggered by dynamic events (right-click, complex interactions)
- You need complex control over tooltip lifecycle independent of Angular change detection
- Tooltip needs to be conditionally created/destroyed based on application state
- You're building reusable utility functions that need to manage tooltips
- Performance is critical and you want to avoid creating tooltip instances at startup

**Choose `ion-title` attribute when:**
- You need simple tooltips with limited configuration
- You want to quickly add tooltips to multiple elements without wrapping them
- You can accept global configuration through config.json for all title tooltips
- You don't need complex content (only simple text)
- You want minimal template markup

**Team recommendation:** For design system mode, prefer the `TooltipService` for dynamic/scenario-based tooltips and `<ion-tooltip>` for static/template-based tooltips. The service provides better control over the tooltip lifecycle and handles complex scenarios more effectively, while the element API is cleaner for simple declarative cases in templates.

## Examples

```html
<ion-tooltip [intent]="newTooltipIntent" [showIcon]="showIcon" [content]="text" trigger="press" [hideCaret]="hideCaret" [offset]="offset" [openDelay]="openDelay" [closeDelay]="closeDelay" [inheritParentWidth]="inheritParentWidth" [fallbackPlacementBehavior]="fallbackPlacementBehavior" [placement]="placement" (openChange)="onOpenChange($event)">
  <ion-button intent="primary">Press Tooltip Anchor</ion-button>
</ion-tooltip>
```
Demonstrates content API with press trigger, showIcon, and configurable delays.

```html
<ion-tooltip [intent]="newTooltipIntent" trigger="hover" [hideCaret]="hideCaret" [offset]="offset" [openDelay]="openDelay" [closeDelay]="closeDelay" [inheritParentWidth]="inheritParentWidth" [fallbackPlacementBehavior]="fallbackPlacementBehavior" [placement]="placement" (openChange)="onOpenChange($event)">
  <ion-button intent="primary">Hover Tooltip Anchor</ion-button>
  <div slot="tooltipContent" *ionLazyLoadContent>
    Following are the features of tooltip
    <ul>
      <li>Dynamic Content</li>
      <li>Custom HTMl allowed</li>
      <li>Can be triggered using press, hover, manual</li>
    </ul>
  </div>
</ion-tooltip>
```
Demonstrates custom slotted content with lazy loading and hover trigger.

```html
<ion-tooltip [intent]="newTooltipIntent" [showIcon]="showIcon" trigger="manual" [hideCaret]="hideCaret" [offset]="offset" [openDelay]="openDelay" [closeDelay]="closeDelay" [inheritParentWidth]="inheritParentWidth" [fallbackPlacementBehavior]="fallbackPlacementBehavior" [placement]="placement" [open]="open" (openChange)="onOpenChange($event)">
  <ion-button intent="primary">Manual Tooltip Anchor</ion-button>
  <div slot="tooltipContent" *ionLazyLoadContent>
    This is custom tooltip content.
  </div>
</ion-tooltip>
```
Demonstrates manual trigger with programmatic open/close control.

```html
<ion-button ion-title="This is tooltip created using ion-title attribute" intent="primary">ion-title Tooltip Anchor</ion-button>
```
Demonstrates simple attribute-based tooltip with ion-title.

```html
<ion-tooltip [intent]="newTooltipIntent" [showIcon]="showIcon" [content]="text" trigger="hover" [hideCaret]="hideCaret" [offset]="offset" [openDelay]="openDelay" [closeDelay]="closeDelay" [inheritParentWidth]="inheritParentWidth" [fallbackPlacementBehavior]="fallbackPlacementBehavior" [placement]="placement" (openChange)="onOpenChange($event)">
  <ion-button intent="primary">Hover Tooltip Anchor</ion-button>
</ion-tooltip>
```
Demonstrates content API with hover trigger (simple text tooltip).

```html
<ion-tooltip [intent]="newTooltipIntent" [showIcon]="showIcon" [content]="text" trigger="manual" [hideCaret]="hideCaret" [offset]="offset" [openDelay]="openDelay" [closeDelay]="closeDelay" [inheritParentWidth]="inheritParentWidth" [fallbackPlacementBehavior]="fallbackPlacementBehavior" [placement]="placement" [open]="open" (openChange)="onOpenChange($event)">
  <ion-button intent="primary">Manual Tooltip Anchor</ion-button>
</ion-tooltip>
```
Demonstrates content API with manual trigger (programmatic control).