---
realComponent: "ion-dropdown"
description: "A form component that allows users to select one or multiple options from a predefined list, with native select fallback for mobile"
themes:
  - light
  - dark
props:
  - name: "size"
    type: "string"
    category: "visual"
    required: false
    default: "md"
    values:
      - sm
      - md
      - lg
    designTokens: {}
  - name: "disabled"
    type: "boolean"
    category: "visual"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "readOnly"
    type: "boolean"
    category: "visual"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "label"
    type: "string"
    category: "content"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "labelPlacement"
    type: "LabelPlacement"
    category: "visual"
    required: false
    default: "vertical"
    values:
      - vertical
      - horizontal
    designTokens: {}
  - name: "labelAlignment"
    type: "LabelAlignment"
    category: "visual"
    required: false
    default: "start"
    values:
      - start
      - end
    designTokens: {}
  - name: "labelWidth"
    type: "string"
    category: "visual"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "helperMessage"
    type: "string"
    category: "content"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "helperMessageAsTooltip"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "validationState"
    type: "ValidationState"
    category: "visual"
    required: false
    default: "none"
    values:
      - none
      - valid
      - warning
      - invalid
    designTokens:
      none:
        light:
          resolvesTo: "#030f26"
          tokenChain: "ion-cont-color-role-light-neutral-900"
          appliesToCssProperty: "border-color"
      valid:
        light:
          resolvesTo: "#2dc168"
          tokenChain: "ion-lit-color-leonardo-base-positive"
          appliesToCssProperty: "border-color"
      warning:
        light:
          resolvesTo: "#fe7f2a"
          tokenChain: "ion-lit-color-leonardo-base-warning"
          appliesToCssProperty: "border-color"
      invalid:
        light:
          resolvesTo: "#c70000"
          tokenChain: "ion-lit-color-leonardo-base-negative"
          appliesToCssProperty: "border-color"
  - name: "validationMode"
    type: "ValidationMode"
    category: "behavioral"
    required: false
    default: "none"
    values:
      - none
      - onChange
      - onBlur
      - onSubmit
    designTokens: {}
  - name: "required"
    type: "boolean"
    category: "content"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "necessityIndicator"
    type: "IndicatorType"
    category: "visual"
    required: false
    default: "requiredMarker"
    values:
      - requiredMarker
      - requiredLabel
      - optionalLabel
      - none
    designTokens: {}
  - name: "startEnhancer"
    type: "Enhancer"
    category: "visual"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "endEnhancer"
    type: "Enhancer"
    category: "visual"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "clearButton"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "placeholder"
    type: "string"
    category: "content"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "tabIndex"
    type: "number"
    category: "accessibility"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "autoFocus"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "name"
    type: "string"
    category: "content"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "ariaLabel"
    type: "string"
    category: "accessibility"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "disableFullScreenMode"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "value"
    type: "any"
    category: "content"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "defaultValue"
    type: "any"
    category: "content"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "options"
    type: "DropdownItemSource"
    category: "content"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "loading"
    type: "boolean"
    category: "visual"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "multiSelect"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "separator"
    type: "string"
    category: "content"
    required: false
    default: ", "
    values: []
    designTokens: {}
  - name: "totalSelected"
    type: "boolean"
    category: "visual"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "showSelectAll"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "confirmOnApply"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "allSelectionValue"
    type: "string"
    category: "content"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "maxSelection"
    type: "number"
    category: "behavioral"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "groupMaxSelection"
    type: "number"
    category: "behavioral"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "dropdownWidth"
    type: "string"
    category: "visual"
    required: false
    default: "auto"
    values: []
    designTokens: {}
  - name: "dropdownHeight"
    type: '"default" | "full"'
    category: "visual"
    required: false
    default: "default"
    values:
      - default
      - full
    designTokens: {}
  - name: "headerElement"
    type: "IonElement"
    category: "content"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "footerElement"
    type: "IonElement"
    category: "content"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "focus"
    type: "() => void"
    category: "behavioral"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "blur"
    type: "() => void"
    category: "behavioral"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "closeDropdown"
    type: "() => void"
    category: "behavioral"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "openDropdown"
    type: "() => void"
    category: "behavioral"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "refreshOptions"
    type: "() => Promise<void>"
    category: "behavioral"
    required: false
    default: "none found"
    values: []
    designTokens: {}
jointTokens: []
propInteractions:
  - "validationMode controls when validation is executed: none (no automatic validation), onChange (validates on each change), onBlur (validates when field loses focus), onSubmit (validates during form submission). Only applies when required=true or other validation logic is present."
  - "labelAlignment only applies when labelPlacement=horizontal. When labelPlacement=vertical, labelAlignment has no visual effect."
  - "multiSelect activates additional multi-select properties: separator, totalSelected, showSelectAll, confirmOnApply, maxSelection, groupMaxSelection, and allSelectionValue. These props only have behavior when multiSelect=true."
  - "totalSelected and allSelectionValue work together: when totalSelected=true and all options are selected, allSelectionValue is displayed in the field instead of the comma-separated list of option labels."
  - "confirmOnApply controls whether multi-select selection is applied immediately (confirmOnApply=false) or only after user clicks Apply button (confirmOnApply=true). When confirmOnApply=true, Clear and Apply buttons appear in the dropdown footer."
  - "maxSelection and groupMaxSelection both limit multi-select but at different scopes: maxSelection applies to all options in the dropdown, groupMaxSelection applies per option group. Both default to Infinity (no limit) when not set."
  - "clearButton and confirmOnApply interact: when confirmOnApply=true, clearButton is hidden (confirmOnApply logic applies instead of clearButton). clearButton is only visible when confirmOnApply=false."
  - "disableFullScreenMode only applies on mobile devices. It controls whether mobile dropdown opens as a popover (disableFullScreenMode=true) or full-screen drawer (disableFullScreenMode=false). On desktop, this prop has no effect."
  - "dropdownHeight virtual scrolling behavior: dropdownHeight=full enables full viewport height for the dropdown panel which is commonly used with virtual scrolling for large option lists. dropdownHeight=default uses standard height calculation."
  - "helperMessage and helperMessageAsTooltip interact: when helperMessageAsTooltip=true, the helper message is shown in a tooltip on hover instead of displayed inline below the field."
  - "size affects multiple UI aspects: field height, padding, typography size, and arrow icon size. The actual visual size is computed via MQ strings for responsive behavior (e.g. xs=lg, sm=md, md=md, lg=md, xl=md by default)."
needsReview:
  - "No dark-theme-specific design tokens found for validationState values (valid, warning, invalid). Only light theme tokens were traced from ds_tokens.css. Dark theme may share the same hex values or use different resolution paths not yet documented."
  - "Disabled and readOnly states have no explicit design token definitions found. Their visual styling (grayed appearance) appears to be applied via CSS classes (ion-ds-disabled, ion-ds-read-only) but specific color/opacity tokens were not traced."
  - "Focus state styling (border color, box shadow, or other focus indicators) has no explicit design token definitions traced. Focus styling appears to be applied via CSS focus pseudo-classes."
  - "Placeholder text color/text icon tokens could not be traced from the available token definitions. Placeholder styling appears to use CSS class ion-ds-field-text-placeholder but specific color values were not found in token definitions."
  - "Dropdown panel background, border, and shadow tokens for the popover/drawer were not traced. These appear to come from UI component tokens (ion-cont-border-width-ui-popover-base, etc.) but specific resolution chains for dropdown panel styling need further investigation."
  - "The size prop has default responsive behavior (xs=lg, sm=md, md=md, lg=md, xl=md) but the MQ string mapping logic and exact resolution for each breakpoint could not be fully traced from the available code."
  - "Enhancer icon color tokens (iconColor property in Enhancer interface) were referenced but specific color palette mappings could not be traced from the available token definitions."
  - "The native select mode (isNative) styling for mobile devices uses browser-default styling since it renders a native <select> element. Design tokens do not apply in native mode - this is by design but should be noted for consistency considerations."
events:
  - name: "valueChange"
    payloadType: "CustomEvent<{ name: string, value: any }>"
    firesWhen: "Emitted whenever the selected option(s) changes - on every selection change in single-select mode, on confirmation in multi-select with confirmOnApply=true"
    detailAccess: "event.detail.name (string) - the dropdown's name attribute if set; event.detail.value (any) - the selected value (single value for single-select, array of values for multi-select)"
    bindingSyntax: "(valueChange)=\"onValueChange($event)\""
  - name: "dropdownStateChanged"
    payloadType: "CustomEvent<boolean>"
    firesWhen: "Emitted when the dropdown panel opens or closes - fires with true when opening, false when closing"
    detailAccess: "event.detail (boolean) - true if dropdown is opening, false if dropdown is closing"
    bindingSyntax: "(dropdownStateChanged)=\"onDropdownStateChanged($event)\""
  - name: "focusIn"
    payloadType: "CustomEvent<void>"
    firesWhen: "Emitted when the dropdown field receives focus - when users click or tab into the field, or when focus is set programmatically"
    detailAccess: "void, event.detail is undefined - this event signals focus state change without carrying data"
    bindingSyntax: "(focusIn)=\"onFocusIn()\""
  - name: "focusOut"
    payloadType: "CustomEvent<void>"
    firesWhen: "Emitted when the dropdown field loses focus - when users click away, tab out, or when focus is removed programmatically"
    detailAccess: "void, event.detail is undefined - this event signals focus state change without carrying data"
    bindingSyntax: "(focusOut)=\"onFocusOut()\""
  - name: "endEnhancerButtonClick"
    payloadType: "CustomEvent<void>"
    firesWhen: "Emitted when the end enhancer button (if type=icon-button) is clicked - provides hook for custom button action handling"
    detailAccess: "void, event.detail is undefined - this event signals button click without carrying data"
    bindingSyntax: "(endEnhancerButtonClick)=\"onEndEnhancerButtonClick()\""
  - name: "validationStateChange"
    payloadType: "CustomEvent<ValidationState>"
    firesWhen: "Emitted when the validation state changes due to validation logic execution - when validationState prop changes from none/valid/warning/invalid to a different state"
    detailAccess: "event.detail (ValidationState) - the validationState value: \"none\", \"valid\", \"warning\", or \"invalid\""
    bindingSyntax: "(validationStateChange)=\"onValidationStateChange($event)\""
---

## Usage Notes

Boolean props on this component must always be passed with an explicit string value — e.g. `disabled="true"` or `[disabled]="isDisabled"` — never as bare attribute presence (e.g. `disabled` alone, with no value). Bare attribute presence is a native HTML convention this component does NOT support; it will not be interpreted as true.

## size

Controls the height, padding, typography size, and arrow icon dimensions of the dropdown field. Size values (sm, md, lg) map to design system spacing and typography tokens that scale the entire field vertically. This is a visual prop that directly impacts the user's perception of the component's scale and prominence in the interface.

The actual rendered size is determined by MQ (Media Query) responsive strings that allow different sizes at different breakpoints. Without an MQ string, the size translates directly (sm=small, md=medium, lg=large). With MQ strings, each breakpoint can map to a different size - for example, the default behavior is xs=lg, sm=md, md=md, lg=md, xl=md, which means extra-small screens get large fields for touch targets, while medium through extra-large screens get medium-sized fields.

Visual cues for each size:
- **sm**: Shorter field height, smaller padding, smaller font for selected text, smaller arrow icon (16px), tighter internal spacing
- **md**: Medium field height (default), standard padding, regular font size for selected text, medium arrow icon (24px), standard internal spacing  
- **lg**: Taller field height, larger padding, larger font for selected text, larger arrow icon (32px), more generous internal spacing

This prop is self-contained and does not depend on other props for its effect. It drives multiple visual properties simultaneously (height, padding, typography, icon size) through the component's CSS classes that map to design tokens.

## disabled

When true, the dropdown field becomes completely non-interactive - users cannot click to open the dropdown menu, and the field appears visually deactivated with reduced opacity (typically 0.4) and grayed styling. This is a visual/behavioral prop that signals and enforces unavailable state.

The disabled state prevents any user interaction with the dropdown - clicking on the field does not open the dropdown menu, keyboard navigation is disabled, and the clear button (if enabled) is also non-functional. The dropdown maintains its selected value but users cannot change it.

Visual indicators of disabled state:
- Reduced opacity field (approx. 60% of normal opacity)
- Grayed appearance for text and icons
- Non-interactive cursor (not clickable)
- All interactive elements within the dropdown (arrow icon, clear button) appear disabled

This prop is self-contained and does not depend on other props. It overrides all interactive behavior regardless of other settings.

## readOnly

When true, the dropdown field maintains user interaction for opening the dropdown menu but prevents changing the selected value. Users can click to expand and view the dropdown options, but selecting different options has no effect. This creates a read-only presentation that still allows exploring the option list.

The readOnly state allows users to see the full dropdown menu and all available options but commits no changes. This is useful for scenarios where you want users to be able to explore options without making selections.

Visual indicators of readOnly state:
- Field appears interactive (normal opacity, interactive cursor)
- Arrow icon indicates dropdown can be opened
- Clear button (if enabled) is non-functional
- All options in the dropdown menu appear selectable but clicking them produces no effect

This prop is self-contained and does not depend on other props. It provides read-only access to the dropdown's option list while preventing value changes.

## label

The text content displayed as the field's identifier, typically positioned above (vertical placement) or beside (horizontal placement) the dropdown field. Labels provide context and help users understand what the dropdown is for. This is a content prop that does not affect the component's behavior or visual appearance beyond the text content.

The label prop accepts plain text strings. The visual presentation (font size, weight, placement, spacing) is controlled by other props like labelPlacement, labelWidth, and the overall component size.

When no label is provided, the dropdown field appears without a text identifier, which may be appropriate when a label is provided elsewhere in the UI (e.g., adjacent to the field as part of a larger form layout).

This prop is self-contained and does not depend on other props for its content, though its visual presentation depends on labelPlacement and labelAlignment.

## labelPlacement

Controls whether the label appears above the field (vertical) or beside it (horizontal). This is a visual/layout prop that affects the overall structure of the component and how it integrates with surrounding layout.

Label placement values:
- **vertical**: Label appears above the dropdown field, stacked vertically. This is the default and most common pattern for form fields where labels identify what each field does independently.
- **horizontal**: Label appears beside the dropdown field, arranged horizontally. This is useful for compact forms or when you want the label and field to fit within a single row.

Visual cues for each placement:
- **vertical**: Label positioned above the field, field spans full container width below the label, ideal for detailed labels or when multiple fields stack vertically
- **horizontal**: Label positioned to the left of the field, label and field share horizontal space within container, useful for compact layouts or short labels

This prop's effect is independent of other props, but its practical use often correlates with labelAlignment (only relevant for horizontal placement) and labelWidth (most commonly used with horizontal placement to control label-to-field spacing).

## labelAlignment

Controls whether the label is aligned to the start (left in LTR, right in RTL) or end (right in LTR, left in RTL) of the label area when labelPlacement=horizontal. This is a visual prop that only affects horizontal label arrangements and has no effect when labelPlacement=vertical.

Label alignment values:
- **start**: Label aligns to the start of the label area - left for left-to-right locales, right for right-to-left locales. This is the default and most common alignment.
- **end**: Label aligns to the end of the label area - right for left-to-right locales, left for right-to-right locales. This creates a rarer right-aligned label pattern, useful for specific design needs.

**Important interaction with labelPlacement**: This prop only has a visual effect when labelPlacement=horizontal. When labelPlacement=vertical, labelAlignment has no effect because the label occupies the full width above the field.

Visual cues for each alignment (when labelPlacement=horizontal):
- **start**: Label text starts at the left edge of the label area, creating left-aligned appearance in LTR. Most common pattern and familiar to users.
- **end**: Label text aligns to the right edge of the label area, creating right-aligned appearance in LTR. Less common pattern, used for specific design requirements.

This prop is dependent on labelPlacement=horizontal for its effect. When used without setting labelPlacement=horizontal, it appears to have no effect.

## labelWidth

Controls the width of the label area when labelWidth is explicitly set. This is a visual/layout prop that allows precise control over how much horizontal space the label occupies when labelPlacement=horizontal. The value accepts CSS length units (e.g., "100px", "30%", "12rem") and is applied directly to the label container.

Label width is most commonly used with labelPlacement=horizontal to create consistent label-to-field spacing across multiple fields in a form. When labelWidth is not specified, the label takes its natural width based on the content.

**Important interaction with labelPlacement**: This prop primarily affects horizontal label arrangements. When labelPlacement=vertical, labelWidth still applies but has less visual impact since the label occupies the full width above the field anyway.

Visual cues for different label widths (with labelPlacement=horizontal):
- **Narrow label** (e.g., "80px"): Label text may wrap or truncate, field takes more horizontal space, useful for short labels like "Name" or "ID"
- **Wide label** (e.g., "300px"): Label has ample space, field may be constrained, useful for detailed labels in compact forms
- **No labelWidth specified**: Label takes natural content width, field fills remaining horizontal space

This prop is most useful when combined with labelPlacement=horizontal. When labelPlacement=vertical, applying this prop has minimal visual effect since the label already occupies the full width above the field.

## helperMessage

Brief explanatory text displayed below the dropdown field to provide guidance, instructions, or contextual information to users. The helper message appears inline (below the field) by default, but can be displayed as a tooltip by setting helperMessageAsTooltip=true. This is a content prop that provides supplementary information without affecting the component's behavior.

The helper message serves as additional context for users - it can explain what the dropdown is for, provide format instructions, or offer other helpful information. The message appears in a smaller/lighter font weight than the label to create visual hierarchy.

**Important interaction with validationState**: When a validationState is set (valid, warning, invalid), the helperMessage is overridden by the validation message. The validation message takes precedence and replaces any helperMessage content. This makes the dropdown's inline message space single-purpose - it shows either help guidance OR validation feedback, not both simultaneously.

Visual presentation:
- **Applies styling**: Helper message uses smaller font size and lighter font weight than the label, appearing below the dropdown field in a neutral color
- **With helperMessageAsTooltip=true**: Helper message appears in a tooltip on hover instead of inline

This prop is self-contained for content, but its display behavior depends on helperMessageAsTooltip and may be overridden by validationState.

## helperMessageAsTooltip

When true, the helper message is displayed as a tooltip instead of being rendered inline below the dropdown field. This is a behavioral prop that affects how the helperMessage content is presented to users.

**Behavior differences**:
- **helperMessageAsTooltip=false (default)**: Helper message appears inline below the dropdown field, always visible, takes up permanent vertical space in the layout
- **helperMessageAsTooltip=true**: Helper message appears in a tooltip on hover/focus, saves vertical space, message only appears when users interact with the field

**Tooltip behavior**:
- Tooltip appears on hover for mouse users, on focus for keyboard users using the field
- Tooltip positioning defaults to "right" for mobile/smaller screens, can be customized via tooltipPlacement prop
- Tooltip follows the same timing as other component tooltips (100ms delay on open, 100ms delay on close)

This prop is dependent on helperMessage for content. It has no effect if helperMessage is not provided. It does not affect validation messages - those still display inline regardless of this prop's value.

## validationState

Controls the visual presentation of validation feedback on the dropdown field. The validation state affects the border color and visually indicates whether the field's current value is acceptable (valid), problematic (invalid), or has warnings (warning). This is a visual prop that communicates status without enforcing validation logic itself.

**Validation state values and their visual effects**:

- **none (default)**: No validation feedback displayed. Border color uses neutral color (`030f26` - ion-cont-color-role-light-neutral-900). This is the default state and means no validation state is currently set.

- **valid**: Valid state displayed. Border color changes to green (`2dc168` - ion-lit-color-leonardo-base-positive). Visual appearance: green border indicates the current value passes validation rules. This state is typically set by validation logic when the field's value is acceptable.

- **warning**: Warning state displayed. Border color changes to orange (`fe7f2a` - ion-lit-color-leonardo-base-warning). Visual appearance: orange border indicates the current value has potential issues but is not invalid. This state is typically set when the value has minor problems or needs attention.

- **invalid**: Invalid state displayed. Border color changes to red (`c70000` - ion-lit-color-leonardo-base-negative). Visual appearance: red border indicates the current value does not pass validation rules. This state is typically set when the field's value fails required validation or other validation rules.

**Important interaction with validationMode**: The validationState prop itself does not trigger validation - it only sets the visual state. For validation to actually occur automatically based on user interaction, you need to set validationMode (onChange, onBlur, onSubmit). The validationMode prop controls WHEN validation logic runs, and when that logic runs, it should set the validationState prop to reflect the result.

**Important interaction with helperMessage**: When validationState is not "none", any helperMessage content is overridden and the validation message appears instead. The dropdown uses a single inline message area that shows either helper guidance (validationState=none) or validation feedback (validationState has a value), not both simultaneously.

**Visual hierarchy**: Validation state uses color as the primary visual indicator - the border color changes to clearly signal the status. Additional feedback may come from validation icons or messages, but the most immediate visual cue is the border color change.

This prop is self-contained for visual presentation but is typically set by validation logic. It interacts with validationMode (for automatic triggering) and helperMessage (for message display behavior).

## validationMode

Controls when validation logic is executed and the validationState is updated. This is a behavioral prop that determines whether validation runs automatically based on user interaction or requires manual triggering. Unlike validationState (which sets the visual appearance), validationMode controls the timing of validation execution.

**Validation mode values and their behavior**:

- **none (default)**: No automatic validation occurs. The validationState must be set manually by application code. This is useful when you want complete control over when validation happens and when to display validation feedback.

- **onChange**: Validation runs on every value change. Each time the user selects a different option in the dropdown, validation logic executes and potentially updates validationState. This provides immediate feedback but may feel excessive if users haven't finished selecting.

- **onBlur**: Validation runs when the dropdown field loses focus (when user clicks away or tabs out). ValidationState is updated at that point. This provides feedback after the user has finished interacting with the field but before they move to the next element.

- **onSubmit**: Validation runs when the parent form submits. ValidationState is updated only at form submission time. This defers feedback until the submission moment, which is traditional for many form validation workflows.

**Important relationship with required**: The validationMode prop works in conjunction with the required prop. When required=true and validationMode is not "none", validation automatically checks whether the dropdown has a selected value. The component includes built-in validation logic for required fields:
- Required+validationMode=onChange: Checks if value is selected each time it changes
- Required+validationMode=onBlur: Checks if value is selected when field loses focus  
- Required+validationMode=onSubmit: Checks if value is selected during form submission
- Required+validationMode=none: No automatic validation of required state

**Important relationship with validationState**: The validationMode prop controls WHEN validation runs, but validationState controls WHAT is displayed. After validation runs (whether automatically via validationMode or manually), the validationState prop is set to reflect the result. Separating timing (validationMode) from presentation (validationState) allows flexible validation workflows.

**Messages**: When validation fails for required fields, the component automatically sets the helperMessage to "This field is required" (or localized equivalent). This message appears in the interface with the invalid validationState styling.

This prop is behavioral and does not have visual presentation on its own - it triggers validation logic that updates validationState. It works independently of other props but is commonly paired with required and validationState for complete validation workflows.

## required

When true, indicates that the dropdown field must have a selected value before the form can be considered complete. This is a semantic/content prop that affects validation behavior and can trigger visual indicators (via necessityIndicator). The required prop itself does not enforce the selection - it marks the field as required, and validation logic checks compliance.

**Required behavior combinations with validationMode**:

- **required=true + validationMode=none**: The field is semantically required (marked in HTML), but no automatic validation occurs. Your application code must manually validate that the field has a selected value.
- **required=true + validationMode=onChange**: Automatic validation runs on each value change. If the field is left empty (no selection), validationState is set to invalid with "This field is required" message.
- **required=true + validationMode=onBlur**: Automatic validation runs when the field loses focus. If the field is empty, validationState is set to invalid with "This field is required" message immediately after the user tabs out.
- **required=true + validationMode=onSubmit**: Automatic validation runs during form submission. If the field is empty, validationState is set to invalid with "This field is required" message at submission time.
- **required=false**: The field is optional. No automatic validation ensures a selection is made. Users can submit the form whether or not they've made a selection.

**Visual indication**: The required prop works with necessityIndicator to visually signal to users that a field requires input:
- **required=true + necessityIndicator=requiredMarker (default)**: Displays an asterisk (*) next to the label
- **required=true + necessityIndicator=requiredLabel**: Displays "Required" text next to the label
- **required=true + necessityIndicator=optionalLabel**: Displays "Optional" text next to the label (even though field is marked required)
- **required=true + necessityIndicator=none**: No visual indicator appears despite field being semantically required

**Accessibility**: The required prop adds the aria-required="true" attribute to the dropdown field's input element, which is important for screen readers and assistive technologies. This helps users understand which fields are required before they attempt form submission.

This prop is content/semantic in nature but has behavioral effects when combined with validationMode and visual effects when combined with necessityIndicator.

## necessityIndicator

Controls the visual indicator that signals to users whether the dropdown field is required or optional. This is a visual prop that adds visual cues (asterisk, text labels) next to the field's label to communicate necessity status.

**Necessity indicator values**:

- **requiredMarker (default)**: Displays an asterisk (*) symbol next to the field's label. This is the most common way to indicate required fields and familiar to most users. The asterisk appears in the same color as the label text, positioned directly after or before the label text depending on the design system's convention.

- **requiredLabel**: Displays the word "Required" as text next to the field's label. This provides more explicit verbal communication than the asterisk, which can be clearer for users who may not understand the asterisk convention or for accessibility reasons. The text appears in the same size and color as the label.

- **optionalLabel**: Displays the word "Optional" as text next to the field's label. This explicitly indicates that the field is NOT required, which can be helpful in forms where most fields are required and you want to highlight the exceptions. The text appears in the same size and color as the label.

- **none**: No visual indicator appears next to the label. The field's necessity status is not visually communicated through labels. This is useful when you want to handle necessity communication through other means (e.g., helper message, separate legend or note) or when mixing required/optional fields in a way that would create visual clutter with indicators on each field.

**Important relationship with required**: The necessityIndicator prop controls what visual indicator appears, but the required prop determines the semantic requirement status and automatic validation behavior:
- **required=true + necessityIndicator=requiredMarker**: Field is semantically required and displays asterisk indicator
- **required=true + necessityIndicator=requiredLabel**: Field is semantically required and displays "Required" text
- **required=true + necessityIndicator=optionalLabel**: Field is semantically required but displays "Optional" text (contradictory but possible)
- **required=true + necessityIndicator=none**: Field is semantically required but displays no visual indicator
- **required=false + any necessityIndicator value**: Field is semantically optional regardless of visual indicator; indicator may mislead users about actual requirement status

**Visual appearance**: The necessity indicator appears next to the label text, typically in the same font weight and size as the label, positioned after (or before) the label text. The indicator does not affect the label's color, size, or other styling properties.

This prop is visual and does not affect the component's behavior - it only adds visual communication. However, its accuracy relative to the actual required prop affects user communication quality.

## startEnhancer

Adds visual content (text, icon, or category icon) at the start of the dropdown field, positioned before the field's text input area. Enhancers provide additional context, affordance, or visual interest to help users understand the field's purpose. This is a visual prop that accepts an object configuration rather than a simple text value.

**Enhancer object structure**:
```typescript
{
  value: string,
  type: "text" | "icon" | "icon-button" | "category",
  iconFontFamily?: string,
  iconColor?: IconColor,
  ariaLabel?: string
}
```

**Start enhancer types and their application**:

- **type="text"**: Displays plain text at the start of the field. The value prop provides the text content (e.g., "+" for country codes, "$" for currency). This is useful for indicating prefixes like "+91", "$", "USD" where the content is plain text rather than an icon. The text appears in the same color as the field text (ion-cont-color-role-light-text-icon-700) with lighter weight to distinguish it from entered content.

- **type="icon"**: Displays an icon at the start of the field. The value prop specifies the icon name (e.g., "person", "location"). This is useful for providing context about what the field is for (e.g., person icon for user selection, location icon for place selection). The icon inherits color from the field's default styling but can be customized via the iconColor property.

- **type="icon-button"**: Displays an interactive button with an icon at the start of the field. The value prop specifies the icon name to display on the button. The button is clickable and triggers the startEnhancerButtonClick event. This is useful for adding interactive functionality like opening a search dialog, picking from a list, or other actions. The button has its own hover and focus states and does not interfere with the dropdown's opening functionality.

- **type="category"**: Displays a category-colored icon at the start of the field. This appears similar to type="icon" but uses category color styling rather than default field color. The value prop specifies the icon name. Category colors provide visual differentiation for different types of content (e.g., red for negative/warning items, green for positive ones, etc.).

**Visual positioning**: The start enhancer appears to the left of the field's text input area, Inline with the field content. It maintains consistent vertical alignment based on the field's size (taller matching for larger sizes). The space allocated to the enhancer scales based on its type (icons take less space than text, category icons take similar space to regular icons).

**Icon sizing**: Icon-based enhancers (type="icon", "icon-button", "category") automatically scale based on the dropdown's size prop:
- **size=sm**: Icon size is 16px
- **size=md (default)**: Icon size is 24px  
- **size=lg**: Icon size is 32px

**Accessibility**: For type="icon-button", you should provide an ariaLabel to ensure screen readers announce the button's purpose. For other enhancer types, the ariaLabel is optional but recommended for icons whose meaning may not be visually obvious.

This prop is visual and does not affect the component's behavior (except type="icon-button" which adds a clickable button). It does not depend on other props for its appearance but interacts visually with the field's layout.

## endEnhancer

Adds visual content (text, icon, or clickable icon-button) at the end of the dropdown field, positioned after the field's text input area and before the dropdown arrow icon. End enhancers provide additional functionality or affordance on the right side of the field. This is a visual prop that accepts an object configuration similar to startEnhancer but positioned differently.

**Enhancer object structure**:
```typescript
{
  value: string,
  type: "text" | "icon" | "icon-button",
  iconFontFamily?: string,
  iconColor?: IconColor,
  ariaLabel?: string
}
```

**End enhancer types and their application**:

- **type="text"**: Displays plain text at the end of the field, before the dropdown arrow. The value prop provides the text content. This is less common than start enhancers but can indicate units (e.g., "items", "people") or other context. The text appears in the same color as the field text with lighter weight.

- **type="icon"**: Displays a static (non-interactive) icon at the end of the field, before the dropdown arrow. The value prop specifies the icon name. This provides visual context or decoration without adding functionality. Common uses include informational icons, status indicators, or decorative elements.

- **type="icon-button"**: Displays an interactive button with an icon at the end of the field, before the dropdown arrow. The value prop specifies the icon name to display on the button. The button is clickable and triggers the endEnhancerButtonClick event. This is useful for adding actions like clearing the field, showing help, opening a dialog, or other contextual functionality. The button has its own hover and focus states and does not interfere with the dropdown's opening functionality.

**Visual positioning and layout**: The end enhancer is positioned between the field's text input area and the dropdown arrow indicator. It maintains consistent vertical alignment based on the field's size. When multiple end elements are present (clearButton, endEnhancer, dropdown arrow), they stack horizontally in this order from left to right: field text → clear button (if enabled) → end enhancer → dropdown arrow.

**Icon sizing and interaction**: Icon-based enhancers automatically scale based on the dropdown's size prop, identical to start enhancers:
- **size=sm**: Icon size is 16px
- **size=md (default)**: Icon size is 24px
- **size=lg**: Icon size is 32px

For type="icon-button", the interactive button includes proper focus and hover states, keyboard support (Enter key to activate), and accessibility attributes (role="button", aria-label).

**Important positioning relative to dropdown arrow**: The end enhancer appears before (to the left of) the dropdown arrow indicator. This means the dropdown arrow is always the rightmost interactive element at the end of the field. Users interact with end enhancers first, then see the dropdown arrow as an affordance for opening the options list.

This prop is visual and does not affect the component's behavior (except type="icon-button" which adds a clickable button). It is positioned independently of startEnhancer and positioned before the dropdown arrow indicator.

## clearButton

When true, displays a clear button (typically an X icon) inside the dropdown field that appears when the dropdown has a selected value and clears the selection when clicked. This is a behavioral/visual prop that conditional rendering and interaction behavior.

**Clear button behavior**:

- **clearButton=false (default)**: No clear button is displayed. Users cannot clear the dropdown's selection through this UI. If they want to deselect an option, they would need to select a different option (or your application code could clear the selection programmatically).

- **clearButton=true**: A clear button appears inside the dropdown field when:
  1. The dropdown has a selected value (the value prop is not empty/null)
  2. The clear button position (after endEnhancer, before dropdown arrow) is available
  3. The dropdown is not disabled or read-only (button only appears in interactive state)

The clear button is only displayed when there's a value to clear. When no option is selected, the button remains hidden to avoid clutter.

**Clear button positioning**: The clear button appears in the end area of the field, positioned after endEnhancer (if any) and before the dropdown arrow indicator. When multiple end elements are present, they stack horizontally: field text → clear button (when value exists) → end enhancer → dropdown arrow.

**Clear button visual appearance**: The clear button displays as an X or close icon, scaled to match the dropdown's size (16px for sm, 24px for md, 32px for lg). The button appears only when the field has a selected value and disappears when the field is empty. The button has hover and focus states for proper interaction feedback.

**Clear button interaction**: Clicking the clear button:
1. Clears the dropdown's selection (sets value to empty/null or empty array for multi-select)
2. Triggers the valueChange event with empty value
3. Clears any validationState (resets to "none") 
4. Hides the clear button itself (since there's no longer a value to clear)
5. Moves focus to the dropdown field for continued interaction

**Important interaction with confirmOnApply**: When confirmOnApply=true, the clearButton is not displayed even if clearButton=true is set. This is because confirmOnApply provides its own Clear button in the dropdown footer for multi-select confirmation scenarios. The two mechanisms don't mix - you use either clearButton (immediate clearing) OR confirmOnApply (confirmation workflow), not both.

**Keyboard accessibility**: The clear button is focusable via keyboard navigation (Tab key) and can be activated with Enter or Space keys. It has appropriate ARIA attributes for screen readers.

**Use cases**:
- Simple selections where users need to deselect: Use clearButton=true for immediate clearing capability
- Multi-select with confirmation workflow: Use confirmOnApply=true (clearButton is not used)
- Fields where clearing is not desirable: Use clearButton=false (default)

This prop is behavioral (adds click interaction) and visual (conditionally displayed). It depends on having a selected value to appear and interacts with confirmOnApply for multi-select scenarios.

## placeholder

The text displayed inside the dropdown field when no option is selected. This is a content prop that provides guidance or context to users about what they should select. The placeholder appears in lighter styling than entered content to distinguish it as instructional text rather than actual selected value.

**Placeholder behavior and usage**:

- **No placeholder provided**: When no option is selected, the field shows empty space or displays the selected value цвет the arrow icon. Users interact with an empty field, which may be disorienting if there's no guidance.
- **Placeholder provided (e.g., placeholder="Select")**: When no option is selected, the field shows "Select" in a lighter color/weight to indicate this is instructional text, not an actual selection. When an option becomes selected, the placeholder is replaced by the selected option's label.

**Visual appearance**: The placeholder text is displayed using the CSS class ion-ds-field-text-placeholder with lighter styling (typically reduced opacity or lighter color) to visually differentiate it from actual selected content. The placeholder uses the same font family and size as selected content but with this visual distinction.

**Important relationship with multi-select and totalSelected**: When multiSelect=true and totalSelected=true, the placeholder handling is more complex. When no options are selected, the placeholder still appears. When options are selected, totalSelected=true typically shows "X selected" instead of the individual labels, which replaces the placeholder display. The placeholder only appears when truly no options are selected.

**Use cases**:
- **No placeholder**: Appropriate when the field's purpose is obvious from context or label, or when you prefer a cleaner, minimalist appearance
- **Simple instructional text (e.g., "Select")**: Common pattern for dropdowns when users need basic guidance about what action to take
- **Contextual placeholder (e.g., "Choose a category")**: More specific guidance when the field's purpose may not be immediately clear
- **Format guidance (e.g., "DD/MM/YYYY")**: Less common for dropdowns but useful when the dropdown represents a structured format

**Accessibility**: The placeholder text is not announced by screen readers when the field is empty (typical HTML behavior for placeholder attributes). Instead, the field's label and helperMessage provide the primary accessibility description. The placeholder primarily serves sighted users as visual guidance.

This prop is content-only and does not affect the component's behavior. It is self-contained but its visual presentation is enhanced by multiSelect and totalSelected functionality.

## tabIndex

Controls the keyboard tab order and focusability of the dropdown field. This is an accessibility prop that determines whether the field can receive focus via keyboard navigation and in what order relative to other focusable elements.

**Tab index values and their behavior**:

- **tabIndex > 0** (e.g., tabIndex="1", tabIndex="2"): The field can receive keyboard focus and participates in the tab order. Fields with lower positive tabIndex values are focused first in the tab sequence. For example, if Field A has tabIndex="1" and Field B has tabIndex="2", users tab to Field A first, then Field B.

- **tabIndex="0"** (default): The field can receive keyboard focus and participates in the natural tab order determined by its position in the DOM. Fields with tabIndex="0" are tabbed to in the order they appear in the page, which is the default and recommended approach for most form fields.

- **tabIndex < 0** (typically tabIndex="-1"): The field is not focusable via tab key but can receive focus programmatically (e.g., via the focus() method). This is useful when you want to make a field focusable for programmatic interaction but not part of the normal keyboard navigation flow.

**Important default behavior**: When tabIndex is not explicitly set, the dropdown field uses the default value of 0, making it focusable and part of the natural tab order created by its DOM position. This is almost always the appropriate behavior for form fields.

**Accessibility implications**: The tab index affects keyboard navigation, which is critical for users who rely on keyboard navigation instead of mouse/touch. Managing tab order properly ensures that keyboard users can navigate through form fields in a logical, predictable sequence.

**Important relationship with disabled and readOnly**: The dropdown field is only actually focusable and interactive when disabled=false and readOnly=false. Setting a positive tabIndex on a disabled or readOnly Dropdown doesn't make it interactive - those props take precedence for interactivity.

**Recommended usage**: For most form scenarios, do not explicitly set tabIndex and let it default to 0. Only adjust tabIndex when you have a specific reason to modify the default tab order (e.g., when you need to override a confusing automatic tab order).

This prop is accessibility-focused and affects keyboard navigation. It does not affect the visual appearance or other behavior beyond focusability.

## autoFocus

When true, the dropdown field automatically receives focus when the component loads or mounts. This is a behavioral prop that affects initial focus placement and can improve usability by placing focus where users are expected to start.

**Auto focus behavior**:

- **autoFocus=false (default)**: The dropdown does not automatically receive focus when the component loads. Focus remains where it was before component mounted (typically not in the dropdown). Users must click or tab to the dropdown to interact with it.

- **autoFocus=true**: The dropdown field receives focus immediately when the component loads, before any user interaction. This calls the browser's focus() method on the dropdown's input element programmatically, making it the currently focused element. Users can immediately interact with the dropdown without needing to click or tab to it first.

**Browser behavior differences**: The autoFocus prop wraps the HTML autofocus attribute and calls the focus() method. Different browsers may handle autofocus differently:
- Most browsers properly autofocus the first element with autofocus=true
- Some browsers require user interaction before allowing programmatic focus
- The component tries different approaches to ensure cross-browser compatibility

**Important relationship with multiple elements**: When multiple form elements all have autoFocus=true, only one will actually receive focus - typically the first one encountered by the browser. You should not set autoFocus=true on multiple elements in the same view as this creates unpredictable behavior.

**Important relationship with validation**: If the dropdown requires immediate validation (e.g., a required field that should be filled first), autoFocus=true can ensure that users start with the most important field. However, this can also be disorienting if focus unexpectedly jumps.

**Accessibility considerations**: Auto focus can be helpful (users immediately land on the element they need to interact with) but also potentially disruptive (focus jumps without user control). For accessibility, consider whether auto focus truly improves user experience or creates confusion. Screen reader users may expect focus to start at the top of the page or content, not jump to a form field.

**Use cases**:
- **dialog/modal forms**: Set autoFocus=true on the most important field so users can immediately start interacting
- **single-field dialogs**: Set autoFocus=true on the only field to save users a click
- **sequential data entry**: Set autoFocus=true on the first field in a multi-step form
- **avoid in most cases**: Let users control focus flow by clicking/tabbing naturally

This prop is behavioral and does not affect visual appearance. It is self-contained but may be affected by browser behavior and should not be used on multiple elements in the same view.

## name

Sets the HTML name attribute for the dropdown field, which is important for form submission. The name attribute identifies the field when the form is submitted, allowing server-side code to associate submitted data with specific form elements. This is a content/behavioral prop that's critical for form data handling.

**Name behavior and usage**:

- **name not set (or empty string)**: The dropdown is still functional for interaction, but if it's part of a form that submits via standard HTML form submission, the dropdown's value won't be included in the submitted data (or may be included with an empty name). This may be acceptable when using AJAX submission or when the dropdown value is obtained programmatically rather than through form submission.

- **name set (e.g., name="country")**: The dropdown includes name="country" in its underlying input element, and when the parent form submits, the selected value is sent as country=value (where value is the selected option's value). This allows server-side code to access the dropdown's value via the name attribute.

**Form submission behavior**: When using standard HTML form submission (not AJAX or custom submission), the browser automatically includes the name-value pair for all form elements with:
1. A name attribute set
2. A non-empty value (selected option)

The dropdown component properly integrates with this behavior by setting the name attribute on its underlying input element.

**Multi-select naming in form submission**: When multiSelect=true, the dropdown's value is an array of selected values. Standard HTML form submission handles this by submitting multiple name-value pairs with the same name attribute. For example, if name="colors" and ["red", "blue"] are selected, the form submission includes: colors=red&colors=blue. Server-side code can access this as an array for the "colors" field.

**Important relationship with value change events**: The name prop is included in the valueChange event payload, specifically as the name property in IDropdownValueChangeEventArgs. This allows your event handler to identify which dropdown fired the event, which is useful when you have multiple dropdowns sharing the same event handler.

**Accessibility and debugging**: The name attribute doesn't directly affect accessibility but can help with debugging form submissions, since you can see which colored values correspond to named fields in browser developer tools.

This prop is important for form submission behavior and event handling. It doesn't affect visual appearance or interaction behavior beyond form submission and event identification.

## ariaLabel

Provides an accessible label for screen readers when the standard label prop is not sufficient or available. The aria-label attribute is read aloud by screen readers to identify the dropdown field to users who cannot see it visually. This is an accessibility prop that ensures users with visual impairments understand what the dropdown is for.

**ARIA label behavior**:

- **ariaLabel not set (or empty string)**: Screen readers announce the dropdown's purpose based on the label prop (if available). For example, if label="Country", screen readers may say "Country, dropdown, collapsed". This is usually sufficient for accessibility when a clear label is provided.

- **ariaLabel set (e.g., ariaLabel="Select your country of residence")**: Screen readers use this aria-label text instead of or in addition to the visual label. For example, screen readers would say "Select your country of residence, dropdown, collapsed". This can provide clearer, more descriptive text than the visual label.

**Important relationship with label prop**: When both label and ariaLabel are provided, screen readers typically use the more specific ariaLabel value rather than repeating the visual label. The ariaLabel is intended for cases where the visual label is either insufficient for blind users or when you want to provide alternative text.

**Use cases for ariaLabel**:

- **Different text for screen readers**: You may want screen readers to hear more descriptive text than what's visually shown. For example, label="Country" but ariaLabel="United States or Canada selection" for context specific to your application.

- **No visual label**: If the dropdown has no label prop (or the interface is minimal without explicit labels), ariaLabel provides the only accessibility identification for screen readers.

- **Icon-only fields**: If the dropdown uses only visual icons without text labels, ariaLabel provides the text description for screen readers.

- **Helper context**: You can include additional context in ariaLabel that helps screen reader users understand the field's purpose but would be verbose visually.

**Implementation note**: The component combines prop values for accessibility - the ariaLabelMessage getter in the TypeScript code shows that the a11y label is `ariaLabel || label + (necessityIndicator === "optionalLabel" ? " optional" : "")`. This means if ariaLabel is provided, it's used alone; otherwise the label is used with optional marker if configured.

**Accessibility impact**: ARIA labels are critical for accessibility. Screen reader users depend on accurate, descriptive ARIA labels to understand form fields. Without proper ARIA labels, screen reader users may not understand what the dropdown is for or may misinterpret its purpose.

This prop is accessibility-focused and does not affect visual appearance. It is important for compliance with accessibility standards (WCAG) and ensuring usable experiences for screen reader users.

## disableFullScreenMode

Controls whether the dropdown opens as a full-screen drawer or a popover on mobile devices. This is a behavioral prop that only affects mobile devices (touch devices) and has no effect on desktop/near-desktop layouts. On mobile, this prop determines the mobile presentation mode.

**Disable full screen mode behavior**:

- **disableFullScreenMode=false (default)**: On mobile devices (isMobileDevice=true), the dropdown opens as a full-screen drawer that covers most of the viewport height (75% by default). The drawer mode provides a mobile-optimized experience with larger touch targets and more space for selecting options, especially important for multi-select scenarios. This is the standard mobile behavior built into the design system.

- **disableFullScreenMode=true**: On mobile devices, the dropdown opens as a popover (floating overlay) instead of a full-screen drawer. The popover appears anchored below (or above if space is limited) the dropdown field and takes up less screen space than the full drawer. This preserves more context from the surrounding interface and may be preferred for specific mobile layouts.

**Desktop impact**: On desktop and non-mobile devices, disableFullScreenMode has no effect regardless of its value. Desktop always uses popover presentation since the screen space is already sufficient. This prop specifically targets mobile presentation differences.

**Mobile device detection**: The component uses the environment service's `isMobileDevice()` method to determine whether mobile presentation is needed. This typically considers both screen size and touch capability to identify true mobile/tablet devices vs small desktop windows.

**Important use case - multi-select**: The full-screen drawer mode is particularly beneficial for multi-select dropdowns on mobile because it provides larger touch targets and more space for confirming selections with the Apply/Clear buttons. When confirmOnApply=true, the drawer presentation shows these buttons in a footer area that provides a good mobile user experience.

**Important relationship with virtual scrolling**: Both drawer and popover modes support virtual scrolling when enabled (virtualScroll=true). The viewport height calculation differs slightly between modes (drawer gets 75% of viewport minus decorations, popover sizing is based on available space), but both enable efficient rendering of large option lists.

**Browser native mode impact**: The disableFullScreenMode prop has no effect when the dropdown renders as a native HTML <select> element. Native select rendering is controlled separately via design system configuration (enableNative: "MobileApp" or "MobileBrowser") and uses browser's native dropdown behavior which doesn't offer the drawer/popover choice.

**Use cases**:
- **Standard mobile behavior**: Use disableFullScreenMode=false (default) for standard mobile drawer presentation
- **Preserve context**: Use disableFullScreenMode=true when you want to keep surrounding interface visible on mobile
- **Desktop-only**: The prop doesn't need consideration for desktop-only applications since it has no effect there

This prop is behavioral and only affects mobile presentation. It interacts with the mobile device detection, virtual scrolling, and multi-select confirmation features.

## value

The currently selected value(s) of the dropdown. This is a content prop that represents which option(s) are currently selected. The value prop can be set initially (controlled component) or updated via valueChange events (uncontrolled component). The prop handles both single-select and multi-select scenarios automatically.

**Value behavior for single-select (multiSelect=false)**:

- **value type**: Accepts the actual value of the selected option (e.g., if option has value="us", then value="us")
- **Empty state**: value=null or value=undefined or value="" means no option is selected
- **Manual setting**: You can programmatically set the value to_SelectedIndexChangeded option, which updates the displayed selection
- **Event updates**: When users select an option, the valueChange event fires with the new value, and you can update your bound value accordingly

**Value behavior for multi-select (multiSelect=true)**:

- **value type**: Expects an array of selected option values (e.g., if options "us" and "ca" are selected, then value=["us", "ca"])
- **Empty state**: value=[] (empty array) means no options are selected - not null/undefined which would be misinterpreted
- **Manual setting**: You can programmatically set the value to an array of selected values
- **Event updates**: When users select/deselect options, the valueChange event fires with the updated array, and you can update your bound value accordingly

**Value normalization**: The component normalizes values internally to match the expected format for the current mode:
- If multiSelect=true and you provide a single value (not array), it's automatically converted to array: [value]
- If multiSelect=false and you provide an array, it automatically uses the last value in the array

**Value matching logic**: For value to match an option, the component uses a `equals()` helper function that performs deep equality comparison. This means:
- Simple values (strings, numbers, booleans): Compared by value (us matches "us", 5 matches 5)
- Complex values (objects, arrays): Compared by structure and content (not reference). For example, {id: 1, name: "Smith"} matches an option with same structure and content, even if different object reference.

**Important relationship with defaultValue**: If defaultValue is provided and value is not initially set, the component uses defaultValue as the initial selection. Once users interact, value overrides defaultValue. This is useful for pre-filling a default selection that users can override.

**Important relationship with validation and required**: The required property checks whether the dropdown has a valid selected value. For multiSelect, a non-empty array is considered "has value". For single-select, any non-null/non-empty value is considered "has value".

**Code examples - single-select**:
```typescript
// Setting initial selection
value="us"

// Responding to selection change
onValueChange(event) {
  this.value = event.detail.value; // Gets selected value (e.g., "us")
}
```

**Code examples - multi-select**:
```typescript
// Setting initial selections
value=["us", "ca", "mx"]

// Responding to selection changes
onValueChange(event) {
  this.value = event.detail.value; // Gets array of values (e.g., ["us", "ca"])
}
```

This prop is content/behavioral in nature and is essential for the dropdown's data model. It formats differently for single vs multi-select and integrates with validation and events.

## defaultValue

Provides the initial selected value(s) for the dropdown when the component first loads. Unlike value, which represents the current always-up-to-date selection, defaultValue has special behavior around initialization and history management. This is a content prop that's useful for pre-filling the dropdown or for browser history/ caching scenarios.

**Default value behavior and differences from value**:

- **defaultValue vs value**: The value prop always reflects the current selection, including all user interactions. The defaultValue prop provides an initial selection that can be overridden by user interaction and is also considered during browser history navigation (back/forward buttons), making it more suitable for scenarios where you want history awareness.

- **Interaction override**: When defaultValue is set and users don't interact, the dropdown shows the default selection. Once users select a different option, value overrides defaultValue and the user's selection persists.

- **Value initialization**: If both defaultValue and value are provided and value is empty/unset, defaultValue is used as the initial selection. This allows you to provide a default that users can override.

**Browser history integration**: The defaultValue prop has special behavior with browser history (back button navigation). When users navigate back to a page where they had previously interacted with the dropdown:
- History-aware forms treat defaultValue as the initial state before user interaction
- The browser may restore the form's previous state based on defaultValue
- This is different from value, which is treated as always-current user state

**Single-select default value**:
```typescript
// Pre-selecting "United States" on load
defaultValue="us"
```

**Multi-select default value**:
```typescript
// Pre-selecting multiple countries on load
defaultValue=["us", "ca", "mx"]
```

**Important relationship with required validation**: If defaultValue is set to a valid selection and the dropdown is required=true, then validation initially passes because the field is not empty. This is useful for forms where you want a required field to start with a valid selection.

**Common use cases**:
- **Form pre-population**: Set defaultValue when you want the dropdown to start with a reasonable selection for user convenience
- **Profile loading**: Load user's previously saved selection as defaultValue so it's their starting point
- **Survey templates**: Set default selections for templates that users can customize
- **History preservation**: Use defaultValue instead of value when you want browser history awareness

**Code example - using defaultValue properly**:
```typescript
// Don't update defaultValue after user interaction
// Instead update value when valueChange fires
onValueChange(event) {
  this.value = event.detail.value; // Updates current selection
  // Don't update: this.defaultValue = ... (this defeats the purpose)
}
```

This prop is content-focused and provides initial state vs the current state represented by value. It has special behavior with browser history and is most useful for initialization scenarios.

## options

The available options that users can select from in the dropdown. This is a content prop that defines the dropdown's option list, which can include simple options, grouped options, options with icons/descriptions, disabled options, and more. The options prop is central to the dropdown's data model and user interface.

**Options structure types**:

The options prop accepts multiple different structures to accommodate different data models:

1. **Basic IDropdownOption array**:
```typescript
[
  { value: "us", label: "United States" },
  { value: "ca", label: "Canada" },
  { value: "mx", label: "Mexico" }
]
```

2. **Mixed options and groups (IDropdownItem array)**:
```typescript
[
  { label: "North America", items: [
    { value: "us", label: "United States" },
    { value: "ca", label: "Canada" }
  ]},
  { value: "us", label: "United States (ungrouped)" },
  { value: "mx", label: "Mexico" }
]
```

3. **Function returning options**:
```typescript
() => [
  { value: "us", label: "United States" },
  { value: "ca", label: "Canada" }
]
```

4. **Async function returning Promise with options**:
```typescript
async () => {
  const response = await fetch('/api/countries');
  return response.json();
}
```

**Basic IDropdownOption properties**:
- `value`: The internal value of the option (any type - string, number, object, etc.)
- `label`: User-facing label text displayed in the dropdown (string)
- `description`: Optional secondary text displayed below the label (string)
- `disabled`: True if this option cannot be selected (boolean)
- `startEnhancer`: Optional enhancer object displayed before the option label (type: "text" | "icon")

**Grouped option (IDropdownOptionGroup) properties**:
- `label`: Group label displayed as a header for the group (string)
- `iconName`: Optional icon displayed alongside the group label (string)
- `iconFamily`: Optional icon family for the group icon (string)
- `items`: Array of IDropdownOption that belong to this group

**Options display patterns**:

- **Simple options** (value and label only): Clean list with just option labels, most common pattern
- **Options with descriptions**: Option label with secondary description below, provides additional context
- **Options with enhancers**: Text prefix or icon before the option label, visually differentiates grouped or categorized options
- **Disabled options**: Options appear grayed/unclickable and cannot be selected, useful for unavailable but relevant options
- **Grouped options**: Options organized under headers with optional group icons, useful for large option sets
- **Mixed listing**: Combination of grouped and ungrouped options (grouped items appear first, then ungrouped items)

**Virtual scrolling consideration**: Large option lists (≥15 items) automatically enable virtual scrolling for performance. This applies to both static arrays and function-returned options. Virtual scrolling efficiently renders only visible options regardless of total count.

**Updating options dynamically**: The options prop can be reactive - when the source data changes, the dropdown updates its option list. For arrays, this means assigning a new array reference. For functions, the function re-executes and returns updated options.

**Code examples - different option patterns**:

```typescript
// Simple options
options = [
  { value: "us", label: "United States" },
  { value: "ca", label: "Canada" }
]

// Options with descriptions
options = [
  { value: "us", label: "United States", description: "USA headquarters" },
  { value: "ca", label: "Canada", description: "Canadian operations" }
]

// Options with icon enhancers
options = [
  { value: "us", label: "United States", startEnhancer: { type: "icon", value: "flag_us" } },
  { value: "ca", label: "Canada", startEnhancer: { type: "icon", value: "flag_ca" } }
]

// Mixed grouped and ungrouped options
options = [
  { label: "Americas", items: [
    { value: "us", label: "United States" },
    { value: "ca", label: "Canada" }
  ]},
  { value: "uk", label: "United Kingdom (Europe)" },
  { value: "au", label: "Australia (Asia-Pacific)" }
]

// Async options from API
options = async () => {
  const response = await fetch('https://api.example.com/countries');
  return response.json();
}
```

This prop is content-focused and central to the dropdown's functionality. It can be structured in various ways to accommodate different data models, display patterns, and data loading strategies.

## loading

When true, indicates that the dropdown's options are currently loading or the component is in a loading state. This is a visual prop that typically displays a loading indicator/spinner to communicate to users that the dropdown is not yet ready for interaction.

**Loading behavior**:

- **loading=false (default)**: The dropdown displays normally and is fully interactive. Users can see the options, make selections, and interact with all dropdown functionality.

- **loading=true**: The dropdown appears in a loading state, typically with a spinner or loading indicator. The exact visual pattern depends on the design system implementation, but users should understand that the dropdown is not yet ready. This commonly appears when:
  - Options are being fetched asynchronously from an API
  - The dropdown is initializing and calculating options
  - The options data is being processed/calculated

**Important relationship with options prop**: The loading prop is most commonly used in conjunction with async options. When options are provided via a function that returns a Promise, the dropdown may need to show the loading state while the async operation completes.

**Impact on interaction**: When loading=true, the dropdown should be non-interactive - users cannot select options or interact with the dropdown until loading completes. The visual loading state communicates this temporary unavailability.

**Implementation pattern for async loading**:
```typescript
// Set loading true initially
loading = true;

// Set options as async function
options = async () => {
  try {
    const data = await fetchCountryOptions();
    return data;
  } finally {
    // Ensure loading false regardless of success/failure
    this.loading = false;
  }
};
```

**Visual representation**: The exact appearance of the loading state depends on the design system, but typically includes:
- Visual loading indicator (spinner or loader icon)
- Possibly placeholder text like "Loading..." or similar
- Non-interactive appearance (cursor indicates not clickable)

**Accessibility considerations**: When loading=true, the dropdown should have appropriate ARIA attributes to indicate loading state to screen readers. This helps users understand why the dropdown is temporarily unavailable.

**Use cases**:
- **API-driven options**: Show loading state while fetching options from server
- **Async data processing**: Show loading state while calculating large/complex option lists
- **Initialization delay**: Show loading state during component setup when options aren't immediately available
- **Data refreshing**: Show loading state when refreshing options after user action

This prop is visual and behavioral (affects interaction capabilities)。It is most useful in async loading scenarios and communicates temporary unavailability to users.

## multiSelect

When true, enables multiple option selection where users can select more than one option from the dropdown. This is a behavioral prop that fundamentally changes the dropdown's interaction model from single selection to multiple selection.

**Multi-select behavior and single-select differences**:

**Single-select (multiSelect=false, default)**:
- Only one option can be selected at a time
- Selecting one option automatically deselects the previously selected option
- Value is a single value (e.g., "us") not an array
- No selection limit by default (can select any one option)
- No multi-select-specific UI elements (checkboxes, apply/clear buttons)

**Multi-select (multiSelect=true)**:
- Multiple options can be selected simultaneously
- Users can select or deselect options independently
- Value is always an array (e.g., ["us", "ca", "mx"]) even if only one or no items selected
- Selection limits can be controlled via maxSelection (total) and groupMaxSelection (per group)
- Multi-select UI elements appear: checkboxes within options, apply/clear buttons (if confirmOnApply=true)
- mobile confirmation: On mobile when confirmOnApply=true, full-screen drawer has Apply/Clear buttons at bottom

**Visual differences in multi-select**:
- **Checkboxes**: Each option displays a checkbox to indicate its selected state
- **Selection indication**: Selected options maintain visual highlighting and checked state
- **Multi-select controls**: When enabled, additional UI elements appear:
  - Show Select All checkbox at top (if showSelectAll=true)
  - Clear and Apply buttons in footer (if confirmOnApply=true)
  - Selection count display (if totalSelected=true)

**Multi-select value handling**:
```typescript
// Initial state - no selections
value = []

// After selecting "US" and "CA"  
value = ["us", "ca"]

// After deselecting "CA"
value = ["us"]
```

**Important relationship with separator prop**: In multi-select mode, the separator prop controls how multiple selected values are displayed in the dropdown field. For example, if separator=", " and value=["us", "ca"], the field might display "United States, Canada" or "2 selected" (if totalSelected=true).

**Important relationship with multi-select specific props**: Several props only have function when multiSelect=true:
- separator: Controls display string between selected option labels
- totalSelected: Shows "X selected" count instead of listing labels
- showSelectAll: Displays Select All checkbox at top of dropdown
- confirmOnApply: Adds Apply/Clear buttons for confirmation workflow
- maxSelection: Limits total number of selections across all options
- groupMaxSelection: Limits number of selections per option group
- allSelectionValue: Custom text to show when all options selected

**Mobile experience changes**:
- **Without confirmOnApply**: Mobile multi-select works identically to desktop - selections update immediately
- **With confirmOnApply**: Mobile shows full-screen drawer with Apply/Clear actions, requiring explicit confirmation (Apply) or cancellation (Clear)

**Code example - multi-select setup**:
```typescript
// Enable multi-select
multiSelect = true;

// Limit to maximum 5 selections
maxSelection = 5;

// Show "Select All" checkbox
showSelectAll = true;

// Display "5 selected" instead of listing all value labels when many selected
totalSelected = true;

// Separator between labels when not showing count
separator = ", ";

// Confirmation workflow
confirmOnApply = true;
```

This prop is behavioral and fundamentally changes the dropdown's interaction model. It activates and enables numerous multi-select-specific features that are not available in single-select mode.

## separator

Controls the text string used to join multiple selected option labels when displaying them in the dropdown field. This is a visual/content prop that only applies in multi-select mode (multiSelect=true) and affects how multiple selected values are formatted for display in the field.

**Separator behavior and usage**:

- **separator not set (defaults to ", ")**: Multiple selected option labels are joined with a comma and space, creating a readable list. For example, if options ["United States", "Canada", "Mexico"] are selected, the field displays: "United States, Canada, Mexico"

- **separator set to custom string**: Multiple selected option labels are joined with the provided string. This allows customization for different formatting preferences:
  - comma separator (", " - default): "United States, Canada, Mexico"
  - vertical bar separator (" | "): "United States | Canada | Mexico"  
  - semicolon separator ("; "): "United States; Canada; Mexico"
  - dash separator (" - "): "United States - Canada - Mexico"
  - custom separator (" // "): "United States // Canada // Mexico"

**Important relationship with multiSelect**: The separator prop only has an effect when multiSelect=true. In single-select mode, there's only one selected option, so no joining is needed and separator is ignored.

**Important relationship with totalSelected**: When totalSelected=true, the separator prop has no effect because instead of listing individual option labels, the field displays something like "3 selected" (the count instead of the values). The separator only applies when the field displays the actual option labels.

**Visual presentation**: The separator is inserted between each option label when multiple selections are displayed in the field. The separator text itself appears in the same color/weight as the option labels, creating a cohesive visual appearance. The separator does NOT appear after the last item.

**Use cases**:

- **Standard comma separator (default)**: Most readable for general multi-select, follows standard English comma-separated list format
- **Vertical bar separator**: Visually creates distinct separation between options, useful for options where comma separation might be confusing (e.g., when option labels themselves contain commas)
- **Semicolon separator**: Alternative to comma when you want visual distinction from typical list formatting
- **Custom separators**: When your application has a specific formatting requirement or brand guidelines

**Code examples**:
```typescript
// Default behavior - comma separated
separator = ", "; // "US, Canada, Mexico"

// Vertical bar separation
separator = " | "; // "US | Canada | Mexico"

// No separator (ingets concatenated)
separator = ""; // "USCanadaMexico"

// Bulleted appearance
separator = " • "; // "US • Canada • Mexico"
```

This prop is visual/content-focused and only applies in multi-select mode. It affects how multiple selected values are formatted for display in the dropdown field.

## totalSelected

When true and multiSelect=true, displays the count of selected options (e.g., "3 selected") in the dropdown field instead of listing all selected option labels. This is a visual prop that provides a condensed display for multi-select, especially useful when many options are selected and listing all labels would be unwieldy.

**Total selected behavior**:

- **totalSelected=false (default)**: The dropdown field displays the labels of all selected options, separated by the separator string. For example, if options ["United States", "Canada", "Mexico"] are selected and separator=", ", the field displays: "United States, Canada, Mexico"

- **totalSelected=true**: The dropdown field displays a count of how many options are selected instead of listing the labels. For example, if 3 options are selected, the field displays "3 selected". The exact text format follows the design system's localized strings.

**Important relationship with multiSelect**: The totalSelected prop only has an effect when multiSelect=true. In single-select mode, there's only ever 0 or 1 selected options, so a count display would be redundant ("0 selected" or "1 selected" simply conveys the same information as the blank field or single selection).

**Important relationship with separator**: When totalSelected=true, the separator prop is ignored because no option labels are being joined. The field displays a single count string instead of formatted option labels, so separator has no role.

**Important relationship with allSelectionValue**: When both totalSelected=true and allSelectionValue is set, the behavior varies based on whether all options are selected:
- **Not all options selected**: Shows "X selected" count (e.g., "3 selected")
- **All options selected**: Shows the custom allSelectionValue text instead of the count (e.g., "All countries selected")

**Use cases**:
- **Many selections selected**: When dozens of options are selected, listing all labels is overwhelming - totalSelected=true provides cleaner display ("25 selected" instead of listing 25 country names)
- **Count-based summary**: When you need a count of selections for display purposes rather than the specifics
- **Clean appearance**: When you want a more minimalist, less cluttered user interface

**Code example**:
```typescript
// Enable multi-select
multiSelect = true;

// Set max selections  
maxSelection = 10;

// Use count display instead of listing
totalSelected = true;

// Custom text when all selected
allSelectionValue = "All countries selected";
```

This prop is visual and only applies in multi-select mode. It dramatically affects how multiple selections are displayed in the dropdown field.

## showSelectAll

When true and multiSelect=true, displays a Select All checkbox at the top of the dropdown menu above the option list. This checkbox allows users to select or deselect all options with a single click. This is a behavioral/visual prop that provides a convenient way to manipulate all selections.

**Show Select All behavior**:

- **showSelectAll=false (default)**: No Select All checkbox is displayed. Users must select or deselect options individually.

- **showSelectAll=true**: A Select All checkbox appears at the top of the dropdown menu, above the first option group or option. The checkbox has three states:
  - **Unchecked**: All options are deselected
  - **Checked**: All selectable options are selected
  - **Indeterminate**: Some (but not all) selectable options are selected

**Important relationship with multiSelect**: The showSelectAll prop only has an effect when multiSelect=true. In single-select mode, "select all" is meaningless since only one option can be selected.

**Select All state logic**:
- When all selectable options (excluding disabled options) are selected → checkbox is checked
- When no selectable options are selected → checkbox is unchecked
- When some but not all selectable options are selected → checkbox is indeterminate (displayed as a dash/minus)
- Disabled options do not affect the Select All state - they are excluded from "all" calculations

**Select All checkbox interaction**:
- **Clicking when unchecked**: Selects all selectable options in the dropdown (disabled options remain unselected)
- **Clicking when checked**: Deselects all options in the dropdown (no options selected)
- **Indeterminate state typically resolves to checked when clicked** (selects remaining unselected options)

**Positioning**: The Select All checkbox appears at the very top of the dropdown menu, before any option groups or individual options. It's visually distinct from regular options (typically has a different background and contains text like "Select All").

**Accessibility**: The Select All checkbox should have proper ARIA labeling so screen readers recognize it as a special control that affects all options. The component should announce changes like "Select All, checked, 5 options selected" or "Select All, not checked, 0 options selected."

**Important relationship with disabled options**: Select All only affects selectable (enabled) options. Disabled options remain disabled regardless of Select All state. If there are 10 options but 2 are disabled, Select All would only select the 8 enabled options.

**Use cases**:
- **Large option sets**: When there are many options and users frequently need to select most or all of them
- **Bulk selection**: When the workflow involves selecting most options and then deselecting a few exceptions
- **Convenience**: When users commonly work with "select all except X" patterns

**Code example**:
```typescript
// Enable multi-select
multiSelect = true;

// Show Select All checkbox for bulk selection
showSelectAll = true;

// Limit to 10 total selections (Select All enforces this limit too)
maxSelection = 10;
```

This prop is behavioral/visual and only applies in multi-select mode. It adds a convenient bulk selection feature when working with option lists.

## confirmOnApply

When true and multiSelect=true, adds Apply and Clear buttons to the dropdown footer and requires explicit confirmation before committing selections. This is a behavioral prop that changes multi-select from immediate-updating to a confirmation workflow.

**Confirm on Apply behavior**:

- **confirmOnApply=false (default)**: Multi-select works with immediate updates - when users select or deselect options, the value updates immediately. No confirmation buttons are displayed.

- **confirmOnApply=true**: Multi-select works with confirmation workflow - users can select/deselect multiple options in the dropdown, but changes are not committed until they click the Apply button. The Clear button deselects all options. The dropdown displays two buttons at the bottom:

**Apply button**:
- Only enabled when at least one option is selected and selections differ from initial state
- Clicking commits the selections (fires valueChange with committed=true)
- After clicking, the dropdown closes and selected options appear in the field
- Button text is "Apply" or localized equivalent

**Clear button**:
- Always enabled when any options are selected
- Clicking deselects all options (fires valueChange with committed=false)
- After clicking, selections are cleared but dropdown remains open
- Button text is "Clear" or localized equivalent

**Important relationship with multiSelect**: The confirmOnApply prop only has an effect when multiSelect=true. In single-select mode, selections are always updated immediately (there's nothing to "confirm" since each selection replaces the previous one).

**Important relationship with clearButton**: When confirmOnApply=true, the clearButton prop is ignored/not displayed. The confirmation workflow provides its own Clear button in the footer, which serves the purpose of clearing selections. You would use either:
- clearButton=true for immediate clearing in single-select or multi-select without confirmation
- confirmOnApply=true for confirmation workflow with own Clear button

**Confirmation workflow state**:
1. **Dropdown opens**: Empty selections (or previous selections if maintaining state)
2. **User selects/deselects options**: Selections are tracked internally but not committed yet
3. **Apply click**: Selections committed (fires valueChange event), dropdown closes, field reflects new selections
4. **Clear click**: All selections deselected (fires valueChange event), dropdown remains open for new selections
5. **Close without Apply**: If dropdown is closed without Apply, changes are abandoned (unless you've maintained preview)

**Mobile experience**: When confirmOnApply=true and the dropdown opens as a full-screen drawer on mobile, the Apply/Clear buttons appear at the top (or bottom) of the drawer for easy access. This provides a mobile-optimized confirmation experience.

**Accessibility**: The Apply and Clear buttons should have proper ARIA attributes. Focus management should ensure keyboard users can navigate to and operate these buttons. The confirmation state should be clearly communicated to screen readers.

**Use cases**:
- **Form submission workflow**: When you want users to review their multi-select selections before submitting
- **Performance optimization**: When option selection triggers expensive operations and you want to defer until explicit confirmation
- **User control**: When you want users to have explicit control over when their selections are committed
- **Complex forms**: When multi-select is just one step in a larger form setup wizard

**Code example**:
```typescript
// Enable multi-select
multiSelect = true;

// Set maximum 10 selections
maxSelection = 10;

// Use confirmation workflow instead of immediate updates
confirmOnApply = true;

onValueChange(event) {
  if (event.detail.committed) {
    // Selections are finalized - commit to your state
    this.selectedCountries = event.detail.value;
  } else {
    // Preview state - selections may change before Apply
    this.previewCountries = event.detail.value;
  }
}
```

This prop is behavioral and only applies in multi-select mode. It changes multi-select from immediate-updating to a confirmation workflow with explicit Apply/Clear buttons.

## allSelectionValue

Provides custom text to display in the dropdown field when all options are selected and totalSelected=true. This is a content prop that allows customization of the display text when every selectable option is chosen.

**All selection value behavior**:

- **allSelectionValue not set**: When all options are selected and totalSelected=true, the dropdown displays the count pattern "{N} selected" where N is the number of options. For example, "10 selected" for 10 options.

- **allSelectionValue set (e.g., allSelectionValue="All countries selected")**: When all options are selected and totalSelected=true, the dropdown displays your custom text instead of the count. For example, "All countries selected" instead of "10 selected".

**Important relationship with totalSelected**: The allSelectionValue prop only has an effect when totalSelected=true. When totalSelected=false, the dropdown displays the actual option labels separated by the separator, so there's no special "all selected" display to customize.

**Important relationship with multiSelect**: The allSelectionValue prop only has an effect when multiSelect=true. In single-select mode, there's no concept of "all options selected" since only one is ever selected.

**All options detection**: The component determines "all options selected" based on the count of selectable options (excluding disabled options). If there are 10 total options but 2 are disabled, then selecting the 8 selectable options triggers the "all selected" state and displays the custom allSelectionValue text.

**Use cases**:
- **Custom messaging**: When you want the field to say something more descriptive than just the count when all options are selected
- **Branding/language**: When the count message is too generic and you want more specific text
- **User experience**: When you want to provide clearer feedback when all options are selected (e.g., "All countries selected" vs "10 selected")

**Code examples**:
```typescript
// Enable multi-select with total count display
multiSelect = true;
totalSelected = true;

// Custom text for all selected state
allSelectionValue = "All regions selected";

// Examples of display behavior:
// When 3 of 10 options selected: "3 selected"
// When all 10 options selected: "All regions selected"
```

This prop is content-focused and only applies when both multiSelect=true and totalSelected=true. It allows customization of the display message when every selectable option is selected.

## maxSelection

Limits the maximum number of options that can be selected in multi-select mode. This is a behavioral prop that enforces selection limits and prevents users from selecting more options than allowed.

**Max selection behavior**:

- **maxSelection not set (or undefined)**: No limit on the number of selected options in multi-select. Users can select as many options as exist in the dropdown, up to all options.

- **maxSelection set to number (e.g., maxSelection=5)**: Users can only select up to the specified number of options. When the limit is reached:
  - Additional options become disabled/unclickable
  - Users must deselect existing selections before selecting additional options
  - Visual indication shows when at the limit (typically disabled appearance on remaining options)
  - Selections are prevented beyond the limit, enforced by the component

**Important relationship with multiSelect**: The maxSelection prop only has an effect when multiSelect=true. In single-select mode, the limit of 1 is inherent, and specifying maxSelection doesn't change behavior.

**Important relationship with groupMaxSelection**:
- **maxSelection**: Limits total selections across ALL options and ALL groups combined
- **groupMaxSelection**: Limits selections per individual option group

Both limits can be set simultaneously, and both must be satisfied. For example:
- maxSelection=5 AND groupMaxSelection=2 with 3 groups means:
  - Total selections cannot exceed 5 across all groups
  - Each of the 3 groups cannot have more than 2 selections independently
  - So possible distribution could be: Group1:2 + Group2:2 + Group3:1 = 5 total (valid)
  - But distribution like Group1:3 + Group2:1 + Group3:1 = 5 total (invalid, exceeds group limit)

**Disabled options don't count toward max**: The maxSelection limit only counts selectable (non-disabled) options. If there are 15 total options but 3 are disabled, maxSelection=5 means users can select up to 5 of the 12 selectable options.

**Show Select All interaction with maxSelection**: When showSelectAll=true and maxSelection is set, clicking Select All selects up to the max limit, not necessarily all options. If there are 10 options and maxSelection=5, clicking Select All selects the first 5 selectable options.

**Use cases**:
- **Resource allocation**: Limiting selections when selecting too many consumes too much resource
- **Data limits**: Preventing selection of too many items for data processing limits
- **Business rules**: Enforcing business constraints (e.g.,最多选择3个因素进行对比)
- **Performance**: Preventing excessive selections that would impact performance

**Code example with multiple limits**:
```typescript
// Enable multi-select
multiSelect = true;

// Set total limit across all options
maxSelection = 5;

// Set per-group limit
groupMaxSelection = 2;

// Show Select All while respecting limits
showSelectAll = true;
```

This prop is behavioral and only applies in multi-select mode. It enforces selection limits at the total level, working in combination with groupMaxSelection for individual group limits.

## groupMaxSelection

Limits the maximum number of options that can be selected from each individual option group in multi-select mode. This is a behavioral prop that enforces per-group selection limits while the overall multi-select limit (maxSelection) controls the total across all groups.

**Group max selection behavior**:

- **groupMaxSelection not set (or undefined)**: No per-group limit on selections within option groups. Users can select any number of options from each group, subject only to the overall maxSelection limit.

- **groupMaxSelection set to number (e.g., groupMaxSelection=2)**: Users can only select up to the specified number of options within each individual option group. When the limit is reached for a group:
  - Additional options in that group become disabled/unclickable
  - Users can still select options from other groups (subject to their per-group limits and overall maxSelection)
  - Visual indication shows when group limit is reached (typically disabled appearance on remaining options in that group)
  - Selections per group are prevented beyond the limit

**Important relationship with multiSelect**: The groupMaxSelection prop only has an effect when multiSelect=true. In single-select mode and when options aren't grouped, per-group limits don't apply.

**Important relationship with maxSelection**:
- **maxSelection**: Limits total selections across ALL options and ALL groups combined
- **groupMaxSelection**: Limits selections per individual option group

Both limits can be set simultaneously, and both must be satisfied. Example:
```typescript
// 3 groups with 4 options each
options = [
  { label: "Americas", items: [US, CA, MX, BR] },
  { label: "Europe", items: [UK, FR, DE, ES] },
  { label: "Asia", items: [JP, CN, IN, KR] }
];

// Limits: 5 total, 2 per group
maxSelection = 5;
groupMaxSelection = 2;

// Valid distributions:
// A: 2 Americas + 2 Europe + 1 Asia = 5 total ✓
// B: 1 Americas + 2 Europe + 2 Asia = 5 total ✓

// Invalid distributions:
// C: 3 Americas + 1 Europe + 1 Asia = 5 total ✗ (exceeds Americas group limit)
// D: 2 Americas + 3 Europe + 0 Asia = 5 total ✗ (exceeds Europe group limit)
```

**Ungrouped options with groupMaxSelection**: Ungrouped options (options not wrapped in a group structure) are treated as part of a single "ungrouped" group for the purposes of groupMaxSelection. So if groupMaxSelection=2 and there are ungrouped options, you can select at most 2 from the pool of ungrouped options.

**Show Select All with per-group limits**: When showSelectAll=true and groupMaxSelection is set, clicking Select All respects the per-group limits, selecting up to groupMaxSelection items from each group rather than all items.

**Independent group limits**: Each group has its own limit. Reaching the limit in one group doesn't affect the limits of other groups. Users can continue selecting from other groups up to their respective groupMaxSelection values.

**Use cases**:
- **Balanced selections**: Enforcing even distribution across categories (e.g.,最多选择2个亚洲国家)
- **Category-specific rules**: Applying different business rules to different groups
- **Fair selections**: Preventing excessive selection from any single category
- **Resource allocation by group**: Managing selections per resource category independently

**Code example with grouped limits**:
```typescript
// Enable multi-select
multiSelect = true;

// Options organized by region/continent groups
options = [
  { label: "Americas", items: [US, CA, MX, BR] },  // 4 options
  { label: "Europe", items: [UK, FR, DE, ES, IT] },  // 5 options  
  { label: "Asia", items: [JP, CN, IN, KR, SG, MY] }  // 6 options
];

// Limit per group
groupMaxSelection = 2;

// Optionally also limit total
maxSelection = 5;
```

This prop is behavioral and only applies in multi-select mode with grouped options. It enforces per-group selection limits, working in combination with maxSelection for total limits.

## dropdownWidth

Controls the width of the dropdown panel/menu that appears when the dropdown opens. This is a visual prop that determines how wide the options list is displayed, independent of the field's width.

**Dropdown width behavior**:

- **dropdownWidth="auto" (default)**: The dropdown panel inherits the width of the dropdown field itself. The panel appears with the same width as the field, creating visual alignment. This is the most common behavior and creates a cohesive appearance where the options list matches the field width.

- **dropdownWidth="none"**: The dropdown panel uses its content-based width rather than inheriting the field's width. The panel expands or contracts to fit the widest option's content, potentially wider or narrower than the field. This can be useful when options are very long or very short and you want them displayed without truncation or excessive whitespace.

- **dropdownWidth="custom CSS width" (e.g., "300px", "80%", "20rem")**: The dropdown panel has the specified custom width, regardless of the field's width. This allows you to:
  - Make the panel wider than the field (e.g., dropdownWidth="600px") when options are very long and need more horizontal space
  - Make the panel narrower than the field (e.g., dropdownWidth="200px") for compact display
  - Use percentage-based widths (e.g., dropdownWidth="80%") relative to viewport or container
  - Use responsive units (e.g., dropdownWidth="clamp(200px, 50vw, 400px)") for adaptive width

**Important relationship with field width**: The dropdownWidth specifically controls the panel/menu width, not the field width. The field's width is controlled by the containing layout and any width constraints on the dropdown component. The dropdownWidth applies to the floating/popover content that appears when the dropdown is opened.

**Visual positioning and alignment**: Regardless of the dropdownWidth, the panel is typically aligned with the field. When dropdownWidth="auto", the panel aligns with the field edges because they match in width. With custom widths, the panel may extend beyond (wider) or be contained within (narrower) the field's horizontal space.

**Interaction with long options**: If options are very long and dropdownWidth is narrow:
- Auto width (="auto"): Field must be wide enough to accommodate longest option, or truncation occurs
- None width (="none"): Panel expands to fit content, possibly wider than field  
- Custom width: Set a width that accommodates your content needs

**Use cases**:
- **_aligned appearance (="auto")**: Most common, creates cohesive field+panel alignment
- **Content-driven width (="none")**: Let content determine panel width to avoid truncation
- **Wider than field**: When field is narrow but options are long and need horizontal space
- **Narrower than field**: When you want compact panel display even in wide fields
- **Responsive width**: Use percentage or viewport units for adaptive sizing

**Code examples**:
```typescript
// Align panel width with field width (most common)
dropdownWidth = "auto";

// Let content determine panel width
dropdownWidth = "none";

// Make panel wider than field for long options
dropdownWidth = "600px";

// Use responsive width based on viewport
dropdownWidth = "min(600px, 80vw)";
```

This prop is visual and controls the dropdown menu/panel width independently of the field width. It affects the appearance and layout of the options list when the dropdown is opened.

## dropdownHeight

Controls the height behavior of the dropdown panel/menu. This is a visual prop that determines how the dropdown panel's height is calculated and displayed, particularly relevant for scrolling behavior with many options.

**Dropdown height behavior**:

- **dropdownHeight="default" (default)**: The dropdown panel has a calculated height based on typical dropdown behavior. This usually means:
  - Fixed or maximum height is set based on design system tokens
  - Content beyond the calculated height scrolls vertically
  - Height is appropriate for the number of options but constrained to reasonable limits
  - For example, maximum height might be 300px or similar design system value

- **dropdownHeight="full"**: The dropdown panel takes up more vertical space, often extending to a larger portion of the viewport. This is particularly useful for:
  - Displays where you want maximum visibility of options
  - Scenarios where users are expected to review many options
  - Desktop interfaces where more vertical space is available than mobile
  - Used in conjunction with virtual scrolling for very large option lists

**Important relationship with virtual scrolling**: When virtualScroll=true (enabled automatically for option lists with ≥15 items), dropdownHeight="full" becomes especially relevant. The full height allows the dropdown panel to use more viewport height, which means:
- More options are visible without scrolling
- Virtual scrolling has more space to render options before they're out of viewport
- Performance benefits of virtual scrolling are maximized
- User can see more items at once when deciding what to select

**Important relationship with mobile presentation**: On mobile devices where the dropdown opens as a full-screen drawer, dropdownHeight="full" maximizes the available vertical space within the drawer (typically 75% of viewport height). This provides the best mobile experience for option browsing.

**Scrolling behavior**: With dropdownHeight="default", the dropdown panel has a fixed/max height and scrolls internally when content exceeds that height. With dropdownHeight="full", the panel uses more vertical space and therefore:
- Less internal scrolling is needed for the same number of options
- Initial view shows more options at once
- Better visibility reduces the need to scroll through long lists

**Visual presentation**: Height settings primarily affect the dropdown panel size, not the options themselves. Options are rendered at the same size regardless of dropdownHeight - just more or fewer are visible at once.

**Responsive consideration**: In some implementations, dropdownHeight may have different effects at different viewport sizes. For example, "full" height on mobile might use all available drawer space, while on desktop it might use a larger percentage of viewport.

**Use cases**:
- **Standard behavior (="default")**: Most dropdowns use default height, which provides good balance of visibility and space efficiency
- **Maximum visibility (="full")**: When you want users to see as many options as possible, especially for very large option lists
- **Virtual scrolling synergy**: When virtual scrolling is enabled, "full" height provides the best performance and user experience
- **Mobile optimization**: Full height in mobile drawer mode provides best mobile option browsing experience

**Code example with virtual scrolling**:
```typescript
// Long option list (triggers virtual scrolling automatically)
options = [...150 country options]; // 150 items

// Use full height for better visibility in large list
dropdownHeight = "full";

// Can also explicitly set virtualScroll, though it auto-enables for ≥15 items
virtualScroll = true;
```

This prop is visual and affects the dropdown panel's height behavior and scrolling characteristics. It's particularly relevant for large option lists and works well with virtual scrolling.

## headerElement

Allows injection of custom header content at the top of the dropdown panel, above the option list. This is a content prop that accepts either an IonElement function that returns an HTMLElement, or a raw string. This prop provides the ability to add custom content to the dropdown header for branding, instructions, or other UI elements.

**Header element behavior and types**:

The headerElement prop accepts two formats:

1. **IonElement function**:
```typescript
headerElement = () => {
  return <HTMLElement>document.querySelector('.my-custom-header-template');
}
```

2. **String**:
```typescript
headerElement = "Select up to 5 countries for comparison";
```

**Visual positioning**: The header element appears at the very top of the dropdown panel, above any Select All checkbox and above the first option group or individual option. The header content is integrated into the dropdown panel's flow and scrolls with the dropdown content.

**Important relationship with mobile presentation**: On mobile devices where the dropdown opens as a full-screen drawer, the headerElement appears at the top of the drawer, maintaining consistent positioning relative to the content.

**Content types and use cases**:

**Text header (string format)**:
- Provides instructional text at the top of the dropdown
- Useful for context like "Select up to 5 regions" or "Most popular countries listed first"
- Serves similar purpose to helperMessage but appears inside the dropdown panel

**Custom HTML header (IonElement function)**:
- Provides complete control over header content and styling
- Can include icons, buttons, links, or any HTML content
- Useful for complex headers like search indicators, filters, or advanced controls

**Important behavior with confirmOnApply**: When confirmOnApply=true and Apply/Clear buttons are shown, the headerElement positioning is adjusted to appear with proper spacing from these buttons, ensuring visual hierarchy is maintained.

**Common header use cases**:
- **Instructions**: Add guidance like "Select your top 3 preferences"
- **Search indicator**: Show when search is affecting the displayed options
- **Filters/controls**: Add sorting buttons, filter controls at panel top
- **Branding**: Include logos or branding elements in the dropdown
- **Context**: Explain business rules or constraints relevant to the dropdown

**Code examples**:
```typescript
// Simple text header
headerElement = "Select up to 5 countries";

// Custom HTML header with filter controls
headerElement = () => {
  return this.customHeaderTemplate.nativeElement;
}

// Dynamic header based on state
headerElement = () => {
  const headerText = this.showAllCountries 
    ? "All countries available" 
    : "Popular countries shown first";
  return `<div class="dropdown-header">${headerText}</div>`;
}
```

This prop is content-focused and allows custom header injection at the top of the dropdown panel. It works with the dropdown's presentation modes and custom content strategies.

## footerElement

Allows injection of custom footer content at the bottom of the dropdown panel, below the option list. This is a content prop that accepts either an IonElement function, an HTMLElement, or a raw string. This prop provides the ability to add custom content to the dropdown footer for additional controls, information, or UI elements.

**Footer element behavior and types**:

The footerElement prop accepts three formats:

1. **IonElement function**:
```typescript
footerElement = () => {
  return <HTMLElement>document.querySelector('.my-custom-footer-template');
}
```

2. **HTMLElement**:
```typescript
footerElement = this.footerTemplate.nativeElement;
```

3. **String**:
```typescript
footerElement = "Press Enter to select or Esc to cancel";
```

**Visual positioning**: The footer element appears at the bottom of the dropdown panel, below all options and option groups. If confirmation buttons are present (confirmOnApply=true), the footerElement is positioned above or below these buttons depending on the design system implementation.

**Important relationship with mobile presentation**: On mobile devices where the dropdown opens as a full-screen drawer, the footerElement appears at the bottom of the drawer, providing a consistent footer position across desktop and mobile.

**Important relationship with confirmOnApply**: When confirmOnApply=true, Apply and Clear buttons appear in the dropdown footer area. If footerElement is also provided, the content is arranged to integrate properly with these buttons - typically the custom footerElement appears above the confirmation buttons, maintaining logical user interaction flow.

**Content types and use cases**:

**Text footer (string format)**:
- Provides instructional text or shortcuts at the bottom
- Useful for keyboard shortcut hints like "Press Enter to confirm"
- Can show context-specific guidance like "Selection updates saved automatically"

**Custom HTML footer (IonElement/HTMLElement)**:
- Provides complete control over footer content and styling  
- Can include buttons, links, status indicators, charts, or any HTML content
- Useful for complex footers like save actions, progress indicators, or summary displays

**Common footer use cases**:
- **Keyboard shortcuts**: Show hints for power users (e.g., "Enter:Select, Esc:Cancel")
- **Additional actions**: Add secondary actions that complement the dropdown selection
- **Status indicators**: Display selection count, status, or validation feedback in the footer
- **Context information**: Provide details about selection limits or business rules
- **Branding**: Include additional branding elements in the footer area

**Code examples**:
```typescript
// Simple text footer
footerElement = "Use arrow keys to navigate, Enter to select";

// Custom HTML footer with action buttons
footerElement = this.footerTemplate.nativeElement;

// React-like template example
footerElement = () => {
  return <div class="dropdown-footer">
    <button (click)="this.customAction()">Custom Action</button>
  </div>;
}

// Dynamic footer based on selections
footerElement = () => {
  const count = this.selectedCount;
  const limit = this.maxSelection;
  return `Selected: ${count} / ${limit}`;
}
```

This prop is content-focused and allows custom footer injection at the bottom of the dropdown panel. It integrates with the dropdown's interaction modes and provides flexible customization for footer content.

## focus

Programmatic method to give the dropdown component focus. This is a behavioral method prop that allows you to set focus to the dropdown from elsewhere in your application, which is useful for accessibility, user experience, or keyboard-based workflows.

**Focus behavior**:

The focus prop is a method (function) rather than a configuration prop. You call it programmatically to set focus to the dropdown field:

```typescript
// Call focus method to set focus
this.dropdownComponent.focus();
```

**What happens when focus is called**:
- The dropdown field becomes the currently focused element in the page
- Keyboard users can immediately interact with the dropdown (type to open, arrow keys, etc.)
- Screen readers announce the dropdown's label and value to users
- Visual focus indicator appears around the dropdown field
- When the dropdown has focus, pressing Space or Enter opens the options list (unless disabled or read-only)

**Common use cases for programmatic focus**:
- **Error handling**: Set focus to a problem field after form validation errors
- **Dialog/modals**: Set focus to the first interactive field when a dialog opens
- **Sequential workflow**: Automatically focus the next field after completing the previous one
- **Quick access**: Focus shortcut keys allow users to jump to specific dropdowns
- **Accessibility**: Ensure proper focus management for keyboard-only users
- **Scripted interactions**: Focus dropdown from button clicks or other user actions

**Relationship with autoFocus**: The focus method sets focus immediately when called, while the autoFocus prop sets focus when the component initially loads. The focus method is more flexible and can be called at any time.

**Focus management patterns**:
```typescript
// Focus on error
onSubmit(form) {
  if (!form.valid && form.errors.countryRequired) {
    this.countryDropdown.focus(); // Focus dropdown with required error
  }
}

// Focus after previous field completion
onPreviousFieldComplete() {
  // User completed previous field, advance to dropdown
  this.countryDropdown.focus();
}

// Focus from keyboard shortcut
 onKeyDown(event) {
  if (event.key === 'k' && event.altKey) {
    this.countryDropdown.focus(); // Alt+K focuses country dropdown
  }
}
```

This prop is a behavioral method (not configuration) that allows programmatic focus control. It doesn't affect visual appearance directly but affects interaction state and accessibility.

## blur

Programmatic method to remove focus from the dropdown component. This is a behavioral method prop that allows you to programmatically remove focus from the dropdown field, which is useful for managing focus flow, validation timing, or keyboard-based workflows.

**Blur behavior**:

The blur prop is a method (function) rather than a configuration prop. You call it programmatically to remove focus from the dropdown field:

```typescript
// Call blur method to remove focus
this.dropdownComponent.blur();
```

**What happens when blur is called**:
- The dropdown field loses focus as the currently focused element
- Visual focus indicator disappears from the dropdown field
- Focus moves away (either to next element in tab order or back to body window depending on context)
- If the dropdown was open, it may close (depending on configuration and user interaction)
- Screen readers announce that focus moved away from the dropdown
- If validationMode=onBlur, validation may execute (losing focus may trigger validation)

**Common use cases for programmatic blur**:
- **Validation timing**: Trigger onBlur validation programmatically rather than waiting for user to tab away
- **Focus management**: Move focus away from dropdown after selection or action completion
- **Dialog workflows**: Close dialogs and remove focus from elements when dismissed
- **Auto-save workflows**: Save data when dropdown loses focus (called blur programmatically)
- **Sequential workflows**: Manage focus flow through complex forms with custom timing
- **Error clearing**: Clear validation states when programmatically blurring problematic fields

**Relationship with validation**: When blur is called programmatically, validation may execute if validationMode=onBlur is set. This is intentional for some workflows but may be unexpected if blur is called for non-validation reasons.

**Focus vs blur patterns**:
```typescript
// Flow: Select → Validate → Continue
onCountrySelect() {
  // User selected country
  this.validateCountry();   // Validate selection
  this.countryDropdown.blur(); // Remove focus after validation
  this.nextField.focus();   // Move to next field
}

// Dialog dismissal pattern
closeDialog() {
  this.countryDropdown.blur(); // Remove focus before dialog closes
  this.dialogVisible = false;
}

// Clear validation on blur
onClearValidation() {
  this.countryDropdown.blur(); // Remove focus
  this.validationState = "none"; // Clear validation state
  this.helperMessage = ""; // Clear validation message
}
```

**Important behavior with open dropdown**: Calling blur() when the dropdown menu is open typically closes the menu, as if the user clicked outside. This is consistent with losing focus normally triggering menu closure.

This prop is a behavioral method (not configuration) that allows programmatic focus removal. It doesn't affect visual appearance directly but manages interaction state and can trigger validation depending on validationMode settings.

## closeDropdown

Programmatic method to close the dropdown panel/menu when it's currently open. This is a behavioral method prop that allows you to close the dropdown from elsewhere in your application, which is useful for managing dropdown state, responding to external events, or implementing custom UX patterns.

**Close dropdown behavior**:

The closeDropdown prop is a method (function) rather than a configuration prop. You call it programmatically to close the dropdown menu:

```typescript
// Call closeDropdown method to close menu
this.dropdownComponent.closeDropdown();
```

**What happens when closeDropdown is called**:
- The dropdown panel/menu closes if it's currently open
- If the dropdown is already closed, calling closeDropdown has no effect
- Visual appearance returns to the collapsed state (only the field is visible)
- Dropdown state resets appropriately (e.g., focused item tracking may reset)
- Screen readers are notified that the dropdown is collapsed
- Focus returns to the dropdown field (the trigger element) for continued interaction
- Any temporary selections or hover states in the menu are cleared

**Common use cases for programmatic close**:
- **External events**: Close dropdown when something else happens in the interface (e.g., external control changed context)
- **Timer-based closing**: Auto-close dropdown after inactivity (e.g., "If nothing selected in 30 seconds, close")
- **Coordination**: Close dropdown when another dropdown in the same group opens (ensure only one open at a time)
- **Form actions**: Close dropdowns when users click form submission or cancel buttons
- **Error handling**: Close dropdowns when validation errors occur elsewhere in form
- **UX patterns**: Implement "click outside to close" behavior for additional elements
- **State management**: Close dropdowns when application state changes make current options irrelevant

**Usage patterns**:
```typescript
// External event triggers close
onExternalDataChanged() {
  // New data available, close dropdown to refresh
  this.countryDropdown.closeDropdown();
  this.refreshCountryOptions();
}

// Timer-based auto-close
openDropdown() {
  setTimeout(() => {
    this.countryDropdown.closeDropdown();
  }, 30000); // Close after 30 seconds if inactive
}

// Form action closes dropdowns
onFormSubmit() {
  this.countryDropdown.closeDropdown();
  this.stateDropdown.closeDropdown();
  this.submitForm();
}

// Keyboard shortcut closes dropdown
onKeyDown(event) {
  if (event.key === 'Escape') {
    this.countryDropdown.closeDropdown();
  }
}
```

**Relationship with openDropdown**: closeDropdown is the programmatic opposite of openDropdown. One closes an open dropdown, the other opens a closed dropdown. Together they provide complete programmatic control over dropdown open/closed state beyond user click interactions.

**Mobile behavior**: On mobile where the dropdown opens as a full-screen drawer, closeDropdown closes the drawer (equivalent to user tapping the close/back button or swiping down).

This prop is a behavioral method that provides programmatic control over dropdown open/closed state. It's particularly useful for coordinating with other interface elements, implementing custom UX patterns, and managing complex form workflows.

## openDropdown

Programmatic method to open the dropdown panel/menu when it's currently closed. This is a behavioral method prop that allows you to open the dropdown from elsewhere in your application, which is useful for controlling UX patterns, responding to triggers, or implementing keyboard-based workflows.

**Open dropdown behavior**:

The openDropdown prop is a method (function) rather than a configuration prop. You call it programmatically to open the dropdown menu:

```typescript
// Call openDropdown method to open menu
this.dropdownComponent.openDropdown();
```

**What happens when openDropdown is called**:
- The dropdown panel/menu appears (opens) if it's not already open
- If the dropdown is already open, calling openDropdown has no effect
- Visual appearance changes to show the expanded options list
- Dropdown state initializes appropriately (focused item tracking sets to first or previously selected item)
- Screen readers are notified that the dropdown is expanded and announce the available options
- Focus either remains on the trigger element or moves to the first menu item depending on accessibility requirements
- When the dropdown is disabled or read-only, calling openDropdown has no effect (remains closed)

**Common use cases for programmatic open**:
- **Button triggers**: Clicking a button opens the dropdown (useful when dropdown field is hidden or replaced by button)
- **Keyboard shortcuts**: Open dropdowns via keyboard commands (e.g., Alt+C for country dropdown)
- **Sequential workflow**: Automatically open next dropdown after completing previous selection
- **Action triggers**: Open dropdown when another action occurs (e.g., user selects "Show more options")
- **External events**: Open dropdown in response to application state changes or user actions elsewhere
- **UX patterns**: Implement "click label to open dropdown" pattern where label becomes clickable
- **Focus management**: Open dropdown when custom focus management logic dictates it

**Usage patterns and UX examples**:
```typescript
// Button-triggered dropdown
onClickCountryButton() {
  this.countryDropdown.openDropdown();
}

// Keyboard shortcut opens dropdown
onKeyDown(event) {
  if (event.altKey && event.key === 'c') {
    this.countryDropdown.openDropdown(); // Alt+C opens country dropdown
  }
}

// Sequential workflow - auto-open next dropdown
onCountrySelected(country) {
  // User selected country, show states dropdown
  this.stateDropdown.openDropdown();
}

// Clickable label pattern
onLabelClick() {
  this.countryDropdown.openDropdown(); // Label click opens dropdown
}

// External event triggers dropdown
onContextChanged(context) {
  if (context.needsCountrySelection) {
    this.countryDropdown.openDropdown();
  }
}
```

**Important behavior with disabled/read-only**: If the dropdown is disabled=true or readOnly=true, calling openDropdown has no effect - the menu will not open. This prevents unintended opening when dropdowns should be non-interactive.

**Mobile behavior**: On mobile where the dropdown opens as a full-screen drawer, openDropdown opens the drawer, showing the full-screen overlay for mobile users.

**Relationship with closeDropdown**: openDropdown is the programmatic opposite of closeDropdown. Together they provide complete programmatic control over dropdown open/closed state beyond user click interactions.

**Accessibility considerations**: When programmatically opening dropdowns, ensure that focus is properly managed for screen reader users. The dropdown should receive focus or have proper ARIA state changes announced when it opens.

This prop is a behavioral method that provides programmatic control over dropdown open/closed state. It enables custom UX patterns and programmatic triggering beyond standard click interactions.

## refreshOptions

Programmatic method to reload/refresh the dropdown's options. This is a behavioral method prop that allows you to trigger an options reload when data has changed, which is particularly useful when options are provided via async functions or when the options data source has been updated.

**Refresh options behavior**:

The refreshOptions prop is a method (function) rather than a configuration prop. You call it programmatically to reload the dropdown's options:

```typescript
// Call refreshOptions method to reload options
this.dropdownComponent.refreshOptions();
```

**What happens when refreshOptions is called**:
- The dropdown re-executes its options loading logic
- For static array options: The options are re-processed (useful if options data changed in your application)
- For function options: The function is called again to retrieve updated options
- For async function options: The async function is called again, and the dropdown shows loading state if applicable while the Promise resolves
- The dropdown's internal value-label map is rebuilt from the refreshed options
- Currently selected values are preserved if they still exist in the refreshed options
- The dropdown's open/closed state is preserved (doesn't auto-close or auto-open)

**Common use cases for options refresh**:
- **Data updates**: Refresh options when underlying data has changed (e.g., country list updated)
- **Language/locale change**: Reload options when user changes language (options need new labels)
- **Context changes**: Refresh options when application context changes (e.g., region change affects available options)
- **Manual refresh**: Provide a refresh button that users can click to reload latest options
- **Race condition handling**: Reload options after async operations complete successfully
- **Incremental loading**: Previously had placeholder options, now has full list - refresh to load complete data
- **Filter/clear reset**: User clears or resets filters - refresh to show all options again

**Usage patterns and code examples**:
```typescript
// Refresh after data update
onCountryDataUpdated() {
  // Country list was updated in database
  this.fetchLatestCountries(); // Update our local data
  this.countryDropdown.refreshOptions(); // Reload dropdown options
}

// Refresh on language change
onLanguageChanged(newLanguage) {
  this.translateService.use(newLanguage).subscribe(() => {
    // Labels updated, refresh dropdown to use translated labels
    this.countryDropdown.refreshOptions();
  });
}

// Manual refresh button pattern
onRefreshClick() {
  this.loading = true;
  this.fetchLatestData().then(() => {
    this.countryDropdown.refreshOptions();
    this.loading = false;
  });
}

// Filter reset refreshes options
onClearFilters() {
  this.appliedFilters = none;
  this.countryDropdown.refreshOptions(); // Show all option again
}

// Async data loading with refresh
async loadCountriesFromAPI() {
  try {
    this.countries = await this.countryAPI.getCountries();
    // Options provided as function will re-execute
    this.countryDropdown.refreshOptions(); 
  } catch (error) {
    // Handle error, maybe show placeholder options
  }
}
```

**Important behavior with selections**: When refreshOptions is called, the dropdown attempts to preserve currently selected values. If selected values still exist in the refreshed options (by value equality), they remain selected. If selected values no longer exist in the updated options, they are deselected. This generally provides the expected user experience.

**Relationship with loading state**: When options are provided via an async function, refreshOptions should set loading=true while the async operation is in progress, then set loading=false when it completes. The dropdown may or may not automatically set loading depending on configuration, so manual loading state management may be needed.

**Performance considerations**: Refreshing options involves re-executing the options loading logic, which can be expensive for large lists or when calling APIs. Avoid excessive refresh calls that could impact performance.

This prop is a behavioral method that provides programmatic control over options reloading. It's particularly useful for dynamic option lists and data-driven dropdowns.

## Events

### valueChange

Emitted whenever the selected option(s) changes - on every selection or deselection in single-select mode, on every commit in multi-select mode (depending on confirmOnApply setting). This is the primary event for tracking dropdown selection changes in real-time.

**Emitted args:** `CustomEvent<{ name: string, value: any }>` where `name` is the dropdown's name attribute (if set) and `value` is the selected value (single value for single-select, array of values for multi-select)

**When to use:** Handle this event when you need to react to selection changes - for form validation, dependent field updates, data fetching, or when selection affects other parts of your application

**How to use:**
```typescript
// TypeScript handler for value-change event
onValueChange(event: Event): void {
  const customEvent = event as CustomEvent<{ name: string, value: any }>;
  const dropdownName = customEvent.detail.name;
  const selectedValue = customEvent.detail.value;
  
  if (Array.isArray(selectedValue)) {
    console.log(`Multi-select from ${dropdownName}:`, selectedValue);
    // Handle multi-select array (e.g., ["us", "ca", "mx"])
  } else {
    console.log(`Single-select from ${dropdownName}:`, selectedValue);
    // Handle single-select value (e.g., "us")
  }
  
  // Update your application state
  this.selectedCountries = selectedValue;
}
```

**Binding syntax:**
```html
<ion-dropdown
  label="Country"
  [options]="countryOptions"
  (valueChange)="onValueChange($event)">
</ion-dropdown>
```

### dropdownStateChanged

Emitted when the dropdown panel opens or closes - fires with `true` when the panel opens/opens, fires with `false` when the panel closes/closes. This event is useful for coordinating UI states or tracking dropdown open/closed state.

**Emitted args:** `CustomEvent<boolean>` where the boolean indicates open (true) or closed (false) state

**When to use:** Handle this event when you need to know the dropdown's open state - for coordinating with other UI elements, preventing multiple dropdowns from being open simultaneously, or tracking user interaction patterns

**How to use:**
```typescript
// TypeScript handler for dropdown state changes
onDropdownStateChanged(event: Event): void {
  const customEvent = event as CustomEvent<boolean>;
  const isOpen = customEvent.detail;
  
  if (isOpen) {
    console.log('Dropdown opened - can disable other dropdowns, show contextual help, etc.');
  } else {
    console.log('Dropdown closed - can restore UI state, perform validation, etc.');
  }
}
```

**Binding syntax:**
```html
<ion-dropdown
  label="Country"
  [options]="countryOptions"
  (dropdownStateChanged)="onDropdownStateChanged($event)">
</ion-dropdown>
```

### focusIn

Emitted when the dropdown field receives focus - when users click on it, tab to it, or when focus is set programmatically via the focus() method. This event is useful for focus management, keyboard navigation tracking, and accessibility enhancements.

**Emitted args:** `CustomEvent<void>` - no data is provided, this event signals focus state change

**When to use:** Handle this event when you need focus state tracking - for keyboard navigation, UI state management, accessibility enhancements, or focus-dependent behavior

**How to use:**
```typescript
// TypeScript handler for focus received
onFocusIn(): void {
  console.log('Dropdown field received focus - can highlight label, show help, etc.');
  // Optionally perform focus-dependent actions
  if (this.shouldShowHelpOnFocus) {
    this.showCountryDropdownHelp();
  }
}
```

**Binding syntax:**
```html
<ion-dropdown
  label="Country"
  [options]="countryOptions"
  (focusIn)="onFocusIn()">
</ion-dropdown>
```

### focusOut

Emitted when the dropdown field loses focus - when users click away, tab out, or when focus is removed programmatically via the blur() method. This event is commonly used for triggering validation when validationMode=onBlur and for cleaning up focus-dependent state.

**Emitted args:** `CustomEvent<void>` - no data is provided, this event signals focus state change

**When to use:** Handle this event when you need to know the dropdown lost focus - for trigger validation (especially when validationMode=onBlur), cleaning up UI state, or focus-dependent behavior

**How to use:**
```typescript
// TypeScript handler for focus lost
onFocusOut(): void {
  console.log('Dropdown field lost focus - validation may trigger, cleanup needed, etc.');
  // Focus-out logic may include:
  // - Validation (if not already handled by validationMode)
  // - Clearing temporary UI states
  // - Performing deferred calculations
}
```

**Binding syntax:**
```html
<ion-dropdown
  label="Country"
  [options]="countryOptions"
  (focusOut)="onFocusOut()">
</ion-dropdown>
```

### endEnhancerButtonClick

Emitted when the end enhancer button is clicked - this only fires if the end enhancer is configured with type="icon-button". This event provides a hook for handling custom button actions without needing to reference the enhancer element directly.

**Emitted args:** `CustomEvent<void>` - no data is provided, this event signals that the button was clicked

**When to use:** Handle this event when you need custom button behavior - for actions like opening dialogs, triggering related workflows, or performing contextual operations specific to the dropdown's end button

**How to use:**
```typescript
// TypeScript handler for end enhancer button click
onEndEnhancerButtonClick(): void {
  console.log('End enhancer button clicked - handle custom action');
  // Custom button behavior:
  // - Open related dialog (e.g., country selector modal)
  // - Trigger API call (e.g., refresh options from server)
  // - Navigate to related view
  // - Perform contextual workflow action
}
```

**Binding syntax:**
```html
<ion-dropdown
  label="Country"
  [options]="countryOptions"
  endEnhancer="{ type: 'icon-button', value: 'search' }"
  (endEnhancerButtonClick)="onEndEnhancerButtonClick()">
</ion-dropdown>
```

### validationStateChange

Emitted when the dropdown's validation state changes - when validationState prop transitions between "none", "valid", "warning", or "invalid". This event is useful for tracking validation status changes without using @Input binding validationState directly.

**Emitted args:** `CustomEvent<ValidationState>` where ValidationState is one of: "none", "valid", "warning", or "invalid"

**When to use:** Handle this event when you need to know validation status changes - for integrating with form validation systems, providing visual feedback beyond the built-in indicators, or tracking validation state programmatically

**How to use:**
```typescript
// TypeScript handler for validation state change
onValidationStateChange(event: Event): void {
  const customEvent = event as CustomEvent<string>;
  const newValidationState = customEvent.detail as "none" | "valid" | "warning" | "invalid";
  
  console.log(`Validation state changed to: ${newValidationState}`);
  
  // React to validation state changes:
  // - Update form-wide validation state
  // - Change container styling based on validation
  // - Show/hide additional validation UI
  // - Track validation metrics
}
```

**Binding syntax:**
```html
<ion-dropdown
  label="Country"
  [options]="countryOptions"
  required="true"
  validationMode="onBlur"
  (validationStateChange)="onValidationStateChange($event)">
</ion-dropdown>
```

### Complete event binding example

The following example demonstrates wiring all the key dropdown events together in a complete form context:

```typescript
@Component({
  template: `
    <ion-dropdown
      label="Country"
      placeholder="Select country"
      [options]="countryOptions"
      [multiSelect]="false"
      [required]="true"
      validationMode="onBlur"
      [validationState]="validationState"
      [name]="\'country\'"
      (valueChange)="onValueChange($event)"
      (dropdownStateChanged)="onDropdownStateChanged($event)"
      (focusIn)="onFocusIn()"
      (focusOut)="onFocusOut()"
      (endEnhancerButtonClick)="onEndEnhancerButtonClick()"
      (validationStateChange)="onValidationStateChange($event)">
    </ion-dropdown>
    
    <div class="form-status">
      <p>Selection: {{ selectedCountriesDisplay }}</p>
      <p>Valid: {{ validationState !== 'invalid' ? 'Yes' : 'No' }}</p>
      <p>Dropdown open: {{ isDropdownOpen ? 'Yes' : 'No' }}</p>
    </div>
  `
})
export class CountryDropdownComponent {
  countryOptions = [
    { value: "us", label: "United States" },
    { value: "ca", label: "Canada" },
    { value: "mx", label: "Mexico" }
  ];
  
  validationState: "none" | "valid" | "warning" | "invalid" = "none";
  isDropdownOpen = false;
  selectedCountries: string[] = [];
  
  // Event handlers using .detail access (critical for web components)
  onValueChange(event: Event): void {
    const customEvent = event as CustomEvent<{ name: string, value: any }>;
    console.log(`Value changed: name=${customEvent.detail.name}, value=${customEvent.detail.value}`);
    this.selectedCountries = Array.isArray(customEvent.detail.value) 
      ? customEvent.detail.value 
      : [customEvent.detail.value];
  }
  
  onDropdownStateChanged(event: Event): void {
    const customEvent = event as CustomEvent<boolean>;
    this.isDropdownOpen = customEvent.detail;
  }
  
  onFocusIn(): void {
    console.log('Country dropdown received focus');
  }
  
  onFocusOut(): void {
    console.log('Country dropdown lost focus');
  }
  
  onEndEnhancerButtonClick(): void {
    console.log('End enhancer button clicked - show country search modal');
    this.openCountrySearchModal();
  }
  
  onValidationStateChange(event: Event): void {
    const customEvent = event as CustomEvent<any>;
    this.validationState = customEvent.detail;
    console.log(`Validation state changed to: ${this.validationState}`);
  }
  
  openCountrySearchModal(): void {
    // Custom modal handling
  }
  
  get selectedCountriesDisplay(): string {
    return this.selectedCountries.length 
      ? this.selectedCountries.join(', ') 
      : 'No selection';
  }
}
```

### Multi-select confirmation event flow example

When using `confirmOnApply=true` in multi-select mode, the valueChange event has an important distinction that requires different handling:

**Important:** In multi-select with `confirmOnApply=true`, valueChange fires in two different ways:
- **Preview mode:** When users select/deselect options in the dropdown with Apply button still unclicked, valueChange fires with `committed: false` 
- **Confirmed mode:** When users click Apply, valueChange fires with `committed: true`

```typescript
@Component({
  template: `
    <ion-dropdown
      label="Regions"
      placeholder="Select regions"
      [options]="regionOptions"
      [multiSelect]="true"
      [confirmOnApply]="true"
      (valueChange)="onMultiSelectValueChange($event)">
    </ion-dropdown>
    
    <p>Selected regions: {{ selectedRegionsDisplay }}</p>
    <p>Preview count: {{ previewRegionsDisplay }}</p>
  `
})
export class RegionMultiSelectComponent {
  regionOptions = [
    { value: "na", label: "North America" },
    { value: "eu", label: "Europe" },
    { value: "asia", label: "Asia" }
  ];
  
  confirmedRegions: string[] = [];
  previewRegions: string[] = [];
  
  // Multi-select with confirmation workflow
  onMultiSelectValueChange(event: Event): void {
    const customEvent = event as CustomEvent<{ name: string, value: string[], committed: boolean }>;
    const regions = customEvent.detail.value;
    const isCommitted = customEvent.detail.committed;
    
    if (isCommitted) {
      // User clicked Apply - update confirmed selection
      console.log('Multi-select confirmed:', regions);
      this.confirmedRegions = [...regions];
      this.previewRegions = [];
    } else {
      // User is previewing selections (not yet committed)
      console.log('Multi-select preview:', regions);
      this.previewRegions = [...regions];
    }
  }
  
  get selectedRegionsDisplay(): string {
    return this.confirmedRegions.length ? this.confirmedRegions.join(', ') : 'None confirmed';
  }
  
  get previewRegionsDisplay(): string {
    return this.previewRegions.length ? `${this.previewRegions.length} pending` : '';
  }
}
```

**Key point:** The `committed` property (`event.detail.committed`) indicates whether the user has finalized their selection with Apply (`true`) or is still previewing changes (`false`). This distinction is critical for multi-select confirmation workflows.

## Examples

```html
<ion-dropdown
    label="Country"
    placeholder="Select a country"
    [options]="basicCountryOptions"
    labelPlacement="vertical">
</ion-dropdown>
```

Demonstrates the most basic dropdown configuration with label, placeholder, and options array.

```html
<ion-dropdown
    label="Size Example"
    placeholder="Select"
    labelPlacement="vertical"
    [options]="listOptions">
</ion-dropdown>
```

Shows dropdown with vertical label placement and standard options array, commonly used for basic single-select scenarios.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions">
</ion-dropdown>
```

Demonstrates dropdown with explicit vertical label placement (same as default behavior), showing fundamental usage pattern.

```html
<ion-dropdown
    label="Label"
    labelPlacement="horizontal"
    placeholder="Select"
    [options]="listOptions">
</ion-dropdown>
```

Shows dropdown with horizontal label placement, where label appears beside the field rather than stacked above it.

```html
<ion-dropdown
    label="Label"
    labelPlacement="horizontal"
    labelAlignment="start"
    placeholder="Select"
    [options]="listOptions">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="horizontal"
    labelAlignment="end"
    placeholder="Select"
    [options]="listOptions">
</ion-dropdown>
```

Demonstrates both start and end label alignment within horizontal label placement, showing how label positioning can be customized.

 ```html
 <ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    required="false"
    [options]="listOptions">
 </ion-dropdown>

 <ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    required="true"
    [options]="listOptions">
 </ion-dropdown>
 ```

 Shows required vs optional dropdowns with visual indicator (asterisk) appearing when required=true.

 ```html
 <ion-dropdown
    label="Country"
    placeholder="Select country"
    [options]="countryOptions"
    (valueChange)="onCountryChange($event)">
 </ion-dropdown>
 ```

 Demonstrates valueChange event binding where onCountryChange handles selections using event.detail to access the Dropdown's actual payload.

 ```html
 <ion-dropdown
    label="Regions"
    placeholder="Select regions"
    [options]="regionOptions"
    [multiSelect]="true"
    [confirmOnApply]="true"
    (valueChange)="onRegionSelect($event)">
 </ion-dropdown>
 ```

 Shows multi-select with confirmation workflow where onRegionSelect uses event.detail.value (array of selected values) and event.detail.committed (boolean indicating if Apply was clicked) to handle preview vs confirmed selections.

 Demonstrates all four necessity indicator types: asterisk marker, "Required" text, "Optional" text, or no indicator.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions"
    autoFocus="false">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions"
    autoFocus="true">
</ion-dropdown>
```

Shows dropdown with and without auto focus on load, demonstrating how autoFocus affects initial focus placement.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    [options]="listOptions">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions">
</ion-dropdown>
```

Demonstrates dropdown with and without placeholder text, showing how placeholder provides guidance when no option is selected.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    defaultValue="Value"
    [options]="listOptions">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    defaultValue=""
    [options]="listOptions">
</ion-dropdown>
```

Shows dropdown with and without default value, demonstrating how defaultValue provides initial selection that users can override.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions"
    startEnhancer="{ type: 'icon', value: 'placeholder' }">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions"
    startEnhancer="{ type: 'text', value: '+91' }">
</ion-dropdown>
```

Demonstrates start enhancer as an icon and as text, showing how visual content and prefixes can be added to the dropdown field.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions"
    endEnhancer="{ type: 'icon', value: 'placeholder' }">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions"
    endEnhancer="{ type: 'text', value: '$' }">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions"
    endEnhancer="{ type: 'icon-button', value: 'lock_filled' }">
</ion-dropdown>
```

Shows three end enhancer types: static icon, text prefix, and interactive icon-button, demonstrating the different ways enhancers can be positioned at the end of the field.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    defaultValue="Value"
    [options]="listOptions"
    clearButton="false">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    defaultValue="Value"
    [options]="listOptions"
    clearButton="true">
</ion-dropdown>
```

Demonstrates clear button functionality, showing how the clear button appears when a selection exists and allows users to clear their selection.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    defaultValue="Value"
    [options]="listOptions"
    helperMessage="Helper Message"
    validationState="none"
    helperMessageAsTooltip="false">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    defaultValue="Value"
    [options]="listOptions"
    helperMessage="Valid Helper Message"
    validationState="valid"
    helperMessageAsTooltip="false">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    defaultValue="Value"
    [options]="listOptions"
    helperMessage="Invalid Helper Message"
    validationState="invalid"
    helperMessageAsTooltip="false">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    defaultValue="Value"
    [options]="listOptions"
    helperMessage="Warning Helper Message"
    validationState="warning"
    helperMessageAsTooltip="false">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    defaultValue="Value"
    [options]="listOptions"
    helperMessage="Helper Message"
    validationState="none"
    helperMessageAsTooltip="true"
    tooltip-placement="right">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    defaultValue="Value"
    [options]="listOptions"
    helperMessage="Valid Helper Message"
    validationState="valid"
    helperMessageAsTooltip="true"
    tooltip-placement="right">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    defaultValue="Value"
    [options]="listOptions"
    helperMessage="Invalid Helper Message"
    validationState="invalid"
    helperMessageAsTooltip="true"
    tooltip-placement="right">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    defaultValue="Value"
    [options]="listOptions"
    helperMessage="Warning Helper Message"
    validationState="warning"
    helperMessageAsTooltip="true"
    tooltip-placement="right">
</ion-dropdown>
```

Shows all validation states (none, valid, invalid, warning) with helper messages displayed both inline and as tooltips, demonstrating validation feedback patterns.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions"
    required="true"
    validationMode="onBlur">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions"
    required="true"
    validationMode="onChange">
</ion-dropdown>
```

Demonstrates different validation modes (onBlur vs onChange), showing when validation executes and updates the validation state.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions"
    disabled="false">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions"
    disabled="true">
</ion-dropdown>
```

Shows disabled vs enabled dropdown states, demonstrating the visual appearance and interaction differences when disabled=true.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    defaultValue="Value"
    [options]="listOptions"
    readOnly="false"
    label="Label">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    defaultValue="Value"
    [options]="listOptions"
    readOnly="true"
    label="Label">
</ion-dropdown>
```

Demonstrates readOnly vs interactive dropdown states, showing how readOnly allows viewing options without making changes.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions"
    ariaLabel="This is aria label explicitly defined">
</ion-dropdown>
```

Shows dropdown with and without explicit ariaLabel, demonstrating how ariaLabel provides screen reader accessibility.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="longDescriptionOptions"
    dropdownWidth="auto">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="longDescriptionOptions"
    dropdownWidth="none">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="longDescriptionOptions"
    dropdownWidth="300px">
</ion-dropdown>
```

Demonstrates different dropdown width configurations: auto (matches field), none (content-based), and custom width (300px), showing how panel width can be customized independently of the field.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="multiDescriptionOptions"
    dropdownHeight="default">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="multiDescriptionOptions"
    dropdownHeight="full">
</ion-dropdown>
```

Shows dropdown height variants - default (standard) and full (expanded), demonstrating how panel height affects scrolling behavior and option visibility.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="optionsWithLabelDescription">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="groupedOptions">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="optionsWithDisabledItems">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="optionsWithIconEnhancers">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="optionsWithCategoryIcons">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="optionsWithTextEnhancers">
</ion-dropdown>
```

Demonstrates different options list configurations: basic options with descriptions, grouped options with icons, disabled options, icon enhancers, category icons, and text enhancers, showing the variety of option presentation patterns available.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions"
    multiSelect="false">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions"
    multiSelect="true">
</ion-dropdown>
```

Shows single-select vs multi-select dropdowns, demonstrating the fundamental interaction differences when multiSelect is enabled.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions"
    multiSelect="true"
    totalSelected="false">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions"
    multiSelect="true"
    totalSelected="true">
</ion-dropdown>
```

Demonstrates totalSelected display in multi-select mode, showing how totalSelected="true" displays count ("3 selected") instead of listing all labels.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="optionsWithDisabledItems"
    multiSelect="true"
    showSelectAll="false">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="optionsWithDisabledItems"
    multiSelect="true"
    showSelectAll="true">
</ion-dropdown>
```

Shows Select All checkbox functionality in multi-select mode, demonstrating how showSelectAll adds a bulk selection control at the top of the option list.

```html
<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions"
    multiSelect="false">
</ion-dropdown>

<ion-dropdown
    label="Label"
    labelPlacement="vertical"
    placeholder="Select"
    [options]="listOptions"
    multiSelect="true">
</ion-dropdown>
```

Demonstrates the fundamental difference between single-select and multi-select interaction models, showing how multiSelect enables multiple simultaneous selections and display differences (checkboxes, etc.).