---
realComponent: ion-radio-group
description: A radio group component that manages a set of mutually exclusive radio button options with shared state, validation, keyboard navigation, and accessibility features.
themes: [modern-light-ds, modern-dark-ds]
relatedComponents:
  - name: "ion-radio"
    relationship: "child"
    whenToUse: "Use individual ion-radio elements as children within the radio-group. Each radio represents one option in the mutually-exclusive set managed by the parent radio-group component. The radio-group provides shared name/selection state and keyboard navigation, while ion-radio handles individual option presentation."
apiTypes: ["element"]
props:
  - name: size
    type: string
    category: visual
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: emphasized
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
    default: "none found"
    values: []
    designTokens: {}
  - name: labelPlacement
    type: string
    category: visual
    required: false
    default: "vertical"
    values: ["vertical", "horizontal"]
    designTokens: {}
  - name: labelAlignment
    type: string
    category: visual
    required: false
    default: "start"
    values: ["start", "end"]
    designTokens: {}
  - name: labelWidth
    type: string
    category: visual
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: contentOrientation
    type: string
    category: visual
    required: false
    default: "vertical"
    values: ["vertical", "horizontal"]
    designTokens: {}
  - name: name
    type: string
    category: behavioral
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: value
    type: any
    category: behavioral
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: defaultValue
    type: any
    category: behavioral
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: required
    type: boolean
    category: accessibility
    required: false
    default: false
    values: []
    designTokens: {}
  - name: necessityIndicator
    type: string
    category: visual
    required: false
    default: "requiredMarker"
    values: ["requiredMarker", "requiredLabel", "optionalLabel", "none"]
    designTokens: {}
  - name: validationState
    type: string
    category: visual
    required: false
    default: "none"
    values: ["valid", "invalid", "warning", "none"]
    designTokens:
      "valid":
        light:
          resolvesTo: "#2dc168"
          tokenChain: "validation state valid --ion-comp-radio-container-color-bg-valid-subtle -> --ion-lit-color-leonardo-base-positive (#2dc168)"
          appliesToCssProperty: "background-color, border-color"
      "invalid":
        light:
          resolvesTo: "#c70000"
          tokenChain: "validation state invalid --ion-comp-radio-container-color-bg-invalid-subtle -> --ion-lit-color-leonardo-base-negative (#c70000)"
          appliesToCssProperty: "background-color, border-color"
      "warning":
        light:
          resolvesTo: "#fe7f2a"
          tokenChain: "validation state warning --ion-comp-radio-container-color-bg-warning-subtle -> --ion-lit-color-leonardo-base-warning (#fe7f2a)"
          appliesToCssProperty: "background-color, border-color"
      "none":
        light:
          resolvesTo: "#ffffff"
          tokenChain: "validation state none --ion-comp-radio-container-color-bg-enabled-subtle -> --ion-lit-color-palette-misc-white (#ffffff)"
          appliesToCssProperty: "background-color, border-color"
  - name: validationMode
    type: string
    category: behavioral
    required: false
    default: "none found"
    values: ["onSubmit", "onBlur", "none"]
    designTokens: {}
  - name: helperMessage
    type: string
    category: content
    required: false
    default: "none found"
    values: []
    designTokens: {}
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
  - name: ariaLabel
    type: string
    category: accessibility
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: description
    type: string
    category: content
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: orientation
    type: string
    category: visual
    required: false
    default: "none found"
    values: ["vertical", "horizontal"]
    designTokens: {}
events:
  - name: valueChange
    payloadType: "CustomEvent<{name: string, value: string}>"
    firesWhen: "Fires when the user selects a different radio button option. Only fires for actual user interactions, not when value is programmatically updated via the value prop."
    detailAccess: "event.detail.name (string), event.detail.value (string)"
    bindingSyntax: '(valueChange)="onValueChange($event)"'
  - name: change
    payloadType: "CustomEvent<{name: string, value: string}>"
    firesWhen: "Fires when the user selects a different radio button option. Maintained for backward compatibility. Only fires for actual user interactions, not when value is programmatically updated via the value prop."
    detailAccess: "event.detail.name (string), event.detail.value (string)"
    bindingSyntax: '(change)="onChange($event)"'
jointTokens:
  - combination: "emphasis=true, validationState=none"
    resolvesTo: "#007de0"
    tokenChain: "emphasized enabled state --ion-comp-radio-container-color-bg-enabled-bold -> --ion-lit-color-leonardo-base-primary (#007de0)"
    appliesToCssProperty: "background-color, border-color"
  - combination: "emphasis=false, validationState=none"
    resolvesTo: "#ffffff"
    tokenChain: "non-emphasized enabled state --ion-comp-radio-container-color-bg-enabled-subtle -> --ion-lit-color-palette-misc-white (#ffffff)"
    appliesToCssProperty: "background-color, border-color"
  - combination: "validationState=valid"
    resolvesTo: "#2dc168"
    tokenChain: "validation valid state --ion-comp-radio-container-color-bg-valid-subtle -> --ion-lit-color-leonardo-base-positive (#2dc168)"
    appliesToCssProperty: "background-color, border-color"
  - combination: "validationState=invalid"
    resolvesTo: "#c70000"
    tokenChain: "validation invalid state --ion-comp-radio-container-color-bg-invalid-subtle -> --ion-lit-color-leonardo-base-negative (#c70000)"
    appliesToCssProperty: "background-color, border-color"
  - combination: "validationState=warning"
    resolvesTo: "#fe7f2a"
    tokenChain: "validation warning state --ion-comp-radio-container-color-bg-warning-subtle -> --ion-lit-color-leonardo-base-warning (#fe7f2a)"
    appliesToCssProperty: "background-color, border-color"
propInteractions:
  - size prop cascades to all child radio elements via setPropertyToAllRadio("size", value)
  - emphasized prop cascades to all child radio elements via setPropertyToAllRadio("emphasized", value)
  - disabled prop cascades to all child radio elements via setPropertyToAllRadio("disabledInternal", value)
  - readOnly prop cascades to all child radio elements via setPropertyToAllRadio("readOnlyInternal", value)
  - value prop only emits events on user interaction; programmatic updates via value setter don't trigger events (isDefaultValue flag prevents this)
  - validationMode only applies validation when set to "onBlur" with required=true; other modes ("onSubmit", "none") don't trigger automatic validation
  - labelPlacement and contentOrientation control different aspects of layout: labelPlacement affects label-to-group positioning, contentOrientation affects radio button layout within the group
  - orientation is deprecated in favor of labelPlacement; when not set, labelPlacement falls back to orientation for compatibility
  - description prop is deprecated in favor of helperMessage; when not set, helperMessage can fall back to description
  - defaultValue is used for initial selection; once user interacts, value takes precedence and isDefaultValue flag becomes false
needsReview:
  - "Dark theme tokens not found for validationState values; only light theme tokens were traceable from ds_tokens.css"
  - "Size prop only documented with default 'md' behavior; specific design tokens for sm/lg size values (dimensions, padding) not traced from provided ds_variables.json"
  - "Design tokens for emphasized combinations with different validation states not fully traced; only basic enabled states documented"
  - "Color values for disabled and readOnly states in combination with emphasis or validation states not traced"
  - "Design tokens for labelWidth prop not found; appears to use direct CSS values without design system abstractions"
  - "ContentOrientation vs labelPlacement interaction not fully documented; when horizontal content orientation meets horizontal label placement, specific layout behavior assumed"
  - "validationMode='onSubmit' behavior documented but actual validation triggering mechanism not traceable from provided source"
  - "Radio button specific token values for different sizes (sm, md, lg) not traced from ds_variables.json; only token references found in radio-ds.css"
---

## Usage Notes

Boolean props on this component must always be passed with an explicit string value — e.g. `disabled="true"` or `[disabled]="isDisabled"` — never as bare attribute presence (e.g. `disabled` alone, with no value). Bare attribute presence is a native HTML convention this component does NOT support; it will not be interpreted as true.

## Related Components

This radio-group component has a closely related companion: `ion-radio`. The radio-group serves as a container that manages shared state and behavior for multiple mutually exclusive radio options. Individual `ion-radio` elements are rendered as children within the radio-group. The radio-group provides shared name/selection state, keyboard navigation, and accessibility features, while each `ion-radio` handles the presentation of individual options. Use radio-group instead of multiple standalone radio elements whenever rendering 2+ mutually exclusive options together — it manages shared name/selection state and keyboard navigation automatically.

## size

Controls the sizing of radio buttons throughout the radio group, affecting the dimensions of both the radio indicators and spacing within the group. The size prop can accept both direct size values and MQ (media query) design strings for responsive behavior.

**Visual cues:**
- sm: Small radio buttons with compact spacing, suited for dense UI layouts
- md: Medium radio buttons (default), standard sizing for most use cases  
- lg: Large radio buttons with generous spacing, for prominent selections or accessibility

**When to use:**
- sm: Compact forms, data-dense interfaces, secondary selection groups
- md: Standard forms, primary selection groups (default)
- lg: Primary selection in spacious layouts, accessibility-focused interfaces

**Responsive behavior:**
- Supports MQ design strings parsed by MqDesignStringParserService
- Example: `xs=sm;sm=md;md=md;lg=lg;xl=lg;xxl=md` for different sizes across breakpoints
- Size cascades to all child radio elements automatically

## emphasized

Controls whether radio buttons use bold/strong visual styling with enhanced border and background colors for increased visual prominence.

**Visual cues:**
- true: Enhanced borders and stronger background colors, more prominent appearance
- false: Standard styling with subtle borders and lighter backgrounds (default)

**When to use:**
- true: Important selection groups, primary choices, when you want options to stand out
- false: Standard secondary selections, less prominent choice groups (default)

**Cascading behavior:**
- Propagates to all child radio elements automatically

## label

Provides the main descriptive text label for the entire radio group. This label appears above or beside the group of radio options depending on labelPlacement.

**Visual cues:**
- When set: Displays as text label positioned according to labelPlacement
- When empty: No group label is rendered; only radio options appear

**When to use:**
- Always provide a clear, descriptive label for accessibility and UX
- Leave empty only for groups that are sufficiently identified by surrounding context

## labelPlacement

Controls the positioning of the group label relative to the radio options container.

**Visual cues:**
- vertical: Label appears above the radio options (default)
- horizontal: Label appears to the left of the radio options

**When to use:**
- vertical: Standard form layout with labels above inputs (default)
- horizontal: Side-by-side layouts, compact interfaces where horizontal space is available

**Note:** The deprecated `orientation` prop falls back to this value.

## labelAlignment

Controls the horizontal alignment of the label within its allocated space. Only applies when labelPlacement is horizontal.

**Visual cues:**
- start: Label aligned to the left (default for LTR languages)
- end: Label aligned to the right (default for RTL languages)

**When to use:**
- start: Standard left-aligned labels (default)
- end: Right-aligned labels for RTL languages or specific design requirements

## labelWidth

Specifies the width of the label area when labelPlacement is horizontal. Accepts CSS values like pixels, percentages, or design tokens.

**Visual cues:**
- When set: Constrains label to specified width; text may wrap or truncate
- When empty: Label takes natural width based on content

**When to use:**
- Set when you need precise control over label width in horizontal layouts
- Use for consistent label column widths across multiple radio groups

## contentOrientation

Controls the layout direction of the radio buttons within the group container.

**Visual cues:**
- vertical: Radio buttons stack vertically (default)
- horizontal: Radio buttons flow horizontally in a row

**When to use:**
- vertical: Standard list of options, longer option text labels (default)
- horizontal: Short option labels, compact layouts, categorical choices

## name

Provides the form name attribute for the radio group, which is used when submitting HTML forms. All child radio elements receive this name automatically.

**Visual property:** none (behavioral)

**When to use:**
- Set when the radio group will be used in an HTML form submission
- Leave empty if no form submission is required

## value

Controls the currently selected value within the radio group. Must match one of the values provided to child radio elements.

**Visual property:** none (behavioral)

**When to use:**
- Set to programmatically control selection state
- Use when reading the current selected value
- Changes programmatically won't emit events (isDefaultValue flag prevents this)
- If value doesn't match any radio button value, console warning is issued

## defaultValue

Provides the initial selected value when the group first renders, used as a fallback for uncontrolled form behavior.

**Visual property:** none (behavioral)

**When to use:**
- Set for initial selection in uncontrolled forms
- Used when value prop is not initially set
- Once user interacts, value prop takes precedence

## required

Specifies whether the radio group must have a selection for form validity.

**Visual cues:**
- true: Typically shows required indicator (asterisk or label text) based on necessityIndicator
- false: No required indication (default)

**When to use:**
- true: When form submission requires one of the radio options to be selected
- false: When selection is optional (default)

## necessityIndicator

Controls how the requirement status is visually indicated to the user.

**Visual cues:**
- requiredMarker: Shows asterisk (*) symbol (default)
- requiredLabel: Shows "Required" text
- optionalLabel: Shows "Optional" text  
- none: No visual indicator

**When to use:**
- requiredMarker: Standard compact indication (default)
- requiredLabel: More explicit requirement communication
- optionalLabel: Explicitly mark optional fields
- none: No visual indication needed

## validationState

Controls the validation state styling, applying colors and visual cues to indicate form validity.

**Visual cues:**
- valid: Green colors indicating successful validation
- invalid: Red colors indicating validation errors
- warning: Orange/amber colors indicating cautionary states
- none: Neutral styling (default)

**When to use:**
- valid: Show successful validation after user action
- invalid: Display validation errors when required field is empty
- warning: Show cautionary states or minor issues
- none: Normal state when no validation needed (default)

**Note:** Colors are applied to radio button containers and indicators; exact values depend on combination with emphasized prop (see jointTokens).

## validationMode

Controls when validation is triggered and helper messages are updated.

**Visual property:** none (behavioral)

**When to use:**
- onBlur: Validate when user focuses away from the radio group
- onSubmit: Validate when form is submitted (validation not triggered automatically in provided code)
- none: No automatic validation (default for validationMode prop)

**Behavioral notes:**
- Only validationMode="onBlur" is actually implemented in the validate() method
- Other modes are accepted but don't trigger automatic validation in current implementation
- Validation only occurs when required=true and validationMode="onBlur"

## helperMessage

Provides context, guidance, or validation feedback text displayed below the radio set.

**Visual cues:**
- When set: Shows message text below radio options with appropriate styling
- Updates automatically when validation state changes in onBlur mode
- When empty: No helper message displayed

**When to use:**
- Provide usage guidance or additional context
- Show validation error messages when validationState="invalid"
- Show confirmation messages when validationState="valid"
- Note: description prop is deprecated; use helperMessage instead

## disabled

Controls disabled state for the entire radio group, preventing all user interactions.

**Visual cues:**
- true: All radio buttons appear non-interactive with reduced opacity and grayed appearance
- Applies to all child radio elements automatically

**When to use:**
- Set true when radio selection should not be currently available
- Override default false when form validation fails or permission-based restrictions apply

**Note:** Cascades to all child radio elements via disabledInternal property.

## readOnly

Controls read-only state where selections can be viewed but not changed by users.

**Visual cues:**
- true: Radio buttons appear interactive but cannot be changed
- Different visual treatment than disabled (maintains full opacity)

**When to use:**
- Set true to allow viewing current selection without editing
- Override default false when display-only view of selection is needed

**Note:** Cascades to all child radio elements via readOnlyInternal property.

## ariaLabel

Provides accessibility label for screen readers, overriding the default behavior which uses the label prop.

**Visual property:** none (accessibility)

**When to use:**
- Override default when ariaLabel needs to differ from visual label
- Use for more descriptive accessibility text than visual label provides
- Leave empty to use label as fallback; "optional" and "read-only" are automatically appended by ariaLabelMessage getter

## description

**DEPRECATED:** Use helperMessage instead. Maintained for backward compatibility.

**When to use:**
- Legacy code; new implementations should use helperMessage
- Falls back to description if helperMessage is not set

## orientation

**DEPRECATED:** Use labelPlacement instead. Maintained for backward compatibility.

**When to use:**
- Legacy code; new implementations should use labelPlacement
- Falls back to orientation for when labelPlacement is not set

## Events

### valueChange

Fires when the user selects a different radio button option through direct interaction (click, keyboard navigation). Does not fire when value is programmatically updated via the value prop setter.

**Emitted args:** `CustomEvent<{name: string, value: string}>`

**When to use:**
- Respond to user selections in controlled inputs
- Update application state when user makes a selection
- Trigger side effects or form validation on selection change

**How to use:**

```typescript
onValueChange(event: CustomEvent<{name: string, value: string}>) {
  const groupName = event.detail.name;
  const selectedValue = event.detail.value;
  console.log(`Radio group '${groupName}' selection changed to: ${selectedValue}`);
  // Update application state or trigger actions
  this.selectedOption = selectedValue;
}
```

**Binding syntax:**

```html
<ion-radio-group (valueChange)="onValueChange($event)">
  <ion-radio label="Option1" value="Option1"></ion-radio>
  <ion-radio label="Option2" value="Option2"></ion-radio>
</ion-radio-group>
```

### change

Fires when the user selects a different radio button option. Maintained for backward compatibility. Does not fire when value is programmatically updated.

**Emitted args:** `CustomEvent<{name: string, value: string}>`

**When to use:**
- Legacy code that expects change event
- New code should prefer valueChange event

**How to use:**

```typescript
onChange(event: CustomEvent<{name: string, value: string}>) {
  // Same payload as valueChange
  const groupName = event.detail.name;
  const selectedValue = event.detail.value;
  // Handle selection change
}
```

**Binding syntax:**

```html
<ion-radio-group (change)="onChange($event)">
  <ion-radio label="Option1" value="Option1"></ion-radio>
  <ion-radio label="Option2" value="Option2"></ion-radio>
</ion-radio-group>
```

### Complete event binding example

```html
<ion-radio-group 
  label="Select an option"
  (valueChange)="onValueChange($event)"
  (change)="onChange($event)">
  <ion-radio label="Option1" value="Option1"></ion-radio>
  <ion-radio label="Option2" value="Option2"></ion-radio>
  <ion-radio label="Option3" value="Option3"></ion-radio>
</ion-radio-group>
```

```typescript
export class MyComponent {
  selectedOption: string;

  onValueChange(event: CustomEvent<{name: string, value: string}>) {
    console.log('valueChange:', event.detail.value);
    this.selectedOption = event.detail.value;
  }

  onChange(event: CustomEvent<{name: string, value: string}>) {
    console.log('change:', event.detail.value);
    // Legacy event handler
  }
}
```

## Examples

```html
<ion-radio-group label="Label">
  <ion-radio label="Option1" value="Option1"></ion-radio>
  <ion-radio label="Option2" value="Option2"></ion-radio>
  <ion-radio label="Option3" value="Option3"></ion-radio>
</ion-radio-group>
```
Demonstrates default radio group with basic label and three options.

```html
<ion-radio-group label="Label" labelPlacement="vertical">
  <ion-radio label="Option1" value="Option1"></ion-radio>
  <ion-radio label="Option2" value="Option2"></ion-radio>
  <ion-radio label="Option3" value="Option3"></ion-radio>
</ion-radio-group>
```
Demonstrates vertical label placement with options arranged vertically.

```html
<ion-radio-group label="Label" labelPlacement="horizontal">
  <ion-radio label="Option1" value="Option1"></ion-radio>
  <ion-radio label="Option2" value="Option2"></ion-radio>
  <ion-radio label="Option3" value="Option3"></ion-radio>
</ion-radio-group>
```
Demonstrates horizontal label placement with side-by-side option layout.

```html
<ion-radio-group label="Label" (valueChange)="onChange($event)">
  <ion-radio label="Option1" value="Option1"></ion-radio>
  <ion-radio label="Option2" value="Option2"></ion-radio>
  <ion-radio label="Option3" value="Option3"></ion-radio>
</ion-radio-group>
```
Demonstrates valueChange event binding to handle user selections.

```html
<ion-radio-group label="Radio Group" required true>
  <ion-radio label="Option1" value="Option1"></ion-radio>
  <ion-radio label="Option2" value="Option2"></ion-radio>
  <ion-radio label="Option3" value="Option3"></ion-radio>
</ion-radio-group>
```
Demonstrates required field with default asterisk indicator.

```html
<ion-radio-group label="Label" necessityIndicator="optionalLabel">
  <ion-radio label="Option1" value="Option1"></ion-radio>
  <ion-radio label="Option2" value="Option2"></ion-radio>
  <ion-radio label="Option3" value="Option3"></ion-radio>
</ion-radio-group>
```
Demonstrates optional field with explicit "Optional" text indicator.

```html
<ion-radio-group 
  label="Radio Group" 
  labelPlacement="vertical" 
  value="Option2">
  <ion-radio label="Option1" value="Option1"></ion-radio>
  <ion-radio label="Option2" value="Option2"></ion-radio>
  <ion-radio label="Option3" value="Option3"></ion-radio>
</ion-radio-group>
```
Demonstrates programmatically controlled selection with pre-selected option.

```html
<ion-radio-group label="Label" disabled="true">
  <ion-radio label="Option1" value="Option1"></ion-radio>
  <ion-radio label="Option2" value="Option2"></ion-radio>
  <ion-radio label="Option3" value="Option3"></ion-radio>
</ion-radio-group>
```
Demonstrates disabled radio group with non-interactive appearance.

```html
<ion-radio-group label="Label" readOnly="true">
  <ion-radio label="Option1" value="Option1"></ion-radio>
  <ion-radio label="Option2" value="Option2"></ion-radio>
  <ion-radio label="Option3" value="Option3"></ion-radio>
</ion-radio-group>
```
Demonstrates read-only radio group with selection visible but not changeable.

```html
<ion-radio-group label="Radio Group" helperMessage="Helper Message">
  <ion-radio label="Option1" value="Option1"></ion-radio>
  <ion-radio label="Option2" value="Option2"></ion-radio>
  <ion-radio label="Option3" value="Option3"></ion-radio>
</ion-radio-group>
```
Demonstrates helper message display for context or guidance.

```html
<ion-radio-group label="Label" helperMessage="Valid Helper Message" validationState="valid">
  <ion-radio label="Option1" value="Option1"></ion-radio>
  <ion-radio label="Option2" value="Option2"></ion-radio>
  <ion-radio label="Option3" value="Option3"></ion-radio>
</ion-radio-group>
```
Demonstrates valid validation state with green styling and success message.

```html
<ion-radio-group label="Label" helperMessage="Invalid Helper Message" validationState="invalid">
  <ion-radio label="Option1" value="Option1"></ion-radio>
  <ion-radio label="Option2" value="Option2"></ion-radio>
  <ion-radio label="Option3" value="Option3"></ion-radio>
</ion-radio-group>
```
Demonstrates invalid validation state with red styling and error message.

```html
<ion-radio-group label="Label" helperMessage="Warning Helper Message" validationState="warning">
  <ion-radio label="Option1" value="Option1"></ion-radio>
  <ion-radio label="Option2" value="Option2"></ion-radio>
  <ion-radio label="Option3" value="Option3"></ion-radio>
</ion-radio-group>
```
Demonstrates warning validation state with amber styling and caution message.