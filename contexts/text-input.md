---
realComponent: ion-text-input
description: Angular standalone text input component with design system styling, validation states, and enhancers support
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
        resolvesTo: "22px"
        tokenChain: "container-inner-height -> --ion-comp-field-container-inner-sizing-height-sm -> calc((var(--ion-cont-sizing-field-sm) - (var(--ion-cont-border-width-field-base)*2))) -> 22px"
        appliesToCssProperty: "height"
      md:
        resolvesTo: "30px"
        tokenChain: "container-inner-height -> --ion-comp-field-container-inner-sizing-height-md -> calc((var(--ion-cont-sizing-field-md) - (var(--ion-cont-border-width-field-base)*2))) -> 30px"
        appliesToCssProperty: "height"
      lg:
        resolvesTo: "38px"
        tokenChain: "container-inner-height -> --ion-comp-field-container-inner-sizing-height-lg -> calc((var(--ion-cont-sizing-field-lg) - (var(--ion-cont-border-width-field-base)*2))) -> 38px"
        appliesToCssProperty: "height"

  - name: disabled
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}

  - name: readOnly
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
    default: none found
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
    default: none found
    values: []
    designTokens: {}

  - name: placeholder
    type: string
    category: content
    required: false
    default: none found
    values: []
    designTokens: {}

  - name: value
    type: string
    category: content
    required: false
    default: none found
    values: []
    designTokens: {}

  - name: defaultValue
    type: string
    category: content
    required: false
    default: none found
    values: []
    designTokens: {}

  - name: helperMessage
    type: string
    category: content
    required: false
    default: none found
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
    values: [none, valid, invalid, warning]
    designTokens:
      invalid:
        light:
          resolvesTo: "#c70000"
          tokenChain: "validation text -> --ion-lit-color-leonardo-base-negative (#c70000)"
          appliesToCssProperty: "color"
      valid:
        light:
          resolvesTo: "#2dc168"
          tokenChain: "validation text -> --ion-lit-color-leonardo-base-positive (#2dc168)"
          appliesToCssProperty: "color"
      warning:
        light:
          resolvesTo: "#fe7f2a"
          tokenChain: "validation text -> --ion-lit-color-leonardo-base-warning (#fe7f2a)"
          appliesToCssProperty: "color"

  - name: validationMode
    type: enum
    category: behavioral
    required: false
    default: "none"
    values: [none, onChange, onBlur, onSubmit]
    designTokens: {}

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
    designTokens: {}

  - name: startEnhancer
    type: object
    category: visual
    required: false
    default: none found
    values: []
    designTokens: {}

  - name: endEnhancer
    type: object
    category: visual
    required: false
    default: none found
    values: []
    designTokens: {}

  - name: clearButton
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}

  - name: type
    type: enum
    category: visual
    required: false
    default: "text"
    values: [text, email, url, tel]
    designTokens: {}

  - name: pattern
    type: string
    category: behavioral
    required: false
    default: none found
    values: []
    designTokens: {}

  - name: minLength
    type: number
    category: behavioral
    required: false
    default: none found
    values: []
    designTokens: {}

  - name: maxLength
    type: number
    category: behavioral
    required: false
    default: none found
    values: []
    designTokens: {}

  - name: showCount
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}

  - name: tabIndex
    type: number
    category: accessibility
    required: false
    default: 0
    values: []
    designTokens: {}

  - name: selectTextOnFocus
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

  - name: disableAutoComplete
    type: boolean
    category: behavioral
    required: false
    default: false
    values: []
    designTokens: {}

  - name: name
    type: string
    category: behavioral
    required: false
    default: none found
    values: []
    designTokens: {}

  - name: inputMode
    type: string
    category: behavioral
    required: false
    default: none found
    values: []
    designTokens: {}

  - name: ariaLabel
    type: string
    category: accessibility
    required: false
    default: none found
    values: []
    designTokens: {}

  - name: focus
    type: function
    category: behavioral
    required: false
    default: "() => this.inputElement.nativeElement.focus()"
    values: []
    designTokens: {}

  - name: reset
    type: function
    category: behavioral
    required: false
    default: "() => { Object.assign(this, this.initialProperties); }"
    values: []
    designTokens: {}

jointTokens: []

propInteractions:
  - "labelAlignment only applies when labelPlacement is horizontal"
  - "labelWidth only applies when labelPlacement is horizontal"
  - "showCount only displays meaningful information when maxLength is set"
  - "validationMode controls when validation runs and helperMessage updates with validation errors"
  - "helperMessage is replaced by browser validation message when validationState becomes invalid"
  - "helperMessageAsTooltip changes helperMessage display from inline to tooltip"
  - "clearButton appears at end of input and can be combined with endEnhancer"
  - "startEnhancer and endEnhancer objects support type (text/icon/icon-button), value, and optional properties"
  - "maxLength set to -1 or invalid values indicates no maximum length limit"
  - "minLength and maxLength minimum values enforced to be at least 1; invalid values set to -1"
  - "value prop truncates to maxLength if maxLength property is set"
  - "defaultValue only applies during ngAfterViewInit when value is not already set"
  - "necessityIndicator works independently of required prop and affects aria label generation"
  - "inputMode prop is not documented/exposed to applications per source comments"
  - "size prop parsed by MqDesignStringParserService for responsive design strings"
  - "ariaLabel uses label value as fallback, adds ' optional' when necessityIndicator is optionalLabel"
  - "validationState=invalid sets aria-invalid attribute to true"
  - "validationMode determines when validation is triggered (onChange, onBlur, onSubmit)"
  - "selectTextOnFocus uses setTimeout with 0ms to select text after focus is gained"

needsReview:
  - "Dark theme validation state color tokens not traced - only light theme base colors found for invalid (#c70000), valid (#2dc168), warning (#fe7f2a)"
  - "Enhancer color tokens not traced from ds_tokens.css for startEnhancer and endEnhancer"
  - "Size-specific design tokens (padding, font-size) not fully traced for sm/md/lg values"
  - "Helper message color tokens not traced for none/valid/invalid/warning states"
  - "Input field border and background color tokens not traced for enabled/disabled/focus states"
  - "Text color tokens not traced for enabled/disabled states in light and dark themes"
  - "Tooltip design tokens not traced for helperMessageAsTooltip functionality"
  - "Focus ring and outline color tokens not traced for accessibility focus states"
  - "Enhancer size and positioning tokens not traced relative to input field size"
  - "Cross-theme verification needed for all color tokens (only light theme traced)"
  - "MQ design string parsing behavior cannot be verified without runtime screen size context"
  - "Character count display styling tokens not traced from ds_tokens.css"
  - "enhancer type 'icon-button' click event styling and token chain not traced"
  - "Placeholder text color tokens not traced from ds_tokens.css"
  - "Disabled state color tokens (text, border, background) not traced for all validation states"
  - "Read-only state visual cues and color tokens not traced from ds_tokens.css"

---

## Usage Notes

Boolean props on this component must always be passed with an explicit string value — e.g. `disabled="true"` or `[disabled]="isDisabled"` — never as bare attribute presence (e.g. `disabled` alone, with no value). Bare attribute presence is a native HTML convention this component does NOT support; it will not be interpreted as true.

## size

Controls text input sizing both through direct size values and responsive MQ design strings. Supports sm, md, lg values parsed by MqDesignStringParserService.

**Visual cues:**
- sm: Small input with 24px container height, compact sizing (22px inner height)
- md: Medium input with 32px container height, standard sizing (30px inner height)
- lg: Large input with 40px container height, prominent sizing (38px inner height)
- Supports MQ design strings like 'xs=sm;sm=md;md=md;lg=lg' for responsive behavior

**When to use:**
- sm: Compact forms, data tables, space-constrained layouts
- md: Standard form fields, primary user input areas (default)
- lg: Prominent input areas, search fields, when extra visibility needed
- MQ strings: Responsive layouts where input size should adapt to screen size

**Responsive behavior:**
- Returns default 'md' if invalid size string or empty string provided
- Parsed by MqDesignStringParserService.parseDesignStringForCurrentScreenSize()
- Component size class updated as 'ion-ds-{parsedSize}'

## disabled

Controls disabled state of the text input, preventing interaction and Changing visual appearance.

**Visual cues:**
- When true: Input appears non-interactive with reduced opacity, disabled cursor
- Applies 'ion-ds-disabled' CSS class
- Prevents all user input and interaction

**When to use:**
- Set true when input field should be read-only but still visible
- Disable during operations that require user to wait
- Override default false when form permissions or validation-state require disabling

## readOnly

Controls whether the text input is read-only but still focusable and interactive.

**Visual cues:**
- When true: Input appears non-editable but can be focused and copied from
- Applies 'ion-ds-read-only' CSS class
- Allows text selection and copying but prevents editing

**When to use:**
- Set true for data display that should be viewable but not modifiable
- Use for calculated or derived values that should not be edited
- Different from disabled as read-only fields can still be focused and interacted with

## label

Controls the text label displayed above (vertical) or beside (horizontal) the input field.

**Visual cues:**
- When set: Displays label text with styling based on labelPlacement property
- When empty: Input field renders without visible label
- Label positioning controlled by labelPlacement property

**When to use:**
- Primary method for identifying input purpose to users
- Should be omitted for purely decorative or unlabeled inputs
- Used as fallback for ariaLabel if not explicitly set

## labelPlacement

Controls the position of the label relative to the input field.

**Visual cues:**
- vertical: Label appears above the input field (default)
- horizontal: Label appears beside the input field, to the left

**When to use:**
- vertical: Standard form layout, most commonly used
- horizontal: Compact layouts, data grids, when horizontal space is available
- When horizontal, labelAlignment and labelWidth properties become relevant

## labelAlignment

Controls alignment of the label relative to the input field when labelPlacement is horizontal.

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
- Useful for form alignment when multiple horizontal label inputs are stacked
- Only applicable when labelPlacement is set to horizontal

## placeholder

Controls placeholder text displayed when input is empty.

**Visual cues:**
- When set: Displays placeholder text in empty input field
- When empty: Input field shows no placeholder
- Placeholder text typically appears in lighter color than input text

**When to use:**
- Provide hints about expected input format or content
- Show example values to guide user input
- Should not be used as substitute for proper label

## value

Controls the current value of the text input field.

**Visual cues:**
- When set: Input field displays the specified value
- Updates to this prop will update the displayed value
- Value changes trigger valueChange event emission

**When to use:**
- Set programmatically to populate input with initial or updated data
- Empty string clears the input field
- Truncates to maxLength if maxLength property is set

## defaultValue

Controls default value that is set only during component initialization.

**Visual cues:**
- When set and no value prop provided: Input displays default value on initialization
- Only applied when value prop is not set during ngAfterViewInit lifecycle hook
- Does not update input if value prop is already set

**When to use:**
- Provide initial value when component first renders
- Use when you need a default but want value prop to take precedence if set
- Different from value as it only applies during initialization, not updates

## helperMessage

Controls helper/explanatory message displayed below the input field. Can also serve as validation message when validationState changes.

**Visual cues:**
- When set: Displays helper message text below input field
- When empty: No helper message displayed
- Replaced by browser validation message when validationState is set to invalid
- Can be displayed as tooltip when helperMessageAsTooltip is true

**When to use:**
- Provide helpful guidance about input requirements or format
- Display dynamic validation messages based on validationState
- Show contextual information about the input field

## helperMessageAsTooltip

Controls whether helper message is displayed as tooltip instead of inline text.

**Visual cues:**
- When true: Helper message appears as tooltip on hover/focus
- When false: Helper message displayed inline below input (default)

**When to use:**
- Set true when space is limited or for cleaner UI
- Keep false for immediate visibility of helper content
- Can be combined with tooltipPlacement prop for positioning control

## validationState

Controls validation state of the text input, affecting visual appearance and helper message handling.

**Visual cues:**
- none: Default state, no visual validation indicators
- valid: Green color scheme (#2dc168), indicates successful validation
- invalid: Red color scheme (#c70000), indicates validation failure
- warning: Orange/amber color scheme (#fe7f2a), indicates caution state
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
- onBlur: Validation runs when input loses focus
- onSubmit: Validation runs when form is submitted

**When to use:**
- none: Manual validation control or no validation needed
- onChange: Real-time validation feedback as user types
- onBlur: Validation feedback after user completes input field
- onSubmit: Validation runs as part of form submission process

## required

Controls whether the input field is marked as required, affecting necessityIndicator display and form validation.

**Visual cues:**
- When true: Input marked as required, affects necessityIndicator display
- Sets required attribute on input element for browser validation
- Triggers browser validation when form submitted if empty

**When to use:**
- Set true for required form fields that must be filled
- Combined with necessityIndicator prop to show visual indicator
- Override default false for fields that are optional

## necessityIndicator

Controls the visual indicator for field requirement status.

**Visual cues:**
- requiredMarker: Asterisk (*) symbol displayed with label (default)
- requiredLabel: Text 'Required' displayed with label
- optionalLabel: Text 'Optional' displayed with label
- none: No requirement indicator displayed

**When to use:**
- requiredMarker: Standard pattern for required fields with label
- requiredLabel: More explicit text indication for required fields
- optionalLabel: Explicitly mark optional fields for clarity
- none: Hide requirement indicators, useful when context is clear

**Interaction with required:**
- Works independently of required prop - can show optionalLabel even when required=true
- Affects aria label generation when value is optionalLabel

## startEnhancer

Controls content displayed at the start (left) of the input field. Accepts object with type and value properties.

**Visual cues:**
- Text enhancer: Displays text string at start of input
- Icon enhancer: Displays icon at start of input
- Enhancer size scales based on the size prop (sm/md/lg)

**When to use:**
- Text enhancer: Add prefixes like country codes (+91) or currencies ($)
- Icon enhancer: Add contextual icons for input type identification
- Used to visually indicate input format or content type

**Enhancer interface:**
- type: "text | icon"
- value: "string"
- iconFontFamily: "string (optional, for custom icons)"
- iconColor: "IconColor (optional, from ion-palette)"
- ariaLabel: "string (optional, for text/icon enhancer significance)"

## endEnhancer

Controls content displayed at the end (right) of the input field. Accepts object with type, value, and optional properties.

**Visual cues:**
- Text enhancer: Displays text string at end of input
- Icon enhancer: Displays icon at end of input
- Icon-button enhancer: Displays interactive icon button at end of input
- Enhancer size scales based on the size prop (sm/md/lg)
- endEnhancerButtonClick event fired for icon-button type

**When to use:**
- Text enhancer: Add suffixes like units, domains, or other contextual text
- Icon enhancer: Add status icons or visual indicators
- Icon-button enhancer: Add interactive actions like password toggle, search trigger
- Combined with clearButton prop for additional end content

**Enhancer interface:**
- type: "text | icon | icon-button"
- value: "string"
- iconFontFamily: "string (optional, for custom icons)"
- iconColor: "IconColor (optional, from ion-palette)"
- ariaLabel: "string (optional, for button accessibility)"

## clearButton

Controls visibility of clear button that allows users to quickly clear input value.

**Visual cues:**
- When true: Clear ('x') button appears at end of input when value present
- When false: No clear button displayed (default)
- Clear button appears/disappears based on whether input has value

**When to use:**
- Set true for input fields that users frequently clear
- Useful in search fields, filters, and data input
- Can be combined with endEnhancer prop

## type

Controls the HTML5 input type, affecting keyboard layout and browser validation on mobile devices.

**Visual cues:**
- text: Standard text input (default)
- email: Email-specific keyboard, validates email format
- url: URL-specific keyboard, validates URL format
- tel: Telephone keypad, optimized for phone number input

**When to use:**
- text: Default for general text input
- email: Email address input fields
- url: Website URL or link input fields
- tel: Phone number or numeric input designed for phone entry

## pattern

Controls regular expression pattern for input validation. Used by browser validation system.

**Visual cues:**
- When set and validationMode is active: Input validated against pattern
- Invalid pattern triggers browser validation message and invalid state
- No visual indicator until validation runs

**When to use:**
- Set when input must match specific format (e.g., phone numbers, postal codes)
- Combine with validationMode prop for validation timing
- Regex pattern should be compatible with browser's pattern validation

## minLength

Controls minimum character length allowed for input. Used by browser validation.

**Visual cues:**
- When set: Input must contain at least this many characters to be valid
- Invalid length triggers browser validation message and invalid state
- Can be combined with showCount to display character count
- Minimum value enforced to be at least 1; invalid values set to -1

**When to use:**
- Set when input requires minimum number of characters
- Useful for passwords, usernames, or data with length requirements
- Combine with maxLength for range constraints

## maxLength

Controls maximum character length allowed for input. Prevents typing beyond limit.

**Visual cues:**
- When set: Input truncates if value exceeds maxLength
- Prevents typing beyond specified character limit
- Can be combined with showCount to display character count
- Minimum value enforced to be at least 1; invalid values set to -1
- Value of -1 indicates no maximum length limit

**When to use:**
- Set when input should not exceed character limit
- Useful for database field constraints, message limits
- Combine with minLength for range constraints

## showCount

Controls visibility of character count display showing current length vs max length.

**Visual cues:**
- When true: Displays character count (current/maxLength) at end of input
- When false: No character count displayed (default)
- Updates dynamically as user types
- Only meaningful when maxLength is set

**When to use:**
- Set true when it helps user to know remaining characters
- Useful for message fields, data entry with limits
- Should be combined with maxLength prop for meaningful display

## tabIndex

Controls tab index for keyboard navigation order in the form.

**Visual cues:**
- Affects order in which fields receive focus when tabbing through page
- Default (0): Part of natural tab order
- Negative values: Removed from tab order
- Positive values: Custom tab order (not recommended)

**When to use:**
- Generally should be left at default (0) for natural tab order
- Override only when specific tab sequence is required

## selectTextOnFocus

Controls whether text content is automatically selected when input receives focus.

**Visual cues:**
- When true: All text in input selected when input receives focus
- When false: Text not selected on focus (default)
- Makes it easy for user to replace entire content

**When to use:**
- Set true when users often replace entire input value
- Useful for search fields, data entry with replacement patterns
- Not suitable when users typically append to existing content

## autoFocus

Controls whether input automatically receives focus when page or component loads.

**Visual cues:**
- When true: Input receives focus and keyboard on page load
- When false: Input does not auto-focus (default)
- Scrolls page to input if necessary

**When to use:**
- Set true for primary input field on page when immediate input expected
- Useful for search pages, login forms, primary data entry
- Be cautious with this as it can interfere with page navigation

## disableAutoComplete

Controls whether browser's autocomplete functionality is disabled for this input.

**Visual cues:**
- When true: Browser autocomplete is disabled
- When false: Browser autocomplete is enabled (default, sets autocomplete='on')

**When to use:**
- Set true for sensitive inputs like passwords, security codes
- Use for fields where autocomplete suggestions are not appropriate
- Keep false for convenience in standard data entry fields

## name

Controls the name attribute of the input element, used for form submission and identification.

**Visual cues:**
- Not directly visible to users
- Used in form data submission and Validation referencing
- Emitted with valueChange events as field identifier

**When to use:**
- Set for all input fields in forms to properly submit form data
- Required for proper form validation and submission
- Helps identify fields in event handlers and backend processing

## inputMode

Controls the HTML5 inputmode attribute, affecting on-screen keyboard type on mobile devices.

**Visual cues:**
- Not visible on desktop devices
- Affects mobile virtual keyboard layout and behavior

**When to use:**
- Use when you need different keyboard than type prop provides
- Typically used for special input modes not covered by standard HTML input types
- Comment indicates this is used for login page OTP fields

**Note:**
- Not documented/exposed to applications per source comments

## ariaLabel

Provides accessibility label for screen readers. Falls back to label if not set.

**Visual cues:**
- Not visible to sighted users
- Read by screen readers to identify the input
- Combined with necessityIndicator text for optional fields

**When to use:**
- Set when different from visible label for accessibility
- Use when you need more descriptive label for screen readers
- Leave empty if label prop provides sufficient description

**Fallback behavior:**
- Uses label value if ariaLabel not set
- Adds ' optional' suffix when necessityIndicator is 'optionalLabel'

## focus

Programmatic focus function to set focus to the input element.

**Visual property:** none (behavioral)

**When to use:**
- This is a behavioral prop not derivable from visual design
- Should generally be left at its default unless specifically called
- Used to programmatically trigger input field focus
- Useful for keyboard navigation, error handling, form logic

## reset

Programmatic reset function to restore input to its initial properties and value.

**Visual property:** none (behavioral)

**When to use:**
- This is a behavioral prop not derivable from visual design
- Should generally be left at its default unless specifically called
- Restores all props to values stored during ngOnInit lifecycle hook
- Used to reset form fields to initial state

## Examples

```html
<ion-text-input label="Label" labelPlacement="vertical" size="md"></ion-text-input>
```
Demonstrates default text input with label and medium size.

```html
<ion-text-input label="Label" labelPlacement="horizontal" labelAlignment="start" labelWidth="120px" size="md"></ion-text-input>
```
Demonstrates horizontal label layout with start alignment and specified width.

```html
<ion-text-input label="Label" size="sm" helperMessage="Helper Message" showCount="true" maxLength="10"></ion-text-input>
```
Demonstrates small input with helper message and character counter.

```html
<ion-text-input label="Label" placeholder="Placeholder" startEnhancer="{ type: 'icon', value: 'placeholder' }"></ion-text-input>
```
Demonstrates input with icon start enhancer.

```html
<ion-text-input label="Label" placeholder="Placeholder" endEnhancer="{ type: 'icon', value: 'placeholder' }"></ion-text-input>
```
Demonstrates input with icon end enhancer.

```html
<ion-text-input label="Label" placeholder="Placeholder" endEnhancer="{ type: 'icon-button', value: 'lock_filled' }"></ion-text-input>
```
Demonstrates input with interactive icon-button end enhancer.

```html
<ion-text-input label="Label" defaultValue="Value" clearButton="true"></ion-text-input>
```
Demonstrates input with default value and clear button visibility.

```html
<ion-text-input label="Label" helperMessage="Valid Helper Message" validationState="valid"></ion-text-input>
```
Demonstrates valid validation state with green helper message.

```html
<ion-text-input label="Label" helperMessage="Invalid Helper Message" validationState="invalid"></ion-text-input>
```
Demonstrates invalid validation state with red helper message.

```html
<ion-text-input label="Label" helperMessage="Warning Helper Message" validationState="warning"></ion-text-input>
```
Demonstrates warning validation state with amber helper message.

```html
<ion-text-input label="Label" required="true" necessityIndicator="requiredMarker"></ion-text-input>
```
Demonstrates required field with asterisk indicator.

```html
<ion-text-input label="Label" pattern=".{8,}" validationMode="onBlur"></ion-text-input>
```
Demonstrates pattern validation triggered on blur.
