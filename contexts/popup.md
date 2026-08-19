---
realComponent: ion-popover
description: A transient overlay that displays arbitrary content anchored to an HTML element with automatic positioning and re-positioning behavior
themes: [modern-light-ds, modern-dark-ds]
apiTypes: ["element", "service"]
serviceApi:
  serviceName: PopupService
  importPath: "./popup/popupService"
  methods:
    - name: createPopUpWithElement
      signature: "createPopUpWithElement<T extends IPopup | IPopover>(contentElement: HTMLElement | string | IonElement, anchor: HTMLElement, options?: IPopupOptions | IPopoverOptions): T"
      configInterface:
        - field: size
          type: "string"
          required: false
          description: "Specify the size of the popover: 'sm', 'md', 'lg'"
        - field: placement
          type: "string"
          required: false
          description: "Specify the placement relative to the trigger: 'auto', 'top', 'right', 'bottom', 'left', 'top-start', 'top-end', 'right-start', 'right-end', 'bottom-start', 'bottom-end', 'left-start', 'left-end'"
        - field: triggerType
          type: "string[]"
          required: false
          description: "Array of trigger types: ['hover', 'click']"
        - field: showCaret
          type: "boolean"
          required: false
          description: "Show or hide the popover caret (arrow element)"
        - field: removePadding
          type: "boolean"
          required: false
          description: "If true, the popup padding will be removed"
        - field: offset
          type: "string"
          required: false
          description: "Offset space in pixels between popover and anchor element"
        - field: open
          type: "boolean"
          required: false
          description: "Whether the popover is currently open"
        - field: returnFocus
          type: "boolean"
          required: false
          description: "Whether focus returns to the anchor element on closing the popover"
        - field: autoFocus
          type: "boolean"
          required: false
          description: "Whether focus will shift to the first interactive element within the popover"
        - field: accessibilityType
          type: "string"
          required: false
          description: "How screen-readers should interpret the popover: 'dialog', 'menu', 'tooltip'"
        - field: openDelay
          type: "number"
          required: false
          description: "Delay in milliseconds before the popover is displayed"
        - field: closeDelay
          type: "number"
          required: false
          description: "Delay in milliseconds before the popover is hidden"
        - field: zindex
          type: "number | 'auto'"
          required: false
          description: "Whether z-index should be managed automatically or have a fixed value"
        - field: onClose
          type: "() => void"
          required: false
          description: "Callback function when popup is closed"
        - field: onOpen
          type: "() => void"
          required: false
          description: "Callback function when popup is shown"
        - field: persistOnBlur
          type: "boolean"
          required: false
          description: "Automatically close the popup when clicking outside of it"
        - field: inheritParentWidth
          type: "string"
          required: false
          description: "Make popover have width to match with anchor element's width"
        - field: fallbackPlacementBehavior
          type: "string"
          required: false
          description: "How popover repositions when original placement doesn't have enough space: 'flip', 'shift', 'flip-shift', 'none'"
        - field: appendToBody
          type: "boolean"
          required: false
          description: "Whether to append popup to body or anchor element"
        - field: enableFocus
          type: "boolean"
          required: false
          description: "Whether focus management is enabled"
        - field: originAnchorId
          type: "string"
          required: false
          description: "ID of the original anchor element for accessibility"
        - field: ionAriaProperties
          type: "IAriaProperties"
          required: false
          description: "Aria properties to set on the popup container"
        - field: manualPosition
          type: "{x: number, y: number}"
          required: false
          description: "Manual x,y coordinates for popover position"
        - field: manualPlacement
          type: "ManualPlacement"
          required: false
          description: "Manual placement type for popover"
      returns: "IPopup | IPopover object with properties and methods including show(), hide(), destroy(), onClose event, onOpen event, and configurable properties like placement, size, showCaret, persistOnBlur, etc."
props:
  - name: placement
    type: "MQ<string>"
    category: visual
    required: false
    default: "bottom"
    values: [auto, top, right, bottom, left, top-start, top-end, right-start, right-end, bottom-start, bottom-end, left-start, left-end, manual]
    designTokens: {}
  - name: size
    type: "MQ<string>"
    category: visual
    required: false
    default: "md"
    values: [sm, md, lg]
    designTokens:
      sm:
        light:
          resolvesTo: "variable --ion-comp-popover-container-spacing-padding-block-sm"
          tokenChain: "component padding -> --ion-comp-popover-container-spacing-padding-block-sm"
          appliesToCssProperty: "padding-block"
        dark:
          resolvesTo: "variable --ion-comp-popover-container-spacing-padding-block-sm"
          tokenChain: "component padding -> --ion-comp-popover-container-spacing-padding-block-sm"
          appliesToCssProperty: "padding-block"
      md:
        light:
          resolvesTo: "variable --ion-comp-popover-container-spacing-padding-block-md"
          tokenChain: "component padding -> --ion-comp-popover-container-spacing-padding-block-md"
          appliesToCssProperty: "padding-block"
        dark:
          resolvesTo: "variable --ion-comp-popover-container-spacing-padding-block-md"
          tokenChain: "component padding -> --ion-comp-popover-container-spacing-padding-block-md"
          appliesToCssProperty: "padding-block"
      lg:
        light:
          resolvesTo: "variable --ion-comp-popover-container-spacing-padding-block-lg"
          tokenChain: "component padding -> --ion-comp-popover-container-spacing-padding-block-lg"
          appliesToCssProperty: "padding-block"
        dark:
          resolvesTo: "variable --ion-comp-popover-container-spacing-padding-block-lg"
          tokenChain: "component padding -> --ion-comp-popover-container-spacing-padding-block-lg"
          appliesToCssProperty: "padding-block"
  - name: showCaret
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
  - name: offset
    type: "MQ<string>"
    category: visual
    required: false
    default: "none found"
    values: []
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
  - name: returnFocus
    type: boolean
    category: behavioral
    required: false
    default: false
    values: []
    designTokens: {}
  - name: accessibilityType
    type: "string"
    category: accessibility
    required: false
    default: "dialog"
    values: [dialog, menu, tooltip]
    designTokens: {}
  - name: openDelay
    type: number
    category: behavioral
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: closeDelay
    type: number
    category: behavioral
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: zIndex
    type: "number | 'auto'"
    category: behavioral
    required: false
    default: "auto"
    values: []
    designTokens: {}
  - name: persistOnBlur
    type: boolean
    category: behavioral
    required: false
    default: false
    values: []
    designTokens: {}
  - name: inheritParentWidth
    type: "MQ<string>"
    category: visual
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: fallbackPlacementBehavior
    type: "MQ<string>"
    category: behavioral
    required: false
    default: "flip-shift"
    values: [flip, shift, flip-shift, none]
    designTokens: {}
  - name: originAnchorId
    type: "string"
    category: accessibility
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: ionAriaProperties
    type: "IAriaProperties"
    category: accessibility
    required: false
    default: "{ariaLabel:'Popover'}"
    values: []
    designTokens: {}
  - name: removePadding
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
events:
  - name: onOpen
    payloadType: "CustomEvent<void>"
    firesWhen: "When the popover is shown after any openDelay has completed"
    detailAccess: "void, event.detail is undefined"
    bindingSyntax: (onOpen)="onPopoverOpen($event)"
  - name: onClose
    payloadType: "CustomEvent<void>"
    firesWhen: "When the popover is closed after any closeDelay has completed"
    detailAccess: "void, event.detail is undefined"
    bindingSyntax: (onClose)="onPopoverClose($event)"
  - name: openChange
    payloadType: "CustomEvent<boolean>"
    firesWhen: "Whenever the popover visibility changes (both opening and closing)"
    detailAccess: "event.detail (boolean) - true when opening, false when closing"
    bindingSyntax: (openChange)="onPopoverVisibilityChange($event)"
jointTokens:
  - combination: "showCaret=true, size=lg"
    resolvesTo: "variable --ion-comp-popover-caret-container-sizing-lg"
    tokenChain: "component caret sizing -> --ion-comp-popover-caret-container-sizing-lg"
    appliesToCssProperty: "width, height"
  - combination: "showCaret=true, size=md"
    resolvesTo: "variable --ion-comp-popover-caret-container-sizing-md"
    tokenChain: "component caret sizing -> --ion-comp-popover-caret-container-sizing-md"
    appliesToCssProperty: "width, height"
  - combination: "showCaret=true, size=sm"
    resolvesTo: "variable --ion-comp-popover-caret-container-sizing-sm"
    tokenChain: "component caret sizing -> --ion-comp-popover-caret-container-sizing-sm"
    appliesToCssProperty: "width, height"
propInteractions:
  - offset value is increased by 8px when showCaret=true and size=lg, and by 5px when showCaret=true and size=sm/md (handled by PopupDs.getOffset method)
  - inheritParentWidth string value of "true" enables matchAnchorWidth behavior in the popup, "false" or other values disable this matching behavior (parsed via MQ design string)
  - placement with value "auto" results in "bottom" placement being used instead of actual auto-placement (fallback in PopupDs.getPlacement)
  - persistOnBlur value dynamically sets automaticallyClose property to the opposite: persistOnBlur=true means automaticallyClose=false, persistOnBlur=false means automaticallyClose=true
  - showCaret property is aliased as showAnchorPointArrow in legacy code for backward compatibility
  - removePadding only applies to design system popover mode and is ignored in legacy mode
  - fallbackPlacementBehavior="none" causes isFixedAnchorPoint to return true, enabling fixed positioning (PopupDs.isFixedAnchorPoint)
  - fallbackPlacementBehavior="flip" disables shift behavior, "shift" disables flip behavior, "flip-shift" enables both (PopupDs.isShiftBehaviorAllowed, PopupDs.isFlipBehaviorAllowed)
needsReview:
  - "Prop default values for offset, openDelay, closeDelay, originAnchorId show as 'none found' - actual implementation defaults used but not explicitly declared in interface defaults"
  - "Design token resolved values for size-based padding (sm/md/lg) not traced to final pixel values - only CSS variable names captured from popover-ds.css"
  - "Design token resolved values for container background color, border color, border radius, border width, box-shadow not traced (variables: --ion-comp-popover-container-color-bg, --ion-comp-popover-container-color-border, --ion-comp-popover-container-border-radius-md, etc.)"
  - "Design token resolved values for caret background color, border color, border width not traced (variables: --ion-comp-popover-caret-container-color-bg, etc.)"
  - "Accessibility type values (dialog, menu, tooltip) have no token mapping - service implementation uses these strings directly without design token support"
  - "No dark theme-specific design tokens traced - all captured tokens are variables only, actual resolved values for light/dark themes not found in ds_tokens.css (only leonardo base colors present, not component-level popover tokens)"
  - "No design token mapping for fallbackPlacementBehavior values - this prop affects behavior but not visual styling resolved from tokens"
  - "MQ design string parsing results for responsive sizing and spacing not verifiable without runtime screen size context"
  - "offset prop combined with showCaret and size has complex offset calculation (adding 5-8px) but resolved token values for these cases not traced"
  - "inheritParentWidth and fallbackPlacementBehavior support MQ design strings but token resolution not verified"
  - "Popover container box-shadow token (--ion-comp-popover-container-shadow) not traced to resolved value"
  - "Popover container min-width and max-width tokens not traced or documented"
  - "Padding-inline tokens for each size variant (sm/md/lg) not traced - only padding-block tokens captured"
  - "Border width tokens for each size variant (sm/md/lg) not traced to final pixel values - only variables captured"
  - "Border radius tokens for each size variant (sm/md/lg) not traced to final pixel values - only variables captured"
  - "Caret border width tokens for each size variant (sm/md/lg) not traced to final values - only variables captured"
  - "Caret container sizing tokens (width/height) only captured as variables, actual resolved pixel values not traced"
  - "Interaction between removePadding prop and container padding tokens not fully explored - when removePadding=true, padding tokens may not apply"
  - "No explicit design token mapping for alertDialogType if present in the API - accessibilityType prop values have visual implications but no token tracing found"
  - "No token mapping for focus ring or focus state styling on popover"
  - "No token mapping for hover/overlay/interaction states that might exist but not documented in provided sources"
  - "No token mapping for z-index management - zIndex prop uses auto or fixed value but z-index variable values not traced"
  - "Manual position coordinates (manualPosition x,y) have no design token mapping - these are absolute pixel values only"
  - "Auto placement (placement=auto) behavior lacks design token documentation - fallback to bottom but this logic not tied to visual tokens"
---

## Usage Notes

Boolean props on this component must always be passed with an explicit string value — e.g. `disabled="true"` or `[disabled]="isDisabled"` — never as bare attribute presence (e.g. `disabled` alone, with no value). Bare attribute presence is a native HTML convention this component does NOT support; it will not be interpreted as true.

## placement

Controls where the popover appears relative to its anchor element. This prop drives the visual positioning of the popover and determines which side of the anchor the popover content will display on.

**Visual cues:**
- top/top-start/top-end: Popover appears above the anchor
- right/right-start/right-end: Popover appears to the right of the anchor  
- bottom/bottom-start/bottom-end: Popover appears below the anchor (default)
- left/left-start/left-end: Popover appears to the left of the anchor
- auto: System automatically chooses placement with most available space (frequently defaults to bottom in practice)
- manual: Manual positioning via manualPosition coordinates

**When to use:**
- "auto" when unsure which placement works best for specific UI context or want automatic decision
- Directional values (top, bottom, etc.) when you need specific visual positioning relative to anchor
- including -start/-end modifiers when you want horizontal alignment with anchor edges
- manual only when needing absolute positioning control via manualPosition coordinates

**Size variants:**
- Placement affects available space for popover content in vertical/horizontal directions
- Choose placement directionally based on available screen space around anchor

**Note:** For offsets that depend on this prop's combination with showCaret and size, see jointTokens section.

## size

Controls the overall dimensions and internal spacing of the popover container. This prop drives the padding/radius/sizing tokens applied to the popover.

**Visual cues:**
- sm: Compact popover with smaller padding and caret, suitable for compact UI or minimal content
- md: Medium-sized popover (default), standard padding and dimensions
- lg: Large popover with generous padding and larger caret, suitable for extensive content

**When to use:**
- sm: Compact tooltips, short hints, or minimal content popover
- md: Standard dropdown menus, confirmation dialogs, or typical popover content (default)
- lg: Rich content popover, detailed forms, or comprehensive information display

**Design token dependencies:**
- Size affects padding-block and padding-inline (see designTokens section)
- Size affects caret sizing when showCaret=true (see jointTokens section)
- Size affects border radius and border width values (variables not fully traced)

## showCaret

Controls whether the popover displays a directional caret (arrow element) pointing toward the anchor element.

**Visual cues:**
- true: Caret arrow displayed pointing from popover to its anchor (triangular CSS shape)
- false: No caret displayed, popover appears as plain box (default)

**When to use:**
- true: When visual connection between popover and anchor helps user understand relationship
- false: When carets are unnecessary for the UI pattern or create visual clutter

**Interaction with offset:**
- When showCaret=true, the offset prop has additional spacing added (5px for sm/md, 8px for lg) to account for caret dimensions

**Interaction with size:**
- Caret size scales with popover size (see jointTokens section for combined effects)

## offset

Controls the spacing distance between the popover and its anchor element, in pixels.

**Visual cues:**
- 0 or omitted: Minimal spacing, popover appears close to anchor
- 10, 20, etc.: Increased gap between anchor andpopover (in pixels)
- Higher values create more separation for visual clarity

**When to use:**
- Small offsets (0-10): Standard spacing when popover should appear near anchor
- Medium offsets (10-20): When popover needs clear visual separation from anchor
- Large offsets (20+): Whenpopover needs significant spacing for visual hierarchy

**Complex behavior:**
- Use as MQ design string: xs=0;sm=0;md=10;lg=10;xl=10;xxl=10
- When showCaret=true, actual offset is increased by 5px (sm/md) or 8px (lg) to account for caret
- Actual offset calculation: resolved value + caretSizeOffset if caret enabled

## open

Controls the visibility state of the popover.

**Visual cues:**
- false: Popover is hidden (default)
- true: Popover is visible and displayed

**When to use:**
- Bind this prop to control when popover appears based on user interaction or application state
- Toggle value programmatically to show/hide popover from other UI elements

**Behavioral notes:**
- Setting open=true triggers showing after openDelay elapses
- Setting open=false triggers closing after closeDelay elapses
- openChange event fires on visibility changes for synchronization

## autoFocus

Controls whether focus automatically moves to the first interactive element within the popover when it opens.

**Visual cues:**
- true: Focus automatically moves into popover when opened
- false: Focus stays on triggering element (default)

**When to use:**
- true: Important for accessibility when popover contains interactive elements (forms, menus) requiring keyboard interaction
- false: When popover is informational only or focus should remain on trigger for continued interaction

**Behavioral property:** This is not derivable from visual design and affects focus management behavior.

## returnFocus

Controls whether focus returns to the anchor element when the popover closes.

**Visual cues:**
- true: Focus returns to the element that triggered the popover
- false: Focus behavior follows default browser behavior (default)

**When to use:**
- true: For accessible popover patterns where users expect to return to their place after dismissal
- false: When focus management is handled externally or following standard keyboard navigation patterns

**Behavioral property:** This is not derivable from visual design and affects focus management behavior.

## accessibilityType

Controls how assistive technologies interpret the popover's semantic role and behavior.

**Visual cues:**
- dialog: Popover treated as dialog by screen readers (default)
- menu: Popover treated as menu containing interactive options
- tooltip: Popover treated as tooltip providing supplementary information

**When to use:**
- dialog: For confirmation dialogs, forms, or complex interactive content
- menu: For dropdown menus containing selectable options or actions
- tooltip: For hints, help text, or information-only popover

**Accessibility behavior:**
- Affects ARIA role attributes and announcement behavior
- Works with originAnchorId to establish relationship between anchor and popover
- Each type has different keyboard navigation patterns expected by assistive technologies

## openDelay

Controls the delay (in milliseconds) before the popover actually becomes visible after open is set to true.

**Visual cues:**
- 0: Popover appears immediately when open=true (default)
- 500, 1000, etc.: Popover appears after specified delay

**When to use:**
- 0 or low values: Standard responsive popover behavior
- 500-1000ms: When gradual appearance is desired for UX (tooltips, hover menus)
- Longer delays: Rare, but can prevent accidental triggering

**Behavioral property:** This is not derivable from visual design and affects timing behavior.

## closeDelay

Controls the delay (in milliseconds) before the popover actually disappears after open is set to false.

**Visual cues:**
- 0: Popover disappears immediately when open=false (default)
- 500, 1000, etc.: Popover disappears after specified delay

**When to use:**
- 0 or low values: Standard responsive popover behavior
- 500-1000ms: When gradual disappearance is desired (giving users time to cancel accidental dismissal)
- Longer delays: Rare, but can prevent accidental closing

**Behavioral property:** This is not derivable from visual design and affects timing behavior.

## zIndex

Controls the stacking order of the popover relative to other elements on the page.

**Visual cues:**
- auto: Automatically manages z-index to appear on top (default)
- 1500, 2000, etc.: Fixed z-index value for specific stacking needs

**When to use:**
- auto: Standard case where popover should always appear above other content (default)
- Fixed values: When popover needs to interact with specific layering in complex UI or multiple overlays

**Behavioral property:** This is not derivable from visual design and affects stacking behavior.

## persistOnBlur

Controls whether the popover automatically closes when focus moves outside of it.

**Visual cues:**
- false: Popover automatically closes when user clicks outside or focus moves away (default)
- true: Popover remains open even when focus/click moves outside

**When to use:**
- false: Standard dropdown/tooltip behavior where dismissal happens automatically
- true: When popover should persist for explicit user dismissal (dialogs, some menus)

**Behavioral property:** This is not derivable from visual design and affects dismissal behavior.

**Note:** This property controls the opposite of automaticallyClose - persistOnBlur=true means automaticallyClose=false.

## inheritParentWidth

Controls whether the popover width matches the anchor element's width.

**Visual cues:**
- false: Popover width determined by content or size prop (default)
- true: Popover width matches anchor element width

**When to use:**
- false: When popover should size based on its own content requirements
- true: When popover should maintain visual alignment with trigger element width

**Design string support:**
- Use as MQ design string: xs=false;sm=false;md=true;lg=true;xl=false;xxl=false
- String value "true" (case-sensitive) enables matching, "false" or other values disable

## fallbackPlacementBehavior

Controls how the popover repositions when the specified placement doesn't have enough available space.

**Visual cues:**
- flip: Popover flips to opposite side of search when original placement doesn't fit
- shift: Popover shifts along edges when close to viewport boundaries
- flip-shift: Combines both flip and shift behaviors (default)
- none: Disables automatic repositioning

**When to use:**
- flip: When wanting alternative positions on opposite side but not edge adjustments
- shift: When wanting edge adjustments but maintain general placement direction
- flip-shift: When wanting maximum adaptability to keep popover visible (default)
- none: When position should be fixed regardless of available space

**Behavioral effects:**
- "none" causes isFixedAnchorPoint=true, enabling fixed positioning
- "flip" disables shift behavior but allows flip repositioning
- "shift" allows edge adjustment but flips to opposite side
- Affects fallback behavior when original placement unavailable

## originAnchorId

Specifies the ID of the anchor element for accessibility relationship establishment.

**Behavioral property:** This is not derivable from visual design and affects accessibility behavior.

**When to use:**
- Required for proper ARIA relationships when using focus-managed popover patterns
- Helps screen readers understand the connection between trigger and popover
- Used with accessibilityType to establish proper accessibility semantics

## ionAriaProperties

Provides customizable ARIA properties to set on the popover container for enhanced accessibility.

**Behavioral property:** This is not derivable from visual design and affects accessibility behavior.

**When to use:**
- When standard ARIA properties don't cover specific use case requirements
- Override default ARIA behavior when needed for custom interaction patterns
- Enhance screen reader announcements with custom properties

**Default behavior:**
- Uses ariaLabel="Popover" as default ARIA label
- Can override with any properties from IAriaProperties interface

## removePadding

Controls whether the popover's internal padding is removed.

**Visual cues:**
- false: Standard padding applied based on size prop (default)
- true: Padding removed from popover container

**When to use:**
- false: Standard case where spacing around content is desired (default)
- true: When custom spacing needed externally when popover needs to appear with minimal interior spacing
- Some borderline/edge cases where full-width content needs to touch container edges

**Note:** Only applies to design system popover mode, not legacy mode.

## Events

### onOpen

Emitted when the popover becomes visible after any openDelay has elapsed.

**Emitted args:** CustomEvent<void>

**Detail access:** void (no payload data). event.detail is undefined

**When to use:**
- To perform actions when popover first appears
- To animate content entry or initialize popover-internal state
- To track popover visibility for analytics or debugging

**How to use:**
```typescript
onPopoverOpen(event: CustomEvent<void>): void {
  console.log('Popover opened');
  // Perform initialization or start animations
  // Note: event.detail is undefined (void)
}
```

**Binding syntax:**
```html
<ion-popover (onOpen)="onPopoverOpen($event)" [open]="open">
  <div slot="anchor">Trigger</div>
  <div slot="popover">Content</div>
</ion-popover>
```

### onClose

Emitted when the popover becomes hidden after any closeDelay has elapsed.

**Emitted args:** CustomEvent<void>

**Detail access:** void (no payload data). event.detail is undefined

**When to use:**
- To clean up popover-internal state when dismissed
- To animate content exit or track analytics
- To synchronize with application state when popover closes

**How to use:**
```typescript
onPopoverClose(event: CustomEvent<void>): void {
  console.log('Popover closed');
  // Perform cleanup or analytics tracking
  // Note: event.detail is undefined (void)
}
```

**Binding syntax:**
```html
<ion-popover (onClose)="onPopoverClose($event)" [open]="open">
  <div slot="anchor">Trigger</div>
  <div slot="popover">Content</div>
</ion-popover>
```

### openChange

Emitted whenever the popover visibility changes (both when opening and closing).

**Emitted args:** CustomEvent<{ isOpen: boolean }>

**Detail access:** event.detail.isOpen (boolean) - true when opening, false when closing

**When to use:**
- To track all popover visibility state changes in one place
- To sync application state with popover visibility
- To conditionally execute different logic for open vs. close actions

**How to use:**
```typescript
onPopoverVisibilityChange(event: CustomEvent<{ isOpen: boolean }>): void {
  if (event.detail.isOpen) {
    console.log('Popover is now open');
    // Handle open-specific logic
  } else {
    console.log('Popover is now closed');
    // Handle close-specific logic
  }
}
```

**Binding syntax:**
```html
<ion-popover (openChange)="onPopoverVisibilityChange($event)" [open]="open">
  <div slot="anchor">Trigger</div>
  <div slot="popover">Content</div>
</ion-popover>
```

**Complete event binding example:**
```typescript
export class MyComponent {
  open = false;

  onPopoverOpen(event: CustomEvent<void>): void {
    console.log('Popover opened');
    // Initialize popover content or start animations
  }

  onPopoverClose(event: CustomEvent<void>): void {
    console.log('Popover closed');
    // Clean up state or track closure
  }

  onPopoverVisibilityChange(event: CustomEvent<{ isOpen: boolean }>): void {
    this.open = event.detail.isOpen;
    // Sync local state with visibility
  }
}
```

```html
<ion-popover [open]="open"
                    (onOpen)="onPopoverOpen($event)"
                    (onClose)="onPopoverClose($event)"
                    (openChange)="onPopoverVisibilityChange($event)">
  <div slot="anchor" (click)="open = !open">Toggle Popover</div>
  <div slot="popover">Popover Content</div>
</ion-popover>
```

## Service API

### createPopUpWithElement

Creates and returns a popover instance with programmatically controlled visibility and behavior.

**Config interface:**
- contentElement: HTMLElement | string | IonElement - The content to display inside the popover
- anchor: HTMLElement - The element that acts as the anchor/trigger for the popover
- options: IPopupOptions | IPopoverOptions - Configuration object with the following optional properties:
  - size: string - Popover size: 'sm', 'md', 'lg'
  - placement: string - Position relative to trigger: 'auto', 'top', 'right', 'bottom', 'left', etc.
  - showCaret: boolean - Display caret arrow
  - removePadding: boolean - Remove padding from popover
  - offset: string - Spacing between popover and anchor (pixels)
  - open: boolean - Initial visibility state
  - returnFocus: boolean - Return focus to anchor on close
  - autoFocus: boolean - Focus first interactive element on open
  - accessibilityType: string - ARIA behavior: 'dialog', 'menu', 'tooltip'
  - openDelay: number - Delay before showing (milliseconds)
  - closeDelay: number - Delay before hiding (milliseconds)
  - zindex: number | 'auto' - Stacking order control
  - onClose: () => void - Callback when popover closes
  - onOpen: () => void - Callback when popover opens
  - persistOnBlur: boolean - Keep open when focus moves outside
  - inheritParentWidth: string - Match anchor width: 'true' or 'false'
  - fallbackPlacementBehavior: string - Reposition behavior: 'flip', 'shift', 'flip-shift', 'none'
  - appendToBody: boolean - Append to body or anchor element
  - enableFocus: boolean - Enable focus management
  - originAnchorId: string - Anchor element ID for ARIA
  - ionAriaProperties: IAriaProperties - Custom ARIA properties
  - manualPosition: {x: number, y: number} - Manual positioning coordinates
  - manualPlacement: ManualPlacement - Manual placement type

**Returns:** IPopup | IPopover object with methods and properties:
- show(): void - Make the popover visible
- hide(): void - Make the popover disappear
- destroy(): void - Release resources and remove from DOM
- onClose: Event<void> - Event that fires when popover closes
- onOpen: Event<void> - Event that fires when popover opens (design system mode only)
- placement: string - Get/set popover placement
- fallbackPlacementBehavior: string - Get/set fallback placement behavior
- showCaret: boolean - Get/set caret visibility
- removePadding: boolean - Get/set padding removal
- persistOnBlur: boolean - Get/set blur persistence
- autoFocus: boolean - Get/set auto-focus behavior
- returnFocus: boolean - Get/set focus return behavior
- openDelay: number - Get/set open delay
- closeDelay: number - Get/set close delay
- size: string - Get/set popover size
- offset: string - Get/set offset spacing
- inheritParentWidth: string - Get/set parent width inheritance
- accessibilityType: string - Get/set accessibility type
- enableFocus: boolean - Get/set focus management

**Payload shape:** Service callbacks (onClose, onOpen) receive plain void callbacks without CustomEvent wrapping. Service methods work directly with TypeScript objects, not DOM events.

**When to use:**
- When popover content or anchor is not known in advance at template time
- When creating popover from component logic based on runtime conditions
- When the same popover needs to be opened from multiple places programmatically
- For imperatively controlled overlay patterns like context menus triggered by right-click
- When you need to manage popover lifecycle independently of Angular templates

**How to use:**
```typescript
import { PopupService } from '@ionweb/sdk/toolkit';

export class MyComponent {
  constructor(private popupService: PopupService) {}

  openMenu(event: MouseEvent) {
    const anchor = event.target as HTMLElement;
    const menuContent = document.createElement('div');
    menuContent.innerHTML = '<div class="menu-item">Option 1</div><div class="menu-item">Option 2</div>';

    const popover = this.popupService.createPopUpWithElement(
      menuContent,
      anchor,
      {
        size: 'md',
        placement: 'bottom',
        showCaret: true,
        autoOpen: true,
        persistOnBlur: false,
        accessibilityType: 'menu',
        onOpen: () => console.log('Menu opened'),
        onClose: () => console.log('Menu closed')
      }
    );

    // Service doesn't wrap callbacks in CustomEvent
    // The callback receives plain parameters, not event.detail
    popover.onClose.add(() => {
      console.log('Cleanup when popover closes');
      popover.destroy();
    });

    popover.show();
  }
}
```

**Alternative usage with template:**
```typescript
import { Component, Input } from '@angular/core';
import { PopupService } from '@ionweb/sdk/toolkit';

@Component({
  selector: 'app-my-component',
  template: `
    <button #triggerButton (click)="openMenu()">Open Menu</button>
  `
})
export class MyComponent {
  @ViewChild('triggerButton') triggerButton: ElementRef;

  constructor(private popupService: PopupService) {}

  openMenu() {
    // Create popover with angular component content
    const popover = this.popupService.createPopUpWithElement(
      () => document.createElement('app-menu-content'),
      this.triggerButton.nativeElement,
      {
        placement: 'bottom',
        size: 'md',
        showCaret: true
      }
    );

    popover.show();
  }
}
```

## When to use which approach

**Choose `<ion-popover>` (element API) when:**
- Popover structure and anchor are known at template definition time
- Declarative control through Angular template syntax is preferred
- Popover is tightly coupled to a specific trigger element
- Simple event handling through Angular @Output() bindings is sufficient
- Popover content is embedded directly in template markup

**Choose `PopupService.createPopUpWithElement` (service API) when:**
- Popover content or anchor depends on runtime values not known in advance
- You need to open the same popover from multiple places programmatically
- Imperative control is needed from component logic rather than template
- Creating tooltip/context menu patterns triggered by right-click or other events
- You need complex control over popover lifecycle independent of Angular change detection
- Popover needs to be conditionally created/destroyed based on application state
- You're building reusable utility functions that need to manage overlays

**Team recommendation:** The applications should prefer the `PopupService` over the declarative component (ion-popover) as that approach is better for performance reasons as the component is only created at the call to service and not at startup when component is rendered. The service provides better control over the overlay lifecycle and handles complex scenarios more effectively.

## Examples

```html
<ion-popover
    [placement]="'auto'"
    [autoFocus]="true"
    [returnFocus]="true"
    [showCaret]="true"
    [offset]="20"
    [open]="open"
    [openDelay]="500"
    [closeDelay]="300"
    (openChange)="onPopoverVisibilityChange($event)"
    [originAnchorId]="originAnchorElementId">
    <div slot="anchor">This is the Anchor</div>
    <div slot="popover">Hi, I'm Popover</div>
</ion-popover>
```
Demonstrates full element API with open/close delays, auto focus management, caret display, and 20px offset.

```html
<ion-popover
    [size]="sm"
    [placement]="bottom"
    [showCaret]="true"
    [persistOnBlur]="true"
    [open]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates small popover size variant with caret, persistence on blur, and pre-opened state.

```html
<ion-popover
    [size]="md"
    [placement]="bottom"
    [showCaret]="true"
    [persistOnBlur]="true"
    [open]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates medium popover size (default) with caret, persistence on blur, and pre-opened state.

```html
<ion-popover
    [size]="lg"
    [placement]="bottom"
    [showCaret]="true"
    [persistOnBlur]="true"
    [open]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates large popover size with caret, persistence on blur, and pre-opened state.

```html
<ion-popover
    [placement]="bottom"
    [showCaret]="false"
    [persistOnBlur]="true"
    [open]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates default medium size popover without caret arrow, showing persistence on blur behavior.

```html
<ion-popover
    [placement]="bottom"
    [showCaret]="false"
    [open]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with caret explicitly hidden and open state active.

```html
<ion-popover
    [placement]="bottom"
    [showCaret]="true"
    [open]="false">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with caret visible but initially closed (ready to be opened by triggering element).

```html
<ion-popover
    [placement]="bottom"
    [showCaret]="true"
    [persistOnBlur]="false"
    [open]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with persistence on blur disabled (closes when focus moves outside).

```html
<ion-popover
    [placement]="bottom"
    [showCaret]="true"
    [persistOnBlur]="true"
    [open]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with persistence on blur enabled (stays open when focus moves outside).

```html
<ion-popover
    [offset]="0"
    [open]="true"
    [placement]="bottom"
    [showCaret]="true"
    [persistOnBlur]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates zero offset between popover and anchor.

```html
<ion-popover
    [offset]="10"
    [open]="true"
    [placement]="bottom"
    [showCaret]="true"
    [persistOnBlur]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates offset of 10 pixels between popover and anchor.

```html
<ion-popover
    [offset]="20"
    [open]="true"
    [placement]="bottom"
    [showCaret]="true"
    [persistOnBlur]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates offset of 20 pixels between popover and anchor.

```html
<ion-popover
    [inheritParentWidth]="false"
    [open]="true"
    [placement]="bottom"
    [persistOnBlur]="true">
    <div class="popover-anchor">Popover Anchor</div>
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with default width (not matching anchor width).

```html
<ion-popover
    [inheritParentWidth]="true"
    [open]="true"
    [placement]="bottom"
    [persistOnBlur]="true">
    <div class="popover-anchor">Popover Anchor</div>
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with width matching anchor element width.

```html
<ion-popover
    [openDelay]="0"
    [open]="true"
    [placement]="bottom"
    [persistOnBlur]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with no opening delay (appears immediately).

```html
<ion-popover
    [openDelay]="500"
    [open]="true"
    [placement]="bottom"
    [persistOnBlur]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with 500ms opening delay.

```html
<ion-popover
    [openDelay]="1000"
    [open]="true"
    [placement]="bottom"
    [persistOnBlur]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with 1000ms opening delay.

```html
<ion-popover
    [closeDelay]="0"
    [open]="true"
    [placement]="bottom">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with no closing delay (disappears immediately when closed).

```html
<ion-popover
    [closeDelay]="500"
    [open]="true"
    [placement]="bottom">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with 500ms closing delay.

```html
<ion-popover
    [closeDelay]="1000"
    [open]="true"
    [placement]="bottom">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with 1000ms closing delay.

```html
<ion-popover
    [zIndex]="auto"
    [open]="true"
    [placement]="bottom"
    [showCaret]="true"
    [persistOnBlur]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with automatic z-index management.

```html
<ion-popover
    [zIndex]="1500"
    [open]="true"
    [placement]="bottom"
    [showCaret]="true"
    [persistOnBlur]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with fixed z-index of 1500.

```html
<ion-popover
    [zIndex]="2000"
    [open]="true"
    [placement]="bottom"
    [showCaret]="true"
    [persistOnBlur]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with fixed z-index of 2000.

```html
<ion-popover
    [accessibilityType]="dialog"
    [open]="true"
    [placement]="bottom"
    [persistOnBlur]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with dialog accessibility type.

```html
<ion-popover
    [accessibilityType]="menu"
    [open]="true"
    [placement]="bottom"
    [persistOnBlur]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with menu accessibility type.

```html
<ion-popover
    [accessibilityType]="tooltip"
    [open]="true"
    [placement]="bottom"
    [persistOnBlur]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with tooltip accessibility type.

```html
<ion-popover
    [autoFocus]="false"
    [open]="true"
    [placement]="bottom"
    [persistOnBlur]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover without auto-focus behavior.

```html
<ion-popover
    [autoFocus]="true"
    [open]="true"
    [placement]="bottom"
    [persistOnBlur]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with auto-focus enabled (focus moves to first interactive element).

```html
<ion-popover
    [returnFocus]="false"
    [open]="true"
    [placement]="bottom"
    [persistOnBlur]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover without focus return to anchor on close.

```html
<ion-popover
    [returnFocus]="true"
    [open]="true"
    [placement]="bottom"
    [persistOnBlur]="true">
    <div slot="popover" class="popover-content">Popover content is placed here.</div>
</ion-popover>
```
Demonstrates popover with focus return enabled to anchor on close.