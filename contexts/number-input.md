---
realComponent: ion-number-input
description: Angular number input component with spinner controls, number formatting, modifiers, and validation support
themes: ["modern-light-ds", "modern-dark-ds"]
props:
  - name: disabled
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens:
      light:
        resolvesTo: "#d7d9dc"
        tokenChain: "disabled state -> --ion-cont-color-role-light-neutral-250 (#d7d9dc)"
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
        tokenChain: "read-only state -> --ion-cont-color-role-light-neutral-100 (#f9f9fa)"
        appliesToCssProperty: "background-color"
  - name: size
    type: string
    category: visual
    required: false
    default: "md"
    values: ["sm", "md", "lg"]
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
  - name: helperMessageAsTooltip
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
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
          tokenChain: "validation valid -> --ion-lit-color-leonardo-base-positive (#2dc168)"
          appliesToCssProperty: "color"
      invalid:
        light:
          resolvesTo: "#c70000"
          tokenChain: "validation invalid -> --ion-lit-color-leonardo-base-negative (#c70000)"
          appliesToCssProperty: "color"
      warning:
        light:
          resolvesTo: "#fe7f2a"
          tokenChain: "validation warning -> --ion-lit-color-leonardo-base-warning (#fe7f2a)"
          appliesToCssProperty: "color"
  - name: validationMode
    type: enum
    category: visual
    required: false
    default: "none"
    values: [onBlur, onChange, onSubmit, none]
    designTokens: {}
  - name: necessityIndicator
    type: enum
    category: visual
    required: false
    default: "requiredMarker"
    values: [requiredMarker, requiredLabel, optionalLabel, none]
    designTokens: {}
  - name: placeholder
    type: string
    category: content
    required: false
    default: ""
    values: []
    designTokens:
      light:
        resolvesTo: "#c4c7cb"
        tokenChain: "placeholder text -> --ion-cont-color-role-light-text-icon-300 (#c4c7cb)"
        appliesToCssProperty: "color"
  - name: tabIndex
    type: number
    category: accessibility
    required: false
    default: 0
    values: []
    designTokens: {}
  - name: autoFocus
    type: boolean
    category: behavioral
    required: false
    default: false
    values: []
    designTokens: {}
  - name: name
    type: string
    category: accessibility
    required: false
    default: ""
    values: []
    designTokens: {}
  - name: minValue
    type: number
    category: behavioral
    required: false
    default: none found
    values: []
    designTokens: {}
  - name: maxValue
    type: number
    category: behavioral
    required: false
    default: none found
    values: []
    designTokens: {}
  - name: stepValue
    type: number
    category: behavioral
    required: false
    default: 1
    values: []
    designTokens: {}
  - name: disableSpinner
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
  - name: disableMouseWheel
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
  - name: roundingMode
    type: enum
    category: visual
    required: false
    default: "none"
    values: [none, default, up, down]
    designTokens: {}
  - name: focusAction
    type: enum
    category: behavioral
    required: false
    default: "none"
    values: [none, selectAll, cursorOnTheLeft, cursorOnTheRight, customAction]
    designTokens: {}
  - name: textAlignment
    type: enum
    category: visual
    required: false
    default: "right"
    values: [left, right, center]
    designTokens:
      left:
        light:
          resolvesTo: "left"
          tokenChain: "text alignment -> CSS property value directly"
          appliesToCssProperty: "text-align"
      right:
        light:
          resolvesTo: "right"
          tokenChain: "default text alignment -> CSS property value directly"
          appliesToCssProperty: "text-align"
      center:
        light:
          resolvesTo: "center"
          tokenChain: "text alignment -> CSS property value directly"
          appliesToCssProperty: "text-align"
  - name: spinner
    type: enum
    category: visual
    required: false
    default: "default"
    values: [none, default, wrapHorizontal, wrapHorizontalEnd, wrapVertical]
    designTokens: {}
  - name: format
    type: Format
    category: visual
    required: false
    default: "none"
    values: ["none", "{ decimalPlaces: number }", "{ locale: string }", "{ CMFmt: ionweb.cm.Format }"]
    designTokens: {}
  - name: enableModifiers
    type: boolean
    category: behavioral
    required: false
    default: false
    values: []
    designTokens: {}
  - name: retainModifiers
    type: boolean
    category: behavioral
    required: false
    default: false
    values: []
    designTokens: {}
  - name: enableCustomModifiers
    type: "{ [modifier: string]: number }"
    category: behavioral
    required: false
    default: "{}"
    values: []
    designTokens: {}
  - name: ariaLabel
    type: string
    category: accessibility
    required: false
    default: ""
    values: []
    designTokens: {}
  - name: value
    type: "number | INumberInputValue"
    category: content
    required: false
    default: undefined
    values: []
    designTokens: {}
  - name: defaultValue
    type: number
    category: content
    required: false
    default: none found
    values: []
    designTokens: {}
  - name: required
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
  - name: inputMode
    type: enum
    category: accessibility
    required: false
    default: none found
    values: [text, numeric, decimal]
    designTokens: {}
  - name: customFormatter
    type: "(value: number) => string"
    category: behavioral
    required: false
    default: none found
    values: []
    designTokens: {}
  - name: customParser
    type: "(value: string) => number"
    category: behavioral
    required: false
    default: none found
    values: []
    designTokens: {}
events:
  - name: valueChange
    payloadType: "CustomEvent<{ name: string, value: number | undefined }>"
    firesWhen: "on every value change through user input, spinner interaction, or programmatic updates"
    detailAccess: "event.detail.name (string), event.detail.value (number | undefined)"
    bindingSyntax: "(valueChange)=\"onValueChange($event)\""
  - name: focusIn
    payloadType: "CustomEvent<void>"
    firesWhen: "when the input field gains focus"
    detailAccess: "void, event.detail is undefined"
    bindingSyntax: "(focusIn)=\"onFocusIn($event)\""
  - name: focusOut
    payloadType: "CustomEvent<void>"
    firesWhen: "when the input field loses focus, after value is committed"
    detailAccess: "void, event.detail is undefined"
    bindingSyntax: "(focusOut)=\"onFocusOut($event)\""
  - name: invalidValueSet
    payloadType: "CustomEvent<number>"
    firesWhen: "when user attempts to set an invalid (NaN) value"
    detailAccess: "event.detail (number) - the invalid value that was attempted"
    bindingSyntax: "(invalidValueSet)=\"onInvalidValueSet($event)\""
  - name: customFocusAction
    payloadType: "CustomEvent<{ input: HTMLElement }>"
    firesWhen: "when focusAction is set to 'customAction' and input gains focus"
    detailAccess: "event.detail.input (HTMLElement) - reference to the input element"
    bindingSyntax: "(customFocusAction)=\"onCustomFocusAction($event)\""
  - name: currentInput
    payloadType: "CustomEvent<string>"
    firesWhen: "on every keystroke and value change, returns the currently provided input"
    detailAccess: "event.detail (string) - current input value as string"
    bindingSyntax: "(currentInput)=\"onCurrentInput($event)\""
  - name: keyDown
    payloadType: "CustomEvent<KeyboardEvent>"
    firesWhen: "on every keydown event in the input field"
    detailAccess: "event.detail (KeyboardEvent) - the keyboard event object"
    bindingSyntax: "(keyDown)=\"onKeyDown($event)\""
  - name: validationStateChange
    payloadType: "CustomEvent<ValidationState>"
    firesWhen: "when the validation state changes dynamically"
    detailAccess: "event.detail (ValidationState) - current validation state: 'valid' | 'invalid' | 'warning' | 'none'"
    bindingSyntax: "(validationStateChange)=\"onValidationStateChange($event)\""
jointTokens:
  - combination: "spinner=default"
    resolvesTo: "#ffffff"
    tokenChain: "spinner button background -> --ion-comp-spin-button-container-color-bg-enabled -> --ion-lit-color-palette-light-navy-1100 (#ffffff)"
    appliesToCssProperty: "background-color"
  - combination: "spinner=default, spinner button enabled"
    resolvesTo: "#030f26"
    tokenChain: "spinner icon color -> --ion-comp-spin-button-container-icon-color-fg-enabled -> --ion-lit-color-leonardo-base-neutral (#030f26)"
    appliesToCssProperty: "color"
propInteractions:
  - "spinner and textAlignment have automatic interaction: when spinner=wrapVertical or wrapHorizontal, textAlignment defaults to 'center'; when spinner=wrapHorizontalEnd, textAlignment defaults to 'left'; when spinner=default or none, textAlignment defaults to 'right'"
  - "enableModifiers and retainModifiers work together: retainModifiers only takes effect when enableModifiers is true or enableCustomModifiers contains actual modifier definitions"
  - "disableSpinner overrides spinner prop: when disableSpinner=true, spinner buttons are hidden regardless of spinner value"
  - "validationMode determines when validation runs: 'onChange' validates on each keystroke, 'onBlur' validates when input loses focus, 'onSubmit' validates on form submission, 'none' disables automatic validation"
  - "format and customFormatter/customParser are mutually dependent: customFormatter and customParser must both be provided together, and when provided they override the format prop"
  - "minValue and maxValue with stepValue control value constraints: spinner and mouse wheel increment/decrement respect min/max bounds, values beyond bounds are clamped to nearest valid value"
  - "textAlignment prop can override automatic behavior: explicit textAlignment value takes precedence over defaults derived from spinner prop"
needsReview:
  - "Dark theme tokens not traced for validationState colors, disabled state colors, placeholder colors, or spinner button colors - only light theme values documented"
  - "Size prop design tokens (min-height, padding, border-radius for sm/md/lg) not resolved to actual pixel values from ds_tokens.css - component tokens referenced but not traced to final values"
  - "Spinner button hover/pressed/disabled state colors not traced from actual token definitions - only enabled state colors documented"
  - "Format prop design tokens not traced - format object structure documented but specific token mappings for decimalPlaces/locale/CMFmt not provided"
  - "Custom formatter/parser function signatures documented but no example implementations or token mappings provided"
  - "RoundingMode prop design tokens not traced - enum values exist but no corresponding formatting behavior or token values documented"
  - "InputMode prop design tokens not traced - affects mobile keyboard type but no token mappings documented"
  - "MqDesignStringParserService responsive sizing behavior not verifiable without runtime context - defaults to 'md' when MQ strings used"
  - "Modifier symbols (k, K, t, T, m, M, b, B, y, Y) default multiplier values not documented - mentioned in stories but actual values not traced"
  - "Complete cross-product of spinner type with size and state combinations not provided - only basic spinner button tokens documented"
  - "Keyboard navigation behaviors (ArrowUp/Down, Home/End, Enter/Tab) documented in code but no corresponding design tokens documented"
  - "Focus ring color tokens and focus state styling not traced from provided token files"
  - "Helper message tooltip placement tokens not fully documented - only default MQ placement string documented"
  - "Minimal style configuration (shell.minimalStyle) affects button transparency but design tokens not traced"
  - "Border radius tokens for validation states and spinner layouts referenced in CSS but not resolved to actual pixel values"
---

## Usage Notes

Boolean props on this component must always be passed with an explicit string value — e.g. `disabled="true"` or `[disabled]="isDisabled"` — never as bare attribute presence (e.g. `disabled` alone, with no value). Bare attribute presence is a native HTML convention this component does NOT support; it will not be interpreted as true.

## disabled

Disables the number input field and all spinner controls, preventing user interaction.

**Visual cues:**
- When true: Input field appears non-interactive with reduced opacity and disabled cursor styling
- Spinner buttons appear disabled and do not respond to mouse interactions
- Background color changes to indicate disabled state

**When to use:**
- Set true when the number input should not be modified by users
- Use when the field is conditionally available based on application state
- Override default false when form state or permissions restrict numeric input

## readOnly

Disables editing while keeping the input field and value visible and accessible.

**Visual cues:**
- When true: Input field appears with read-only styling but value remains visible
- Spinner buttons appear disabled and do not respond to interactions
- Text can be selected and copied but cannot be edited

**When to use:**
- Set true when values should be viewed but not modified
- Use for displaying calculated or derived numeric values
- Override default false when you need to preserve the appearance while preventing editing

## size

Controls the dimensions of the number input field through predefined size variants and responsive MQ design strings.

**Visual cues:**
- sm: Smaller input field with reduced height and padding, suitable for compact layouts
- md: Medium input field (default), standard sizing for general use
- lg: Larger input field with increased height and padding, more prominent appearance
- MQ strings: Supports responsive sizing that changes based on screen size (e.g., "xs=sm;sm=md;md=md;lg=lg")

**When to use:**
- sm: Navigation toolbars, action bars with space constraints, compact forms
- md: Primary numeric input fields in standard forms (default)
- lg: Primary call-to-action numeric inputs, prominent data entry points
- MQ strings: Responsive layouts where size should adapt to available screen space

**Responsive behavior:**
- Supports MQ design strings parsed by MqDesignStringParserService for responsive sizing
- Returns default "md" if invalid size string provided
- Component uses CSS classes like `ion-ds-sm`, `ion-ds-md`, `ion-ds-lg` for styling

## label

Provides descriptive text for the number input field.

**Visual cues:**
- When set: Displays text above or beside the input field based on labelPlacement
- When empty: Input field renders without visible label (may use placeholder or ariaLabel instead)

**When to use:**
- Primary method for describing the purpose of the numeric input
- Should be concise and clearly indicate what number should be entered
- Falls back to empty string if falsy value provided

## labelPlacement

Determines the position of the label relative to the input field.

**Visual cues:**
- vertical: Label appears above the input field (default), most common pattern
- horizontal: Label appears beside the input field, requires labelWidth for proper spacing

**When to use:**
- vertical: Most standard form layouts, adequate horizontal space (default)
- horizontal: Compact layouts where vertical space is limited, side-by-side form patterns
- labelAlignment prop affects label placement only when labelPlacement is set to horizontal

## labelAlignment

Controls the horizontal alignment of the label when labelPlacement is horizontal.

**Visual cues:**
- start: Label aligned to the left side of the input field (default)
- end: Label aligned to the right side of the input field

**When to use:**
- start: Standard left-aligned labels, most common pattern (default)
- end: Right-aligned labels for right-to-left languages or specific design requirements
- Only has visual effect when labelPlacement is set to horizontal

## labelWidth

Specifies the width of the label element when labelPlacement is horizontal.

**Visual cues:**
- When set: Label element uses specified width, creating consistent spacing between labels
- When empty: Label uses auto width based on content

**When to use:**
- Set to pixel value or CSS unit when labelPlacement is horizontal for consistent alignment
- Use to create uniform label widths across multiple form fields
- Only has effect when labelPlacement is set to horizontal

## helperMessage

Provides auxiliary text beneath the input field for guidance or validation feedback.

**Visual cues:**
- When set: Displays text below the input field
- Can be overridden by validation messages when validationState is set
- When helperMessageAsTooltip is true, displays as tooltip instead

**When to use:**
- Provide guidance on expected values or format
- Show contextual help for the input field
- Will be replaced with validation message when validation state changes to invalid/warning/valid

## helperMessageAsTooltip

Controls whether the helper message appears as a tooltip or inline text.

**Visual cues:**
- When true: Helper message appears as tooltip on hover/focus
- When false: Helper message displays inline below the input field (default)

**When to use:**
- Set true when space is limited or inline feedback is not desired
- Keep false (default) when inline guidance is preferred
- Tooltip placement can be controlled with tooltipPlacement prop using MQ string format

## validationState

Controls the visual validation state of the number input field.

**Visual cues:**
- valid: Green (#2dc168) indicator, shows success state
- invalid: Red (#c70000) indicator, shows error state
- warning: Orange (#fe7f2a) indicator, shows warning state
- none: No validation state indicators (default)

**When to use:**
- valid: When input passes all validation requirements
- invalid: When input fails validation and needs correction
- warning: When input passes but has potential issues or deprecation warnings
- none: When no validation state should be displayed (default)
- Affects border color, icon display, and helper message styling based on state

## validationMode

Determines when validation checks are performed on the input value.

**Visual cues:**
- onBlur: Validation runs when input loses focus
- onChange: Validation runs immediately on each keystroke
- onSubmit: Validation runs on form submission
- none: No automatic validation (default)

**When to use:**
- onBlur: Standard form validation pattern, validate after entry is complete
- onChange: Real-time validation for immediate feedback
- onSubmit: Validate only when form is about to be submitted
- none: When validation is handled externally or not required (default)

## necessityIndicator

Controls the visual indicator for required/optional field status.

**Visual cues:**
- requiredMarker: Shows asterisk (*) prefix (default)
- requiredLabel: Shows "Required" label text
- optionalLabel: Shows "Optional" label text
- none: No necessity indicator displayed

**When to use:**
- requiredMarker: Standard pattern for required fields (default with required=true)
- requiredLabel: When explicit text label is preferred over asterisk
- optionalLabel: When you want to explicitly mark optional fields
- none: When field necessity is implied by context or not needed

## placeholder

Provides placeholder text that appears in the input field when empty.

**Visual cues:**
- When set: Displays gray text in input field when value is empty
- When empty: No placeholder text shown
- Styled using placeholder text color token

**When to use:**
- Provide guidance on expected value or format when field is empty
- Show example values or format hints
- Disappears when field has content or is focused

## tabIndex

Controls the tab order and keyboard navigation behavior of the input field.

**Visual cues:**
- Controls the order in which the input field is reached when tabbing through the interface

**When to use:**
- Set to custom number to control tab order in complex forms
- Set to -1 to remove from tab navigation entirely
- Settings should follow accessibility guidelines for logical tab order

## autoFocus

Automatically focuses the input field when the component loads.

**Visual cues:**
- When true: Input field receives focus immediately on page load, cursor appears in field

**When to use:**
- Set true for the primary input field that should be the starting point
- Keep false (default) when focus should start elsewhere or be user-controlled
- Be careful with multiple autofocus elements as only one can be focused at a time

## name

Provides the name attribute for form submission and identification.

**Visual cues:**
- No visible effect, used for form data and programmatic identification

**When to use:**
- Set explicitly when the field is part of a form that will be submitted
- Used as the key in form data when form is submitted
- Included in valueChange event data for identification

## minValue

Specifies the minimum allowed value for the number input.

**Visual cues:**
- No visual effect, constrains input programmatically
- Values below min are clamped to min when using spinner or validation

**When to use:**
- Set to enforce lower bounds on numeric input
- Spinner controls will not decrement below this value
- Validation may show error if value is below min depending on validationMode

## maxValue

Specifies the maximum allowed value for the number input.

**Visual cues:**
- No visual effect, constrains input programmatically
- Values above max are clamped to max when using spinner or validation

**When to use:**
- Set to enforce upper bounds on numeric input
- Spinner controls will not increment above this value
- Validation may show error if value is above max depending on validationMode

## stepValue

Controls the increment/decrement amount when using spinner or mouse wheel.

**Visual cues:**
- No direct visual effect, controls behavior of spinner buttons and mouse wheel
- Combined with modifiers to determine actual step amount

**When to use:**
- Set to 1 for integer inputs (default)
- Set to fractional values for decimal precision (e.g., 0.1, 0.01)
- Larger values for quickly adjusting high-magnitude numbers

## disableSpinner

Controls visibility of the increment/decrement spinner buttons.

**Visual cues:**
- When true: Spinner buttons are hidden, input appears as standard text input
- When false: Spinner buttons appear according to spinner prop (default)

**When to use:**
- Set true when spinner controls are not desired or space is limited
- Keep false (default) when spinner controls improve UX for numeric input
- Overrides spinner prop when set to true

## disableMouseWheel

Controls whether mouse wheel can increment/decrement the value.

**Visual cues:**
- No visual effect, controls behavior when mouse wheel is scrolled over focused input

**When to use:**
- Set true to prevent accidental value changes when scrolling
- Keep false (default) when mouse wheel navigation is convenient
- Works even when spinner controls are disabled or hidden

## disableAutoComplete

Controls whether browser autocomplete suggestions are shown.

**Visual cues:**
- No visual effect, affects browser autocomplete behavior
- Controls the autocomplete HTML attribute on the input element

**When to use:**
- Set true to disable browser autocomplete for sensitive or custom-formatted numbers
- Keep false (default) when browser suggestions are helpful
- Set to "off" on the underlying input when true

## roundingMode

Controls how decimal values are rounded when formatting.

**Visual cues:**
- No visual effect, controls mathematical rounding behavior
- Affects how the formatted value displays decimals

**When to use:**
- none: No explicit rounding, uses default rounding behavior (default)
- default: Rounds to nearest, ties to even (banker's rounding - rounds to 0)
- up: Always rounds towards positive infinity (ceil)
- down: Always rounds towards negative infinity (floor)
- Combined with format prop that specifies decimal places

## focusAction

Controls cursor behavior when the input field receives focus.

**Visual cues:**
- none: No special cursor behavior, cursor position depends on user interaction (default)
- selectAll: Selects all text when field gains focus
- cursorOnTheLeft: Positions cursor at the beginning of the field
- cursorOnTheRight: Positions cursor at the end of the field
- customAction: Triggers customFocusAction event for programmatic control

**When to use:**
- none: Standard behavior, let users control cursor position (default)
- selectAll: When quick replacement of entire value is common
- cursorOnTheLeft: For fields that start from beginning
- cursorOnTheRight: For fields that extend from end
- customAction: When complex cursor positioning logic is needed

## textAlignment

Controls horizontal alignment of the numeric value within the input field.

**Visual cues:**
- left: Numbers aligned to left of field
- center: Numbers centered in field
- right: Numbers aligned to right of field (default for most numerics)

**When to use:**
- Interacts with spinner prop - defaults vary by spinner type
- Left alignment for general-purpose numeric fields
- Center alignment for fields with vertical wrap spinner
- Right alignment for standard numeric inputs (default with default spacer)
- Explicit textAlignment overrides automatic behavior from spinner

## spinner

Controls the style and position of increment/decrement spinner buttons.

**Visual cues:**
- none: No spinner buttons shown
- default: Standard up/down buttons on right side of input (default)
- wrapHorizontal: Increment on right, decrement on left of input
- wrapHorizontalEnd: Both buttons on right side of input
- wrapVertical: Increment on top, decrement on bottom of input

**When to use:**
- none: When spinner controls not needed or space limited
- default: Standard pattern for most numeric inputs (default)
- wrapHorizontal/wrapHorizontalEnd: When horizontal layout is preferred
- wrapVertical: When vertical layout is preferred
- Affects automatic text alignment behavior (see propInteractions)

## format

Controls how numbers are formatted for display using various formatting options.

**Visual cues:**
- none: Displays numbers as-is without formatting (default)
- decimalPlaces: Formats to specified number of decimal places
- locale: Formats according to locale-specific conventions
- CMFmt: Formats using custom formatter from ionweb.cm.Format

**When to use:**
- none: Simple numeric display without additional formatting (default)
- decimalPlaces: Precise control over decimal display (e.g., {decimalPlaces: 2})
- locale: Locale-aware formatting for international users (e.g., {locale: "en-US"})
- CMFmt: Custom formatting using ionweb.cm.Format object (e.g., {CMFmt: someFormat})
- Mutually exclusive with customFormatter/customParser

## enableModifiers

Enables the use of modifier symbols for multiplier shorthand.

**Visual cues:**
- Allows typing suffixes like "k", "M", "B" for thousands, millions, billions
- Modifiers are applied when retainModifiers is also set

**When to use:**
- Set true to enable standard modifiers (k, K, t, T, m, M, b, B, y, Y)
- Keep false (default) when modifiers are not needed or confusing
- Works with retainModifiers to show modifier symbols in display

## retainModifiers

Controls whether modifier symbols are retained in the formatted display.

**Visual cues:**
- When true: Modifiers appear in formatted value (e.g., "100K", "2.5M")
- When false: Modifiers used for input but value displays as full number (default)

**When to use:**
- Set true to show multiplier symbols in the field display
- Keep false (default) when full numeric values are preferred
- Only takes effect when enableModifiers is true or enableCustomModifiers is set

## enableCustomModifiers

Allows definition of custom modifier symbols and their multiplier values.

**Visual cues:**
- Enables custom multiplier symbols beyond standard k/M/B conventions
- Format: { symbol: multiplier } object

**When to use:**
- Define custom business-specific multipliers (e.g., {L: 100000} for lakhs)
- Combined with enableModifiers and retainModifiers for full functionality
- Empty object {} means no custom modifiers defined

## ariaLabel

Provides accessibility label for screen readers and assistive technologies.

**Visual cues:**
- No visual effect, used by screen readers and keyboard navigation

**When to use:**
- Set explicitly when label text is not sufficient for accessibility
- Falls back to label value if ariaLabel not set
- Provides context about the field's purpose to assistive technologies
- For negative numbers, includes minus sign (-) in the aria label

## value

Controls the numeric value of the input field.

**Visual cues:**
- Displays the number according to formatting rules
- Updates display when value changes programmatically or through user input

**When to use:**
- Two-way bind to form state or application state
- When retainModifiers is true, value accepts INumberInputValue object {value: number, modifier?: string}
- Standard number type when retainModifiers is false
- Undefined means field is empty

## defaultValue

Sets the initial value when the component is first rendered.

**Visual cues:**
- Provides initial number displayed in the field on load
- Formatted according to format settings

**When to use:**
- Set to provide initial value when field loads
- Unlike value, does not trigger valueChange on initial render
- Useful for pre-filling form defaults without side effects

## required

Specifies whether the input field is required for form completion.

**Visual cues:**
- When true: Combined with necessityIndicator to show required status
- May trigger validation when validationMode is set appropriately

**When to use:**
- Set true when the field must have a value for submission
- Keep false (default) when field is optional
- Works with validationMode and necessityIndicator for complete UX

## inputMode

Controls the type of virtual keyboard shown on mobile devices.

**Visual cues:**
- No desktop effect, controls mobile keyboard type
- Sets HTML inputmode attribute on the underlying input element

**When to use:**
- text: Full keyboard (default)
- numeric: Number-only keyboard
- decimal: Number keyboard with decimal point
- Optimize for mobile input based on expected number type

## customFormatter

Provides custom number-to-string formatting function.

**Visual cues:**
- Overrides default formatting behavior
- Applied when formatting for display

**When to use:**
- Custom formatting beyond standard format prop options
- Must be paired with customParser
- Example: custom formatted currency, scientific notation, etc.
- Overrides format prop when both are set

## customParser

Provides custom string-to-number parsing function.

**Visual cues:**
- Overrides default parsing behavior
- Applied when user input is converted to numeric value

**When to use:**
- Custom parsing beyond standard format prop options
- Must be paired with customFormatter
- Example: parsing custom-formatted currency, scientific notation, etc.
- Overrides format prop when both are set

## Events

### valueChange

Fires when the numeric value changes through any means: user input, spinner interaction, mouse wheel, or programmatic updates.

**Emitted args:** CustomEvent<{ name: string, value: number | undefined }>

**When to use:**
- React to value changes in real-time
- Update application state when numeric input changes
- Handle user input for form processing
- Track value changes for analytics or validation

**How to use:**
```typescript
onValueChange(event: CustomEvent<{ name: string, value: number | undefined }>) {
    const fieldName = event.detail.name;
    const newValue = event.detail.value;
    // Handle the value change
    console.log(`${fieldName} changed to: ${newValue}`);
}
```

**Binding syntax:**
```html
(ion-number-input (valueChange)="onValueChange($event)"></ion-number-input>
```

### focusIn

Fires when the number input field gains focus.

**Emitted args:** CustomEvent<void>

**When to use:**
- Track when user interacts with the field
- Show contextual help or tooltips when field is focused
- Clear previous validation state on new focus
- Coordinate with other focus-based UI updates

**How to use:**
```typescript
onFocusIn(event: CustomEvent<void>) {
    console.log('Number input field gained focus');
    event.detail is undefined for this event
}
```

**Binding syntax:**
```html
<ion-number-input (focusIn)="onFocusIn($event)"></ion-number-input>
```

### focusOut

Fires when the number input field loses focus, after the value has been committed and validated.

**Emitted args:** CustomEvent<void>

**When to use:**
- Trigger validation when user completes input
- Commit final value to application state
- Dismiss contextual help or tooltips
- Handle blur-based form processing

**How to use:**
```typescript
onFocusOut(event: CustomEvent<void>) {
    console.log('Number input field lost focus, value has been committed');
    event.detail is undefined for this event
}
```

**Binding syntax:**
```html
<ion-number-input (focusOut)="onFocusOut($event)"></ion-number-input>
```

### invalidValueSet

Fires when the user attempts to set an invalid (NaN) value through the component's formatting system.

**Emitted args:** CustomEvent<number>

**When to use:**
- Detect when users enter values that cannot be parsed as numbers
- Provide specific feedback for invalid numeric format
- Log or track input errors for analytics
- Clean up or reset invalid input state

**How to use:**
```typescript
onInvalidValueSet(event: CustomEvent<number>) {
    const invalidValue = event.detail;
    console.error(`Attempted to set invalid value: ${invalidValue}`);
    // Handle invalid value (e.g., reset to previous valid value)
}
```

**Binding syntax:**
```html
<ion-number-input (invalidValueSet)="onInvalidValueSet($event)"></ion-number-input>
```

### customFocusAction

Fires when focusAction is set to 'customAction' and the input field gains focus, allowing programmatic cursor positioning.

**Emitted args:** CustomEvent<{ input: HTMLElement }>

**When to use:**
- Implement complex cursor positioning logic beyond basic options
- Position cursor at specific characters based on field requirements
- Handle focus-based UI enhancements
- Coordinate with other focus handlers

**How to use:**
```typescript
onCustomFocusAction(event: CustomEvent<{ input: HTMLElement }>) {
    const inputElement = event.detail.input;
    const inputLength = inputElement.value.length;
    // Example: Position cursor to select the last digit
    inputElement.setSelectionRange(inputLength - 1, inputLength, 'backward');
    console.log('Custom focus action performed');
}
```

**Binding syntax:**
```html
<ion-number-input focusAction="customAction" (customFocusAction)="onCustomFocusAction($event)"></ion-number-input>
```

### currentInput

Fires on every keystroke and value change, returning the current raw input string before parsing.

**Emitted args:** CustomEvent<string>

**When to use:**
- Track real-time typing for input monitoring
- Implement custom validation on intermediate states
- Provide live character count or format feedback
- Debug input parsing behavior

**How to use:**
```typescript
onCurrentInput(event: CustomEvent<string>) {
    const currentInput = event.detail;
    console.log(`Current input: ${currentInput}`);
    // Monitor or validate intermediate input states
}
```

**Binding syntax:**
```html
<ion-number-input (currentInput)="onCurrentInput($event)"></ion-number-input>
```

### keyDown

Fires on every keyboard event in the input field, including standard input keydown and control keys.

**Emitted args:** CustomEvent<KeyboardEvent>

**When to use:**
- Implement custom keyboard shortcuts (e.g., Ctrl+Enter to submit)
- Intercept or modify keyboard behavior
- Implement keyboard navigation patterns
- Handle special key combinations

**How to use:**
```typescript
onKeyDown(event: CustomEvent<KeyboardEvent>) {
    const keyEvent = event.detail;
    console.log(`Key pressed: ${keyEvent.key}`);
    // Handle specific keyboard shortcuts
    if (keyEvent.key === 'Enter' && keyEvent.ctrlKey) {
        console.log('Ctrl+Enter pressed - submit form');
        // Prevent default behavior and handle submission
        keyEvent.preventDefault();
    }
}
```

**Binding syntax:**
```html
<ion-number-input (keyDown)="onKeyDown($event)"></ion-number-input>
```

### validationStateChange

Fires when the validation state changes dynamically, either through user input, validation triggers, or programmatic changes.

**Emitted args:** CustomEvent<ValidationState>

**When to use:**
- React to validation state changes in real-time
- Update UI based on validation results
- Track validation state for form-level logic
- Show or hide feedback based on state transitions

**How to use:**
```typescript
onValidationStateChange(event: CustomEvent<ValidationState>) {
    const newState = event.detail;
    console.log(`Validation state changed to: ${newState}`);
    // Handle validation state transitions
    if (newState === 'valid') {
        // Field is valid, enable submit or provide positive feedback
    } else if (newState === 'invalid') {
        // Field is invalid, show error or guidance
    }
}
```

**Binding syntax:**
```html
<ion-number-input (validationStateChange)="onValidationStateChange($event)"></ion-number-input>
```

### Complete event binding example

```html
<ion-number-input
    label="Quantity"
    name="quantity"
    [value]="quantity"
    [stepValue]="1"
    [minValue]="0"
    [maxValue]="100"
    (valueChange)="onValueChange($event)"
    (focusIn)="onFocusIn($event)"
    (focusOut)="onFocusOut($event)"
    (invalidValueSet)="onInvalidValueSet($event)"
    (currentInput)="onCurrentInput($event)"
    (keyDown)="onKeyDown($event)"
    (validationStateChange)="onValidationStateChange($event)">
</ion-number-input>
```

```typescript
// Combined handler implementation for all events
export class MyComponent {
    quantity: number = 10;

    onValueChange(event: CustomEvent<{ name: string, value: number | undefined }>) {
        console.log(`Field ${event.detail.name} changed to ${event.detail.value}`);
        this.quantity = event.detail.value as number;
    }

    onFocusIn(event: CustomEvent<void>) {
        console.log('Quantity field focused - show help or clear previous validation');
    }

    onFocusOut(event: CustomEvent<void>) {
        console.log('Quantity field blurred - value committed and validated');
    }

    onInvalidValueSet(event: CustomEvent<number>) {
        console.error(`Invalid value attempt: ${event.detail}`);
        this.quantity = this.quantity || 0; // Reset to last valid value
    }

    onCurrentInput(event: CustomEvent<string>) {
        console.log(`Current input: ${event.detail}`);
        // Monitor typing for validation or feedback
    }

    onKeyDown(event: CustomEvent<KeyboardEvent>) {
        if (event.detail.key === 'Enter' && event.detail.ctrlKey) {
            console.log('Ctrl+Enter pressed - submit form');
            event.detail.preventDefault();
            // Handle form submission
        }
    }

    onValidationStateChange(event: CustomEvent<ValidationState>) {
        console.log(`Validation state: ${event.detail}`);
        // Update UI based on validation state
    }
}
```

## Examples

```html
<ion-number-input label="Label" labelPlacement="vertical" stepValue="1" defaultValue="0"></ion-number-input>
```
Demonstrates basic number input with vertical label placement and default value.

```html
<ion-number-input label="Label" placeholder="Enter number" value="100"></ion-number-input>
```
Demonstrates number input with placeholder text and initial value.

```html
<ion-number-input label="Label" size="sm" defaultValue="0" stepValue="1"></ion-number-input>
<ion-number-input label="Label" size="md" defaultValue="0" stepValue="1"></ion-number-input>
<ion-number-input label="Label" size="lg" defaultValue="0" stepValue="1"></ion-number-input>
```
Demonstrates number input in three sizes: small, medium, and large.

```html
<ion-number-input label="Label" labelPlacement="vertical" helperMessage="Helper Message" helperMessageAsTooltip="false" validationState="valid" defaultValue="0" stepValue="1"></ion-number-input>
<ion-number-input label="Label" labelPlacement="vertical" helperMessage="Invalid Helper Message" helperMessageAsTooltip="false" validationState="invalid" defaultValue="0" stepValue="1"></ion-number-input>
<ion-number-input label="Label" labelPlacement="vertical" helperMessage="Warning Helper Message" helperMessageAsTooltip="false" validationState="warning" defaultValue="0" stepValue="1"></ion-number-input>
```
Demonstrates number input with different validation states and helper messages.

```html
<ion-number-input enableModifiers="false" label="Label" labelPlacement="vertical" defaultValue="0" stepValue="1"></ion-number-input>
<ion-number-input enableModifiers="true" label="Label" labelPlacement="vertical" defaultValue="0" stepValue="1"></ion-number-input>
```
Demonstrates number input with modifiers disabled and enabled.

```html
<ion-number-input spinner="none" label="Label" labelPlacement="vertical" defaultValue="0" stepValue="1"></ion-number-input>
<ion-number-input spinner="default" label="Label" labelPlacement="vertical" defaultValue="0" stepValue="1"></ion-number-input>
<ion-number-input spinner="wrapHorizontal" label="Label" labelPlacement="vertical" defaultValue="0" stepValue="1"></ion-number-input>
<ion-number-input spinner="wrapHorizontalEnd" label="Label" labelPlacement="vertical" defaultValue="0" stepValue="1"></ion-number-input>
<ion-number-input spinner="wrapVertical" label="Label" labelPlacement="vertical" defaultValue="0" stepValue="1"></ion-number-input>
```
Demonstrates number input with different spinner styles: none, default, wrapHorizontal, wrapHorizontalEnd, and wrapVertical.

```html
<ion-number-input disabled="false" label="Label" labelPlacement="vertical" defaultValue="0" stepValue="1"></ion-number-input>
<ion-number-input disabled="true" label="Label" labelPlacement="vertical" defaultValue="0" stepValue="1"></ion-number-input>
```
Demonstrates number input in enabled and disabled states.

```html
<ion-number-input readOnly="false" label="Label" labelPlacement="vertical" defaultValue="0" stepValue="1"></ion-number-input>
<ion-number-input readOnly="true" label="Label" labelPlacement="vertical" defaultValue="0" stepValue="1"></ion-number-input>
```
Demonstrates number input in editable and read-only states.

```html
<div style="width:216px">
    <ion-number-input
        size="medium"
        label="Label"
        labelPlacement="vertical"
        labelAlignment="start"
        required="true"
        necessityIndicator="asterisk"
        autoFocus="false"
        focusAction="none"
        placeholder="Enter number"
        value="undefined"
        defaultValue="0"
        name="quantity"
        stepValue="1"
        format={decimalPlaces: 1}
        roundingMode="default"
        spinner="default"
        minValue="0"
        maxValue="100"
        helperMessage=""
        helperMessageAsTooltip="false"
        validationState="none"
        validationMode="none"
        disabled="false"
        readOnly="false"
        ariaLabel=""
        (valueChange)="onValueChange($event)"
        (customFocusAction)="onFocusInCustomAction($event)"
        (validationStateChange)="onValidationStateChange($event)"
        (keyDown)="onKeyDown($event)">
    </ion-number-input>
</div>
```
Demonstrates fully configured number input with event bindings for value changes, custom focus actions, validation state changes, and keyboard events.