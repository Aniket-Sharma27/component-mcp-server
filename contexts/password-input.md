---
realComponent: "ion-password-input"
description: Angular standalone password input component with design system styling, validation states, and visibility toggle support
themes: [modern-light-ds, modern-dark-ds]
props:
  - name: size
    type: string
    category: visual
    required: false
    default: ""
    values: [sm, md, lg]
    designTokens:
      sm:
        resolvesTo: "22px"
        tokenChain: "container-inner-height -> --ion-comp-field-container-sizing-height-sm -> calc((var(--ion-cont-sizing-field-sm) - (var(--ion-cont-border-width-field-base)*2))) -> 22px"
        appliesToCssProperty: "height"
      md:
        resolvesTo: "30px"
        tokenChain: "container-inner-height -> --ion-comp-field-container-sizing-height-md -> calc((var(--ion-cont-sizing-field-md) - (var(--ion-cont-border-width-field-base)*2))) -> 30px"
        appliesToCssProperty: "height"
      lg:
        resolvesTo: "38px"
        tokenChain: "container-inner-height -> --ion-comp-field-container-sizing-height-lg -> calc((var(--ion-cont-sizing-field-lg) - (var(--ion-cont-border-width-field-base)*2))) -> 38px"
        appliesToCssProperty: "height"

  - name: disabled
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens:
      light:
        resolvesTo: "rgba(0, 0, 0, 0.04)"
        tokenChain: "field-background -> --ion-comp-field-container-color-bg-disabled -> var(--ion-lit-opacity-300)"
        appliesToCssProperty: "background-color"
      dark:
        resolvesTo: "rgba(255, 255, 255, 0.04)"
        tokenChain: "field-background -> --ion-comp-field-container-color-bg-disabled -> var(--ion-lit-opacity-300)"
        appliesToCssProperty: "background-color"

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

  - name: necessityIndicator
    type: enum
    category: visual
    required: false
    default: "requiredMarker"
    values: [requiredMarker, requiredLabel, none]
    designTokens: {}

  - name: placeholder
    type: string
    category: content
    required: false
    default: none found
    values: []
    designTokens:
      light:
        resolvesTo: "#838993"
        tokenChain: "placeholder-text -> --ion-comp-field-text-inputted-color-fg-enabled -> var(--ion-cont-color-role-light-text-icon-500) -> #838993"
        appliesToCssProperty: "color"
      dark:
        resolvesTo: "#838993"
        tokenChain: "placeholder-text -> --ion-comp-field-text-inputted-color-fg-enabled -> var(--ion-cont-color-role-dark-text-icon-700) -> #838993"
        appliesToCssProperty: "color"

  - name: value
    type: string
    category: content
    required: false
    default: ""
    values: []
    designTokens: {}

  - name: visibilityButton
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}

  - name: helperMessage
    type: string
    category: content
    required: false
    default: none found
    values: []
    designTokens:
      invalid:
        light:
          resolvesTo: "#c70000"
          tokenChain: "validation message -> --ion-lit-color-leonardo-base-negative -> #c70000"
          appliesToCssProperty: "color"
      valid:
        light:
          resolvesTo: "#2dc168"
          tokenChain: "validation message -> --ion-lit-color-leonardo-base-positive -> #2dc168"
          appliesToCssProperty: "color"

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
    values: [none, valid, invalid]
    designTokens:
      invalid:
        light:
          resolvesTo: "#c70000"
          tokenChain: "validation border -> --ion-comp-field-container-color-border-invalid -> var(--ion-lit-color-leonardo-base-negative) -> #c70000"
          appliesToCssProperty: "border-color"
      valid:
        light:
          resolvesTo: "#2dc168"
          tokenChain: "validation border -> --ion-comp-field-container-color-border-valid -> var(--ion-lit-color-leonardo-base-positive) -> #2dc168"
          appliesToCssProperty: "border-color"
      none:
        light:
          resolvesTo: "rgba(0, 0, 0, 0.2)"
          tokenChain: "default border -> --ion-comp-field-container-color-border-enabled -> var(--ion-lit-color-leonardo-base-neutral) -> var(--ion-lit-color-palette-light-navy-300) -> #c4c7cb"
          appliesToCssProperty: "border-color"

  - name: validationMode
    type: enum
    category: behavioral
    required: false
    default: "none"
    values: [none, onChange, onBlur, onSubmit]
    designTokens: {}

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
    default: "() => this.inputElement?.nativeElement.focus()"
    values: []
    designTokens: {}

jointTokens: []

propInteractions:
  - "labelAlignment only applies when labelPlacement is horizontal"
  - "labelWidth only applies when labelPlacement is horizontal"
  - "validationMode controls when validation runs and helperMessage updates with validation errors"
  - "helperMessage is replaced by browser validation message when validationState becomes invalid"
  - "helperMessageAsTooltip changes helperMessage display from inline to tooltip"
  - "visibilityButton enables password toggle with eye icon as end enhancer"
  - "size prop parsed by MqDesignStringParserService for responsive design strings"
  - "ariaLabel uses label value as fallback if not explicitly set"
  - "validationState=invalid sets aria-invalid attribute to true"
  - "validationMode determines when validation is triggered (onChange, onBlur, onSubmit)"
  - "necessityIndicator works independently and affects aria label generation"
  - "visibilityButton toggles between visibility_filled and visibility_off_filled icons"
  - "endEnhancerButtonClick event fired when visibility button clicked"

events:
  - name: valueChange
    payloadType: "CustomEvent<{ name: string, value: string }>"
    firesWhen: "Fires on every input change when the user types or modifies the password value"
    bindingSyntax: "(valueChange)=\"onValueChange($event)\""
    emittedArgs: "CustomEvent with IPasswordInputValueChangeEventArgs wrapped in event.detail"
    usageNote: "Access the payload via event.detail.name and event.detail.value (web element pattern)"
  - name: focusIn
    payloadType: "CustomEvent<void>"
    firesWhen: "Fires when the input field receives focus"
    bindingSyntax: "(focusIn)=\"onFocusIn()\""
    emittedArgs: "CustomEvent with void payload (web element pattern)"
    usageNote: "$event parameter contains the CustomEvent object, though no meaningful data is emitted"
  - name: focusOut
    payloadType: "CustomEvent<void>"
    firesWhen: "Fires when the input field loses focus, and validation runs if validationMode is onBlur"
    bindingSyntax: "(focusOut)=\"onFocusOut()\""
    emittedArgs: "CustomEvent with void payload (web element pattern)"
    usageNote: "$event parameter contains the CustomEvent object, though no meaningful data is emitted"
  - name: endEnhancerButtonClick
    payloadType: "CustomEvent<void>"
    firesWhen: "Fires when the visibility button (eye icon) is clicked to toggle password visibility"
    bindingSyntax: "(endEnhancerButtonClick)=\"onEndEnhancerButtonClick()\""
    emittedArgs: "CustomEvent with void payload (web element pattern)"
    usageNote: "$event parameter contains the CustomEvent object, though no meaningful data is emitted"
  - name: validationStateChange
    payloadType: "CustomEvent<\"valid\" | \"invalid\" | \"none\">"
    firesWhen: "Fires whenever the validationState property changes (none, valid, or invalid)"
    bindingSyntax: "(validationStateChange)=\"onValidationStateChange($event)\""
    emittedArgs: "CustomEvent with ValidationState string wrapped in event.detail"
    usageNote: "Access the validation state via event.detail (web element pattern)"

needsReview:
  - "Dark theme validationState color tokens not traced: validationState=invalid (#c70000 in light), validationState=valid (#2dc168 in light), and validationState=none border colors all lack dark-theme-specific token verification"
  - "Enum props labelPlacement, labelAlignment, necessityIndicator, and validationMode have no designTokens entries - these are layout/behavior props with no direct token mapping, which is intentionally the case"
  - "Dark theme placeholder color not traced - only light theme traced (#838993)"
  - "Size-specific design tokens (padding, font-size, border-radius) not fully traced for sm/md/lg values"
  - "Helper message color tokens not traced for 'none' validation state"
  - "Input field border and background color tokens not traced for enabled/disabled/focus states in both themes"
  - "Text color tokens not traced for enabled/disabled states in light and dark themes"
  - "Tooltip design tokens not traced for helperMessageAsTooltip functionality"
  - "Focus ring and outline color tokens not traced for accessibility focus states"
  - "Visibility button icon size and color tokens not traced from ds_tokens.css"
  - "Cross-theme verification needed for all color tokens (only light theme traced for most)"
  - "MQ design string parsing behavior cannot be verified without runtime screen size context"
  - "Validation state hover colors not traced for invalid-hover and valid-hover states"
  - "Container background color tokens not traced for disabled and read-only states"
  - "Enhancer icon color tokens not traced for visibility button in enabled/disabled states"
  - "Field container sizing tokens (min-width) not traced for sm/md/lg sizes"
  - "Field container gap (spacing) tokens not traced for sm/md/lg sizes"
  - "Field container border-radius tokens not traced for all size variants"
---

## Usage Notes

Boolean props on this component must always be passed with an explicit string value — e.g. `disabled="true"` or `[disabled]="isDisabled"` — never as bare attribute presence (e.g. `disabled` alone, with no value). Bare attribute presence is a native HTML convention this component does NOT support; it will not be interpreted as true.

## size

Controls password input sizing both through direct size values and responsive MQ design strings. Supports sm, md, lg values parsed by MqDesignStringParserService.

**Visual cues:**
- sm: Small input with 24px container height, compact sizing (22px inner height)
- md: Medium input with 32px container height, standard sizing (30px inner height) 
- lg: Large input with 40px container height, prominent sizing (38px inner height)
- Supports MQ design strings like 'xs=sm;sm=md;md=md;lg=lg' for responsive behavior

**When to use:**
- sm: Compact forms, data tables, space-constrained layouts
- md: Standard form fields, primary user input areas (default)
- lg: Prominent input areas, when extra visibility needed
- MQ strings: Responsive layouts where input size should adapt to screen size

**Responsive behavior:**
- Returns default 'md' if invalid size string or empty string provided
- Parsed by MqDesignStringParserService.parseDesignStringForCurrentScreenSize()
- Component size class updated as 'ion-ds-{parsedSize}'

## disabled

Controls disabled state of the password input, preventing interaction and changing visual appearance.

**Visual cues:**
- When true: Input appears non-interactive with reduced opacity background, disabled cursor
- Applies 'ion-ds-disabled' CSS class
- Prevents all user input and interaction

**When to use:**
- Set true when input field should be read-only but still visible
- Disable during operations that require user to wait
- Override default false when form permissions or validation-state require disabling

## readOnly

Controls whether the password input is read-only but still focusable and interactive.

**Visual cues:**
- When true: Input appears non-editable but can be focused and copied from
- Applies 'ion-ds-read-only' CSS class
- Allows text selection and copying but prevents editing

**When to use:**
- Set true for data display that should be viewable but not modifiable
- Use for calculated or derived values that should not be edited
- Different from disabled as read-only fields can still be focused and interacted with

## label

Controls the text label displayed above (vertical) or beside (horizontal) the password input field.

**Visual cues:**
- When set: Displays label text with styling based on labelPlacement property
- When empty: Input field renders without visible label
- Label positioning controlled by labelPlacement property

**When to use:**
- Primary method for identifying input purpose to users
- Should be omitted for purely decorative or unlabeled inputs
- Used as fallback for ariaLabel if not explicitly set

## labelPlacement

Controls the position of the label relative to the password input field.

**Visual cues:**
- vertical: Label appears above the input field (default)
- horizontal: Label appears beside the input field, to the left

**When to use:**
- vertical: Standard form layout, most commonly used
- horizontal: Compact layouts, data grids, when horizontal space is available
- When horizontal, labelAlignment and labelWidth properties become relevant

## labelAlignment

Controls alignment of the label relative to the password input field when labelPlacement is horizontal.

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

## necessityIndicator

Controls the visual indicator for field requirement status.

**Visual cues:**
- requiredMarker: Asterisk (*) symbol displayed with label (default)
- requiredLabel: Text 'Required' displayed with label
- none: No requirement indicator displayed

**When to use:**
- requiredMarker: Standard pattern for required fields with label
- requiredLabel: More explicit text indication for required fields
- none: Hide requirement indicators, useful when context is clear
- Password input is always required by default (required attribute hardcoded in HTML)

## placeholder

Controls placeholder text displayed when password input is empty.

**Visual cues:**
- When set: Displays placeholder text in empty password field
- When empty: Password field shows no placeholder
- Placeholder text appears in lighter color (#838993) in light theme

**When to use:**
- Provide hints about expected password requirements or format
- Show example values to guide user input
- Should not be used as substitute for proper label

## value

Controls the current value of the password input field.

**Visual cues:**
- When set: Password field displays masked characters or visible characters if visibilityButton enabled
- Updates to this prop will update the displayed value
- Value changes trigger valueChange event emission

**When to use:**
- Set programmatically to populate input with initial or updated data
- Empty string clears the password field
- For security, password values should typically be cleared after form submission

## visibilityButton

Controls visibility of password toggle button that allows users to show/hide password characters.

**Visual cues:**
- When true: Eye icon (visibility_filled) appears at end of input to show password visibility toggle
- When false: No visibility button displayed (default)
- Icon toggles between visibility_filled (show password) and visibility_off_filled (hide password)

**When to use:**
- Set true when users need to verify their password input
- Useful for password creation forms, account settings
- Especially helpful when password complexity requirements need verification

## helperMessage

Controls helper/explanatory message displayed below the password input. Can also serve as validation message when validationState changes.

**Visual cues:**
- When set: Displays helper message text below password field
- When empty: No helper message displayed
- Replaced by browser validation message when validationState is set to invalid
- Can be displayed as tooltip when helperMessageAsTooltip is true
- Validation states have specific colors: invalid (#c70000 red), valid (#2dc168 green) in light theme

**When to use:**
- Provide helpful guidance about password requirements or format
- Display dynamic validation messages based on validationState
- Show contextual information about password complexity requirements

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

Controls validation state of the password input, affecting visual appearance and helper message handling.

**Visual cues:**
- none: Default state, no visual validation indicators, subtle border (#c4c7cb)
- valid: Green color scheme (#2dc168), indicates successful validation
- invalid: Red color scheme (#c70000), indicates validation failure
- Sets aria-invalid attribute to true for invalid state
- Affects container border color and helper message color

**When to use:**
- none: Default state when no validation is needed
- valid: Display successful validation status
- invalid: Show error state and browser validation message

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
- onBlur: Validation feedback after user completes password field
- onSubmit: Validation runs as part of form submission process

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

## autoFocus

Controls whether input automatically receives focus when page or component loads.

**Visual cues:**
- When true: Input receives focus and keyboard on page load
- When false: Input does not auto-focus (default)
- Scrolls page to input if necessary

**When to use:**
- Set true for primary input field on page when immediate input expected
- Useful for login forms, password entry
- Be cautious with this as it can interfere with page navigation

## name

Controls the name attribute of the input element, used for form submission and identification.

**Visual cues:**
- Not directly visible to users
- Used in form data submission and validation referencing
- Emitted with valueChange events as field identifier

**When to use:**
- Set for all input fields in forms to properly submit form data
- Required for proper form validation and submission
- Helps identify fields in event handlers and backend processing

## ariaLabel

Provides accessibility label for screen readers. Falls back to label if not set.

**Visual cues:**
- Not visible to sighted users
- Read by screen readers to identify the password input

**When to use:**
- Set when different from visible label for accessibility
- Use when you need more descriptive label for screen readers
- Leave empty if label prop provides sufficient description

**Fallback behavior:**
- Uses label value if ariaLabel not set

## focus

Programmatic focus function to set focus to the input element.

**Visual property:** none (behavioral)

**When to use:**
- This is a behavioral prop not derivable from visual design
- Should generally be left at its default unless specifically called
- Used to programmatically trigger password field focus
- Useful for keyboard navigation, error handling, form logic

## Events

### valueChange
Fires on every input change when the user types or modifies the password value. Emits a CustomEvent with payload wrapped in `event.detail`.

**Emitted args:** `CustomEvent<{ name: string, value: string }>`

**When to use:**
- Capture user input for validation or real-time processing
- Track password field changes for analytics
- Implement password strength requirements validation

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
<ion-password-input
  name="userPassword"
  (valueChange)="onValueChange($event)">
</ion-password-input>
```

### focusIn
Fires when the input field receives focus. Emits a CustomEvent with void payload.

**Emitted args:** `CustomEvent<void>`

**When to use:**
- Trigger UI changes when password field gains focus
- Start validation timers or form state tracking
- Implement custom accessibility behavior

**How to use:**
```typescript
// Angular component handler method
onFocusIn(event: CustomEvent<void>): void {
  console.log("Password input focused");
  this.isPasswordFocused = true;
  // event.detail is undefined (void payload)
}
```

**Binding syntax:**
```html
<ion-password-input (focusIn)="onFocusIn()"></ion-password-input>
```

### focusOut
Fires when the input field loses focus. Triggers validation if `validationMode` is set to `onBlur`. Emits a CustomEvent with void payload.

**Emitted args:** `CustomEvent<void>`

**When to use:**
- Trigger validation when user completes password entry
- Track form completion state
- Reset UI elements activated on focus

**How to use:**
```typescript
// Angular component handler method
onFocusOut(event: CustomEvent<void>): void {
  console.log("Password input lost focus");
  this.validatePassword();
  // event.detail is undefined (void payload)
}
```

**Binding syntax:**
```html
<ion-password-input validationMode="onBlur" (focusOut)="onFocusOut()"></ion-password-input>
```

### endEnhancerButtonClick
Fires when the visibility button (eye icon) is clicked to toggle password visibility. Emits a CustomEvent with void payload.

**Emitted args:** `CustomEvent<void>`

**When to use:**
- Track when user toggles password visibility for analytics
- Trigger custom behavior when password visibility changes
- Implement additional security features or logging

**How to use:**
```typescript
// Angular component handler method
onEndEnhancerButtonClick(event: CustomEvent<void>): void {
  console.log("Password visibility toggled");
  this.trackPasswordVisibilityToggle();
  // event.detail is undefined (void payload)
}
```

**Binding syntax:**
```html
<ion-password-input visibilityButton="true" (endEnhancerButtonClick)="onEndEnhancerButtonClick()"></ion-password-input>
```

### validationStateChange
Fires whenever the `validationState` property changes. Emits a CustomEvent with validation state wrapped in `event.detail`.

**Emitted args:** `CustomEvent<"valid" | "invalid" | "none">`

**When to use:**
- React to validation state changes in the UI
- Trigger form submission enable/disable logic
- Implement custom validation feedback animations

**How to use:**
```typescript
// Angular component handler method - web element pattern
onValidationStateChange(event: CustomEvent<"valid" | "invalid" | "none">) {
  console.log("Validation state changed to:", event.detail);
  if (event.detail === "invalid") {
    this.showValidationMessage();
  }
  // Access validation state via event.detail for web element events
}
```

**Binding syntax:**
```html
<ion-password-input
  validationMode="onChange"
  (validationStateChange)="onValidationStateChange($event)">
</ion-password-input>
```

### Complete event binding example:

```html
<ion-password-input
  label="Password"
  name="userPassword"
  visibilityButton="true"
  validationMode="onBlur"
  (valueChange)="onValueChange($event)"
  (focusIn)="onFocusIn()"
  (focusOut)="onFocusOut()"
  (endEnhancerButtonClick)="onEndEnhancerButtonClick()"
  (validationStateChange)="onValidationStateChange($event)">
</ion-password-input>
```

**Handler implementation:**
```typescript
import { CustomEvent } from '@angular/platform-browser';

onValueChange(event: CustomEvent<{ name: string, value: string }>) {
  console.log('Field:', event.detail.name);
  console.log('Value:', event.detail.value);
}

onFocusIn(event: CustomEvent<void>) {
  console.log('Password input focused');
}

onFocusOut(event: CustomEvent<void>) {
  console.log('Password input lost focus');
  this.validatePassword();
}

onEndEnhancerButtonClick(event: CustomEvent<void>) {
  console.log('Password visibility toggled');
}

onValidationStateChange(event: CustomEvent<"valid" | "invalid" | "none">) {
  console.log('Validation state:', event.detail);
}
```

## Examples

```html
<ion-password-input label="Label" labelPlacement="vertical" size="md"></ion-password-input>
```
Demonstrates default password input with label and medium size.

```html
<ion-password-input label="Label" labelPlacement="horizontal" labelAlignment="start" labelWidth="120px" size="md"></ion-password-input>
```
Demonstrates horizontal label layout with start alignment and specified width.

```html
<ion-password-input size="sm" helperMessage="Helper Message" helperMessageAsTooltip="false"></ion-password-input>
```
Demonstrates small input with helper message.

```html
<ion-password-input placeholder="Your password" visibilityButton="false"></ion-password-input>
```
Demonstrates input with placeholder but no visibility button.

```html
<ion-password-input value="password" visibilityButton="true"></ion-password-input>
```
Demonstrates input with value and visibility button enabled for toggle functionality.

```html
<ion-password-input helperMessage="Valid Helper Message" validationState="valid"></ion-password-input>
```
Demonstrates valid validation state with green helper message.

```html
<ion-password-input helperMessage="Invalid Helper Message" validationState="invalid"></ion-password-input>
```
Demonstrates invalid validation state with red helper message.

```html
<ion-password-input label="Label" necessityIndicator="requiredMarker"></ion-password-input>
```
Demonstrates required field with asterisk indicator.

```html
<ion-password-input required="true" validationMode="onBlur"></ion-password-input>
```
Demonstrates pattern validation triggered on blur with required attribute.

```html
<ion-password-input disabled="true"></ion-password-input>
```
Demonstrates disabled password input state.

```html
<ion-password-input readOnly="true" value="password123"></ion-password-input>
```
Demonstrates read-only password input with predefined value.

```html
<ion-password-input size="sm"></ion-password-input>
<ion-password-input size="md"></ion-password-input>
<ion-password-input size="lg"></ion-password-input>
```
Demonstrates comparison of small, medium, and large password input sizes.

```html
<ion-password-input helperMessage="Helper Message" helperMessageAsTooltip="true" tooltip-placement="right"></ion-password-input>
```
Demonstrates helper message displayed as tooltip with right placement.

```html
<ion-password-input
  label="Password"
  name="userPassword"
  visibilityButton="true"
  validationMode="onBlur"
  (valueChange)="onPasswordValueChange($event)"
  (focusOut)="validatePassword()">
</ion-password-input>
```
Demonstrates password input with proper event bindings for value changes and focus-out validation.

```typescript
import { CustomEvent } from '@angular/platform-browser';

onPasswordValueChange(event: CustomEvent<{ name: string, value: string }>) {
  // Access web element event payload via event.detail
  console.log("Password field:", event.detail.name);
  console.log("New value:", event.detail.value);
  this.currentPassword = event.detail.value;
  this.checkPasswordStrength(event.detail.value);
}

validatePassword(event?: CustomEvent<void>): void {
  // Perform validation after user completes entry
  if (this.passwordTooWeak) {
    this.validationState = "invalid";
    this.helperMessage = "Password does not meet requirements";
  } else {
    this.validationState = "valid";
    this.helperMessage = "Password is strong";
  }
}
```
Demonstrates proper event handler implementations with correct web element pattern using `event.detail` for payload access.