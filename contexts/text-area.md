---
realComponent: ion-text-area
description: Angular standalone text area component with design system styling, validation states, and resizing options
themes: [modern-light-ds, modern-dark-ds]
props:
  - name: size
    type: string
    category: visual
    required: false
    default: "md"
    values: [sm, md, lg]
    designTokens:
      sm:
        resolvesTo: "12px"
        tokenChain: "font-size -> --ion-lit-sizing-adaptive-50 -> 12px"
        appliesToCssProperty: "font-size"
      md:
        resolvesTo: "16px"
        tokenChain: "font-size -> --ion-lit-sizing-adaptive-100 -> 16px"
        appliesToCssProperty: "font-size"
      lg:
        resolvesTo: "20px"
        tokenChain: "font-size -> --ion-lit-sizing-adaptive-150 -> 20px"
        appliesToCssProperty: "font-size"

  - name: resize
    type: enum
    category: visual
    required: false
    default: "none"
    values: [none, manual, auto]
    designTokens:
      none:
        resolvesTo: "none"
        tokenChain: "resize -> none"
        appliesToCssProperty: "resize"
      manual:
        resolvesTo: "vertical"
        tokenChain: "resize -> vertical"
        appliesToCssProperty: "resize"
      auto:
        resolvesTo: "content"
        tokenChain: "field-sizing -> content"
        appliesToCssProperty: "field-sizing"

  - name: rows
    type: number
    category: visual
    required: false
    default: 2
    values: []
    designTokens: {}

  - name: value
    type: string
    category: content
    required: false
    default: ""
    values: []
    designTokens: {}

  - name: placeholder
    type: string
    category: content
    required: false
    default: ""
    values: []
    designTokens:
      light:
        resolvesTo: "#838993"
        tokenChain: "placeholder-color -> --ion-comp-field-text-placeholder-color-fg-enabled -> var(--ion-cont-color-role-light-text-icon-500) -> #838993"
        appliesToCssProperty: "color"
      dark:
        resolvesTo: "#676e79"
        tokenChain: "placeholder-color -> --ion-comp-field-text-placeholder-color-fg-enabled -> var(--ion-cont-color-role-dark-text-icon-700) -> #676e79"
        appliesToCssProperty: "color"

  - name: disabled
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens:
      light:
        resolvesTo: "#e9eaeb"
        tokenChain: "disabled-bg -> --ion-comp-field-container-color-bg-disabled -> var(--ion-cont-color-ui-base-layer-05) -> #e9eaeb"
        appliesToCssProperty: "background-color"
      dark:
        resolvesTo: "#2b3649"
        tokenChain: "disabled-bg -> --ion-comp-field-container-color-bg-disabled -> var(--ion-cont-color-ui-base-layer-05) -> #2b3649"
        appliesToCssProperty: "background-color"

  - name: readOnly
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens:
      light:
        resolvesTo: "#f9f9fa"
        tokenChain: "readonly-bg -> --ion-comp-field-container-color-bg-read-only -> var(--ion-cont-color-common-disabled-inverse) -> #f9f9fa"
        appliesToCssProperty: "background-color"
      dark:
        resolvesTo: "#1f2a3e"
        tokenChain: "readonly-bg -> --ion-comp-field-container-color-bg-read-only -> var(--ion-cont-color-common-disabled-inverse) -> #1f2a3e"
        appliesToCssProperty: "background-color"

  - name: required
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}

  - name: necessityIndicator
    type: enum
    category: visual
    required: false
    default: "requiredMarker"
    values: [requiredMarker, requiredLabel, optionalLabel, none]
    designTokens:
      requiredMarker:
        light:
          resolvesTo: "#c70000"
          tokenChain: "required-color -> --ion-comp-field-necessity-indicator-required-marker-color-fg-light -> #c70000"
          appliesToCssProperty: "color"
        dark:
          resolvesTo: "#fe3f3f"
          tokenChain: "required-color -> --ion-comp-field-necessity-indicator-required-marker-color-fg-dark -> #fe3f3f"
          appliesToCssProperty: "color"
      requiredLabel:
        light:
          resolvesTo: "#c70000"
          tokenChain: "required-label-color -> --ion-comp-field-necessity-indicator-required-label-color-fg-light -> #c70000"
          appliesToCssProperty: "color"
        dark:
          resolvesTo: "#fe3f3f"
          tokenChain: "required-label-color -> --ion-comp-field-necessity-indicator-required-label-color-fg-dark -> #fe3f3f"
          appliesToCssProperty: "color"
      optionalLabel:
        light:
          resolvesTo: "#838993"
          tokenChain: "optional-color -> --ion-comp-field-necessity-indicator-optional-label-color-fg-light -> #838993"
          appliesToCssProperty: "color"
        dark:
          resolvesTo: "#676e79"
          tokenChain: "optional-color -> --ion-comp-field-necessity-indicator-optional-label-color-fg-dark -> #676e79"
          appliesToCssProperty: "color"
      none:
        light:
          resolvesTo: "transparent"
          tokenChain: "none-color -> transparent"
          appliesToCssProperty: "color"
        dark:
          resolvesTo: "transparent"
          tokenChain: "none-color -> transparent"
          appliesToCssProperty: "color"

  - name: validationState
    type: enum
    category: visual
    required: false
    default: "none"
    values: [valid, invalid, warning, none]
    designTokens:
      valid:
        light:
          resolvesTo: "#2dc168"
          tokenChain: "validation-border -> --ion-cont-color-ui-status-positive -> #2dc168"
          appliesToCssProperty: "border-color"
        dark:
          resolvesTo: "#249d54"
          tokenChain: "validation-border -> --ion-cont-color-ui-status-positive -> #249d54"
          appliesToCssProperty: "border-color"
      invalid:
        light:
          resolvesTo: "#c70000"
          tokenChain: "validation-border -> --ion-cont-color-ui-status-negative -> #c70000"
          appliesToCssProperty: "border-color"
        dark:
          resolvesTo: "#fe3f3f"
          tokenChain: "validation-border -> --ion-cont-color-ui-status-negative -> #fe3f3f"
          appliesToCssProperty: "border-color"
      warning:
        light:
          resolvesTo: "#fe7f2a"
          tokenChain: "validation-border -> --ion-cont-color-ui-status-warning -> #fe7f2a"
          appliesToCssProperty: "border-color"
        dark:
          resolvesTo: "#ec5913"
          tokenChain: "validation-border -> --ion-cont-color-ui-status-warning -> #ec5913"
          appliesToCssProperty: "border-color"
      none:
        light:
          resolvesTo: "#d7d9dc"
          tokenChain: "default-border -> --ion-cont-color-field-moderate -> #d7d9dc"
          appliesToCssProperty: "border-color"
        dark:
          resolvesTo: "#535c6b"
          tokenChain: "default-border -> --ion-cont-color-field-moderate -> #535c6b"
          appliesToCssProperty: "border-color"

  - name: validationMode
    type: enum
    category: behavioral
    required: false
    default: "none"
    values: [none, onChange, onBlur, onSubmit]
    designTokens: {}

  - name: maxLength
    type: number
    category: behavioral
    required: false
    default: null
    values: []
    designTokens: {}

  - name: minLength
    type: number
    category: behavioral
    required: false
    default: null
    values: []
    designTokens: {}

  - name: showCount
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}

  - name: label
    type: string
    category: content
    required: false
    default: ""
    values: []
    designTokens: {}

  - name: labelPlacement
    type: enum
    category: visual
    required: false
    default: "vertical"
    values: [vertical, horizontal]
    designTokens: {}

  - name: labelAlignment
    type: enum
    category: visual
    required: false
    default: "start"
    values: [start, end]
    designTokens: {}

  - name: labelWidth
    type: string
    category: visual
    required: false
    default: ""
    values: []
    designTokens: {}

  - name: helperMessage
    type: string
    category: content
    required: false
    default: ""
    values: []
    designTokens: {}

  - name: name
    type: string
    category: behavioral
    required: false
    default: ""
    values: []
    designTokens: {}

  - name: ariaLabel
    type: string
    category: accessibility
    required: false
    default: ""
    values: []
    designTokens: {}

  - name: autoFocus
    type: boolean
    category: behavioral
    required: false
    default: false
    values: []
    designTokens: {}

  - name: disableAutoComplete
    type: boolean
    category: behavioral
    required: false
    default: false
    values: []
    designTokens: {}

  - name: defaultValue
    type: string
    category: content
    required: false
    default: ""
    values: []
    designTokens: {}

  - name: tabIndex
    type: number
    category: accessibility
    required: false
    default: 0
    values: []
    designTokens: {}

  - name: reset
    type: function
    category: behavioral
    required: false
    default: "() => { Object.assign(this, this.initialProperties); }"
    values: []
    designTokens: {}

jointTokens:
  - combination: "validationState=valid, disabled=false, readOnly=false"
    resolvesTo: "#2dc168"
    tokenChain: "field-state -> --ion-cont-color-ui-status-positive -> #2dc168 (light) / #249d54 (dark)"
    appliesToCssProperty: "border-color"
  - combination: "validationState=invalid, disabled=false, readOnly=false"
    resolvesTo: "#c70000"
    tokenChain: "field-state -> --ion-cont-color-ui-status-negative -> #c70000 (light) / #fe3f3f (dark)"
    appliesToCssProperty: "border-color"
  - combination: "validationState=warning, disabled=false, readOnly=false"
    resolvesTo: "#fe7f2a"
    tokenChain: "field-state -> --ion-cont-color-ui-status-warning -> #fe7f2a (light) / #ec5913 (dark)"
    appliesToCssProperty: "border-color"

propInteractions:
  - "resize='auto' uses CSS field-sizing property when supported by browser for automatic expansion"
  - "resize='manual' allows vertical user resizing via drag handle"
  - "resize='none' prevents any resizing (fixed dimensions)"
  - "showCount only displays meaningful information when maxLength is set"
  - "validationMode='onChange' triggers validation on every value change"
  - "validationMode='onBlur' triggers validation when text area loses focus"
  - "validationMode='onSubmit' defers validation until form submission"
  - "labelAlignment only applies when labelPlacement='horizontal'"
  - "labelWidth only applies when labelPlacement='horizontal'"
  - "when both defaultValue and value are provided, value takes precedence after initialization"

events:
  - name: valueChange
    payloadType: "CustomEvent<{ name: string, value: string }>"
    firesWhen: "Emits whenever the text area's value changes, including on every keystroke, paste, or programmatic value update"
    bindingSyntax: "(valueChange)="onValueChange($event)""
    emittedArgs: "CustomEvent with ITextAreaValueChangeEventArgs wrapped in event.detail"
    usageNote: "Access the payload via event.detail.name and event.detail.value (web element pattern)"

  - name: focusIn
    payloadType: "CustomEvent<void>"
    firesWhen: "Emits when the text area receives focus, either via keyboard navigation, mouse click, or programmatic focus"
    bindingSyntax: "(focusIn)="onFocusIn()""
    emittedArgs: "CustomEvent with void payload (web element pattern)"
    usageNote: "$event parameter contains the CustomEvent object, though no meaningful data is emitted"

  - name: focusOut
    payloadType: "CustomEvent<void>"
    firesWhen: "Emits when the text area loses focus, either by user navigating away, clicking elsewhere, or programmatic blur"
    bindingSyntax: "(focusOut)="onFocusOut()""
    emittedArgs: "CustomEvent with void payload (web element pattern)"
    usageNote: "$event parameter contains the CustomEvent object, though no meaningful data is emitted"

  - name: keyDown
    payloadType: "CustomEvent<KeyboardEvent>"
    firesWhen: "Emits on every keydown event within the text area, providing access to keyboard event details"
    bindingSyntax: "(keyDown)="onKeyDown($event)""
    emittedArgs: "CustomEvent with KeyboardEvent wrapped in event.detail"
    usageNote: "Access the keyboard event via event.detail (web element pattern)"

  - name: validationStateChange
    payloadType: "CustomEvent<'valid' | 'invalid' | 'warning' | 'none'>"
    firesWhen: "Emits when the validationState property changes from one value to another (e.g., from 'none' to 'valid' or 'invalid')"
    bindingSyntax: "(validationStateChange)="onValidationStateChange($event)""
    emittedArgs: "CustomEvent with ValidationState string wrapped in event.detail"
    usageNote: "Access the validation state via event.detail (web element pattern)"

needsReview:
  - "Dark theme validation state color tokens not fully traced: validationState=invalid (#c70000 in light, #fe3f3f in dark), validationState=valid (#2dc168 in light, #249d54 in dark), validationState=warning (#fe7f2a in light, #ec5913 in dark)"
  - "Enum props labelPlacement, labelAlignment, necessityIndicator, and validationMode have no designTokens entries - these are layout/behavior props with no direct token mapping, which is intentionally the case"
  - "Size-specific padding tokens not fully traced: sm/md/lg padding variations based on --ion-comp-field-container-spacing-padding-inline-start/end-* tokens need verification"
  - "placeholder color tokens traced but need verification for both themes across all component states"
  - "Text color tokens not traced for enabled/disabled/readOnly states in light and dark themes"
  - "Focus ring and outline color tokens not traced for accessibility focus states"
  - "Character count display styling tokens not traced from ds_tokens.css"
  - "Field container background color tokens not traced for disabled and read-only states across all validation states"
  - "Field container border-radius tokens not traced for sm/md/lg size variants"
  - "Field container gap (spacing) tokens not traced for sm/md/lg sizes"
  - "Cross-theme verification needed for all color tokens (only light theme traced for most properties)"
  - "Resize behavior tokens (field-sizing CSS property) not fully traced for browser compatibility scenarios"
  - "Helper message color tokens not traced for none/valid/invalid/warning states"
  - "Auto focus behavior styling not traced from ds_tokens.css"

---

## Usage Notes

Boolean props on this component must always be passed with an explicit string value — e.g. `disabled="true"` or `[disabled]="isDisabled"` — never as bare attribute presence (e.g. `disabled` alone, with no value). Bare attribute presence is a native HTML convention this component does NOT support; it will not be interpreted as true.

## size

Controls text area sizing through font size and proportional spacing adjustments. Supports sm, md, lg values.

**Visual cues:**
- sm: Small text area with 12px font size and compact spacing
- md: Medium text area with 16px font size and standard spacing (default)
- lg: Large text area with 20px font size and generous spacing
- All size variants include proportional padding adjustments

**When to use:**
- sm: Compact forms, data tables, space-constrained layouts
- md: Standard form fields, primary user input areas (default)
- lg: Prominent input areas, message fields, when extra visibility needed

## resize

Controls whether and how users can resize the text area.

**Visual cues:**
- none: No resize handle, fixed dimensions (default)
- manual: Resize handle at bottom-right corner for vertical adjustment
- auto: Automatically expands to fit content when supported by browser

**When to use:**
- none: Fixed-size text areas for consistent layout
- manual: Allow user control over text area height
- auto: Self-adjusting text areas for variable content length

## rows

Controls the initial number of visible text lines before scrolling.

**Visual cues:**
- Text area height scales proportionally with the rows value
- Shows approximately that many lines based on current font size

**When to use:**
- Set higher value for longer-form input with visible context
- Set lower value for compact layouts
- Most impactful when resize="none" - only sets initial height for auto/manual resize

## value

The current text content of the text area.

**Visual cues:**
- Text area displays the specified value
- Updates to this prop will update the displayed value
- Value changes trigger valueChange event emission

**When to use:**
- Set programmatically to populate with initial or updated data
- Empty string clears the text area
- Truncates to maxLength if maxLength property is set

## placeholder

The placeholder text shown when the text area is empty.

**Visual cues:**
- Displays placeholder text in empty text area in muted color (#838993 in light theme, #676e79 in dark theme)
- Placeholder text disappears as soon as user begins typing
- Never submitted as form data

**When to use:**
- Provide hints about expected content format or length
- Show example values to guide user input
- Should not be used as substitute for proper label

## disabled

Controls disabled state of the text area, preventing interaction and changing visual appearance.

**Visual cues:**
- When true: Text area appears non-interactive with reduced opacity background (#e9eaeb in light theme, #2b3649 in dark theme)
- Applies 'ion-ds-disabled' CSS class
- Prevents all user input and interaction

**When to use:**
- Set true when text area should be read-only but still visible
- Disable during operations that require user to wait
- Override default false when form permissions or validation-state require disabling

## readOnly

Controls whether the text area is read-only but still focusable and interactive.

**Visual cues:**
- When true: Text area appears non-editable but can be focused and copied
- Applies 'ion-ds-read-only' CSS class
- Light background (#f9f9fa in light theme, #1f2a3e in dark theme)
- Allows text selection and copying but prevents editing

**When to use:**
- Set true for data display that should be viewable but not modifiable
- Use for calculated or derived values that should not be edited
- Different from disabled as read-only fields can still be focused

## required

Controls whether the text area is marked as required, affecting necessityIndicator display and form validation.

**Visual cues:**
- When true: Text area marked as required, affects necessityIndicator display
- Sets required attribute on textarea element for browser validation
- Triggers browser validation when form submitted if empty

**When to use:**
- Set true for required form fields that must be filled
- Combined with necessityIndicator prop to show visual indicator
- Override default false for fields that are optional

## necessityIndicator

Controls the visual indicator for field requirement status.

**Visual cues:**
- requiredMarker: Asterisk (*) symbol displayed with label (#c70000 in light theme, #fe3f3f in dark theme)
- requiredLabel: Text 'Required' displayed with label
- optionalLabel: Text 'Optional' displayed with label (#838993 in light theme, #676e79 in dark theme)
- none: No requirement indicator displayed

**When to use:**
- requiredMarker: Standard pattern for required fields with label
- requiredLabel: More explicit text indication for required fields
- optionalLabel: Explicitly mark optional fields for clarity
- none: Hide requirement indicators, useful when context is clear

## validationState

Controls validation state of the text area, affecting visual appearance and helper message handling.

**Visual cues:**
- none: Default state, uses moderate border color (#d7d9dc in light theme, #535c6b in dark theme)
- valid: Green border color (#2dc168 in light theme, #249d54 in dark theme), indicates successful validation
- invalid: Red border color (#c70000 in light theme, #fe3f3f in dark theme), indicates validation failure
- warning: amber border color (#fe7f2a in light theme, #ec5913 in dark theme), indicates caution state
- Sets aria-invalid attribute to true for invalid state

**When to use:**
- none: Default state when no validation is needed
- valid: Display successful validation status
- invalid: Show error state and browser validation message
- warning: Display caution state when input requires attention

## validationMode

Controls when validation is triggered and helper message is updated with validation results.

**Visual cues:**
- none: No automatic validation (default)
- onChange: Validation runs on every input change
- onBlur: Validation runs when text area loses focus
- onSubmit: Validation runs when form is submitted

**When to use:**
- none: Manual validation control or no validation needed
- onChange: Real-time validation feedback as user types
- onBlur: Validation feedback after user completes text area
- onSubmit: Validation runs as part of form submission process

## maxLength

Controls maximum character length allowed in the text area.

**Visual cues:**
- Prevents typing beyond specified character limit
- Can be combined with showCount to display character count

**When to use:**
- Set when text area should not exceed character limit
- Useful for database field constraints, message limits
- Combine with minLength for range constraints

## minLength

Controls minimum character length required for valid input.

**Visual cues:**
- Text area must contain at least this many characters to be valid
- Invalid length triggers browser validation message and invalid state
- Can be combined with showCount to display character count

**When to use:**
- Set when text area requires minimum number of characters
- Useful for validation of required content length
- Combine with maxLength for range constraints

## showCount

Controls visibility of character count display.

**Visual cues:**
- When true: Displays character count (current/maxLength) at end of text area
- When false: No character count displayed (default)
- Updates dynamically as user types
- Only meaningful when maxLength is set

**When to use:**
- Set true when it helps user to know remaining characters
- Useful for message fields, data entry with limits
- Should be combined with maxLength prop for meaningful display

## label

Controls the text label displayed above (vertical) or beside (horizontal) the text area.

**Visual cues:**
- When set: Displays label text with styling based on labelPlacement property
- When empty: Text area renders without visible label
- Label positioning controlled by labelPlacement property

**When to use:**
- Primary method for identifying text area purpose to users
- Should be omitted for purely decorative or unlabeled text areas
- Used as fallback for ariaLabel if not explicitly set

## labelPlacement

Controls the position of the label relative to the text area.

**Visual cues:**
- vertical: Label appears above the text area (default)
- horizontal: Label appears beside the text area

**When to use:**
- vertical: Standard form layout, most commonly used
- horizontal: Compact layouts, data grids, when horizontal space is available
- When horizontal, labelAlignment and labelWidth properties become relevant

## labelAlignment

Controls alignment of the label relative to the text area when labelPlacement is horizontal.

**Visual cues:**
- start: Label aligned to left/start side (default)
- end: Label aligned to right/end side

**When to use:**
- start: Standard left-aligned labels in horizontal form layouts
- end: Right-aligned labels, useful for certain design patterns
- Only applicable when labelPlacement is set to horizontal

## labelWidth

Controls the width of the label when labelPlacement is horizontal. Accepts various CSS units (px, %, em, etc.).

**Visual cues:**
- When set: Label has specified width in horizontal layout
- When empty: Label width determined by content length
- Supports pixel values, percentages, em, rem, and other CSS units

**When to use:**
- Set when using horizontal label placement to create consistent label column width
- Useful for form alignment when multiple horizontal label text areas are stacked
- Only applicable when labelPlacement is set to horizontal

## helperMessage

Controls helper/explanatory message displayed below the text area.

**Visual cues:**
- When set: Displays helper message text below text area
- When empty: No helper message displayed
- Can be replaced by browser validation message when validationState is set
- Helper message color varies based on validationState

**When to use:**
- Provide helpful guidance about text area requirements or format
- Display dynamic validation messages based on validationState
- Show contextual information about the text area

## name

Controls the name attribute of the textarea element, used for form submission and identification.

**Visual cues:**
- Not directly visible to users
- Used in form data submission and validation referencing
- Emitted with valueChange events as field identifier

**When to use:**
- Set for all text areas in forms to properly submit form data
- Required for proper form validation and submission
- Helps identify fields in event handlers and backend processing

## ariaLabel

Provides accessibility label for screen readers. Falls back to label if not set.

**Visual cues:**
- Not visible to sighted users
- Read by screen readers to identify the text area

**When to use:**
- Set when different from visible label for accessibility
- Use when you need more descriptive label for screen readers
- Leave empty if label prop provides sufficient description

## autoFocus

Controls whether text area automatically receives focus when page or component loads.

**Visual cues:**
- When true: Text area receives focus and cursor on page load
- When false: Text area does not auto-focus (default)
- Scrolls page to text area if necessary

**When to use:**
- Set true for primary text area on page when immediate input expected
- Useful for forms where text area is primary focus
- Be cautious with this as it can interfere with page navigation

## disableAutoComplete

Controls whether browser's autocomplete functionality is disabled for this text area.

**Visual cues:**
- When true: Browser autocomplete is disabled
- When false: Browser autocomplete is enabled (default, sets autocomplete='on')

**When to use:**
- Set true for sensitive inputs where autocomplete suggestions are not appropriate
- Use for fields where browser suggestions are not helpful
- Keep false for convenience in standard data entry fields

## defaultValue

Controls default value that is set only during component initialization.

**Visual cues:**
- When set and no value prop provided: Text area displays default value on initialization
- Only applied when value prop is not set during ngAfterViewInit lifecycle hook
- Does not update text area if value prop is already set

**When to use:**
- Provide initial value when component first renders
- Use when you need a default but want value prop to take precedence if set
- Different from value as it only applies during initialization, not updates

## tabIndex

Controls tab index for keyboard navigation order in the form.

**Visual cues:**
- Affects order in which text areas receive focus when tabbing through page
- Default (0): Part of natural tab order
- Negative values: Removed from tab order
- Positive values: Custom tab order (not recommended)

**When to use:**
- Generally should be left at default (0) for natural tab order
- Override only when specific tab sequence is required

## reset

Programmatic reset function to restore text area to its initial properties and value.

**Visual property:** none (behavioral)

**When to use:**
- This is a behavioral prop not derivable from visual design
- Should generally be left at its default unless specifically called
- Restores all props to values stored during ngOnInit lifecycle hook
- Used to reset form fields to initial state

## Events

### valueChange
Emits whenever the text area's value changes, including on every keystroke, paste, or programmatic value update. Emits a CustomEvent with payload wrapped in `event.detail`.

**Emitted args:** `CustomEvent<{ name: string, value: string }>`

**When to use:**
- Capture user input for validation or real-time processing
- Track text area changes for analytics
- Implement content length requirements validation

**How to use:**
```typescript
// Angular component handler method - web element pattern
onValueChange(event: CustomEvent<{ name: string, value: string }>) {
  console.log("Field name:", event.detail.name);
  console.log("Current value:", event.detail.value);
  // Access payload via event.detail for web element events
}
```

**Binding syntax:**
```html
<ion-text-area
  name="userMessage"
  (valueChange)="onValueChange($event)">
</ion-text-area>
```

### focusIn
Emits when the text area receives focus, either via keyboard navigation, mouse click, or programmatic focus. Emits a CustomEvent with void payload.

**Emitted args:** `CustomEvent<void>`

**When to use:**
- Trigger UI changes when text area gains focus
- Start validation timers or form state tracking
- Implement custom accessibility behavior

**How to use:**
```typescript
// Angular component handler method
onFocusIn(event: CustomEvent<void>): void {
  console.log("Text area focused");
  this.isTextAreaFocused = true;
  // event.detail is undefined (void payload)
}
```

**Binding syntax:**
```html
<ion-text-area (focusIn)="onFocusIn()"></ion-text-area>
```

### focusOut
Emits when the text area loses focus. Triggers validation if `validationMode` is set to `onBlur`. Emits a CustomEvent with void payload.

**Emitted args:** `CustomEvent<void>`

**When to use:**
- Trigger validation when user completes text area input
- Track form completion state
- Reset UI elements activated on focus

**How to use:**
```typescript
// Angular component handler method
onFocusOut(event: CustomEvent<void>): void {
  console.log("Text area lost focus");
  this.validateTextArea();
  // event.detail is undefined (void payload)
}
```

**Binding syntax:**
```html
<ion-text-area validationMode="onBlur" (focusOut)="onFocusOut()"></ion-text-area>
```

### keyDown
Emits on every keydown event within the text area, providing access to keyboard event details. Emits a CustomEvent with KeyboardEvent wrapped in event.detail.

**Emitted args:** `CustomEvent<KeyboardEvent>`

**When to use:**
- Implement keyboard shortcuts or special key handling
- Prevent default behavior for certain key combinations
- Track specific keyboard interactions within the text area

**How to use:**
```typescript
// Angular component handler method - web element pattern
onKeyDown(event: CustomEvent<KeyboardEvent>) {
  if (event.detail.key === 'Enter' && event.detail.ctrlKey) {
    event.detail.preventDefault();
    this.submitOnCtrlEnter();
  }
  // Access keyboard event via event.detail for web element events
}
```

**Binding syntax:**
```html
<ion-text-area (keyDown)="onKeyDown($event)"></ion-text-area>
```

### validationStateChange
Emits when the validationState property changes. Emits a CustomEvent with validation state wrapped in `event.detail`.

**Emitted args:** `CustomEvent<"valid" | "invalid" | "warning" | "none">`

**When to use:**
- React to validation state changes in the UI
- Trigger form submission enable/disable logic
- Implement custom validation feedback animations

**How to use:**
```typescript
// Angular component handler method - web element pattern
onValidationStateChange(event: CustomEvent<"valid" | "invalid" | "warning" | "none">) {
  console.log("Validation state changed to:", event.detail);
  if (event.detail === "invalid") {
    this.showValidationMessage();
  }
  // Access validation state via event.detail for web element events
}
```

**Binding syntax:**
```html
<ion-text-area
  validationMode="onChange"
  (validationStateChange)="onValidationStateChange($event)">
</ion-text-area>
```

### Complete event binding example:

```html
<ion-text-area
  label="Message"
  name="userMessage"
  maxLength="500"
  validationMode="onBlur"
  (valueChange)="onValueChange($event)"
  (focusIn)="onFocusIn()"
  (focusOut)="onFocusOut()"
  (keyDown)="onKeyDown($event)"
  (validationStateChange)="onValidationStateChange($event)">
</ion-text-area>
```

**Handler implementation:**
```typescript
import { CustomEvent } from '@angular/platform-browser';

onValueChange(event: CustomEvent<{ name: string, value: string }>) {
  console.log('Field:', event.detail.name);
  console.log('Value:', event.detail.value);
}

onFocusIn(event: CustomEvent<void>) {
  console.log('Text area focused');
}

onFocusOut(event: CustomEvent<void>) {
  console.log('Text area lost focus');
  this.validateTextArea();
}

onKeyDown(event: CustomEvent<KeyboardEvent>) {
  if (event.detail.ctrlKey && event.detail.key === 'Enter') {
    event.detail.preventDefault();
    this.submitMessage();
  }
}

onValidationStateChange(event: CustomEvent<"valid" | "invalid" | "warning" | "none">) {
  console.log('Validation state:', event.detail);
}
```

## Examples

```html
<ion-text-area label="Label" label-placement="vertical"></ion-text-area>
```
Demonstrates default text area with vertical label placement.

```html
<ion-text-area size="sm" label="Label" label-placement="vertical"></ion-text-area>
```
Demonstrates small-sized text area.

```html
<ion-text-area size="md" label="Label" label-placement="vertical"></ion-text-area>
```
Demonstrates medium-sized text area (default).

```html
<ion-text-area size="lg" label="Label" label-placement="vertical"></ion-text-area>
```
Demonstrates large-sized text area.

```html
<ion-text-area label="Label" label-placement="vertical"></ion-text-area>
```
Demonstrates text area with vertical label placement.

```html
<ion-text-area label="" label-placement=""></ion-text-area>
```
Demonstrates text area without label.

```html
<ion-text-area label="Label" label-placement="vertical"></ion-text-area>
```
Demonstrates text area with vertical label placement.

```html
<ion-text-area label="Label" label-placement="horizontal"></ion-text-area>
```
Demonstrates text area with horizontal label placement.

```html
<ion-text-area label="Label" label-placement="horizontal" label-alignment="start" label-width="150px"></ion-text-area>
```
Demonstrates text area with label aligned to start.

```html
<ion-text-area label="Label" label-placement="horizontal" label-alignment="end" label-width="150px"></ion-text-area>
```
Demonstrates text area with label aligned to end.

```html
<ion-text-area placeholder="Placeholder"></ion-text-area>
```
Demonstrates text area with placeholder.

```html
<ion-text-area placeholder=""></ion-text-area>
```
Demonstrates text area without placeholder.

```html
<ion-text-area default-value="Value"></ion-text-area>
```
Demonstrates text area with default value.

```html
<ion-text-area default-value=""></ion-text-area>
```
Demonstrates text area without default value.

```html
<ion-text-area helper-message="Valid Helper Message" validation-state="valid"></ion-text-area>
```
Demonstrates text area in valid state with helper message.

```html
<ion-text-area helper-message="Invalid Helper Message" validation-state="invalid"></ion-text-area>
```
Demonstrates text area in invalid state with helper message.

```html
<ion-text-area helper-message="Warning Helper Message" validation-state="warning"></ion-text-area>
```
Demonstrates text area in warning state with helper message.

```html
<ion-text-area disabled="false"></ion-text-area>
```
Demonstrates text area in enabled state.

```html
<ion-text-area disabled="true"></ion-text-area>
```
Demonstrates text area in disabled state.

```html
<ion-text-area read-only="false"></ion-text-area>
```
Demonstrates text area that is not read-only.

```html
<ion-text-area read-only="true"></ion-text-area>
```
Demonstrates text area in read-only state.

```html
<ion-text-area helper-message="Helper Message" validation-state="none"></ion-text-area>
```
Demonstrates helper message without validation state.

```html
<ion-text-area show-count="false"></ion-text-area>
```
Demonstrates text area without character counter.

```html
<ion-text-area show-count="true" max-length="100"></ion-text-area>
```
Demonstrates text area with character counter.

```html
<ion-text-area max-length="5"></ion-text-area>
```
Demonstrates text area with max-length of 5.

```html
<ion-text-area max-length="10"></ion-text-area>
```
Demonstrates text area with max-length of 10.

```html
<ion-text-area max-length="20" min-length="5" show-count="true" validation-mode="onBlur"></ion-text-area>
```
Demonstrates text area with min-length of 5.

```html
<ion-text-area max-length="20" min-length="10" show-count="true" validation-mode="onBlur"></ion-text-area>
```
Demonstrates text area with min-length of 10.

```html
<ion-text-area auto-focus="false"></ion-text-area>
```
Demonstrates text area without auto focus.

```html
<ion-text-area auto-focus="true"></ion-text-area>
```
Demonstrates text area with auto focus.

```html
<ion-text-area resize="auto"></ion-text-area>
```
Demonstrates text area with auto resize behavior.

```html
<ion-text-area resize="none"></ion-text-area>
```
Demonstrates text area with no resize behavior.

```html
<ion-text-area resize="manual"></ion-text-area>
```
Demonstrates text area with manual resize behavior.

```html
<ion-text-area rows="2"></ion-text-area>
```
Demonstrates text area with 2 rows.

```html
<ion-text-area rows="5"></ion-text-area>
```
Demonstrates text area with 5 rows.

```html
<ion-text-area rows="10"></ion-text-area>
```
Demonstrates text area with 10 rows.

```html
<ion-text-area required="true" validation-mode="onBlur"></ion-text-area>
```
Demonstrates text area with required validation on blur.

```html
<ion-text-area required="true" validation-mode="onChange"></ion-text-area>
```
Demonstrates text area with required validation on change.

```html
<ion-text-area></ion-text-area>
```
Demonstrates text area without ariaLabel.

```html
<ion-text-area aria-label="This is aria label explicitly defined."></ion-text-area>
```
Demonstrates text area with explicit ariaLabel.