---
realComponent: ion-radio
description: A radio button component that allows users to select a single option from a group, with support for design system styling, emphasis variations, and responsive sizing
themes: [light, dark]
props:
  - name: label
    type: string
    category: content
    required: false
    default: none found
    values: []
    designTokens: {}
  - name: name
    type: string
    category: content
    required: false
    default: none found
    values: []
    designTokens: {}
  - name: id
    type: string
    category: accessibility
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
  - name: required
    type: boolean
    category: content
    required: false
    default: none found
    values: []
    designTokens: {}
  - name: emphasized
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens:
      true:
        light:
          resolvesTo: "#007de0"
          tokenChain: "--ion-comp-radio-container-color-bg-enabled-bold -> --ion-lit-color-leonardo-base-primary (#007de0)"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#008af7"
          tokenChain: "--ion-comp-radio-container-color-bg-enabled-bold -> --ion-lit-color-palette-dark-blue-700 (#008af7)"
          appliesToCssProperty: "background-color"
      false:
        light:
          resolvesTo: "#ffffff"
          tokenChain: "--ion-comp-radio-container-color-bg-enabled-subtle -> #ffffff"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#1f1e1f"
          tokenChain: "--ion-comp-radio-container-color-bg-enabled-subtle -> --ion-lit-color-palette-dark-slate-900 (#1f1e1f)"
          appliesToCssProperty: "background-color"
  - name: size
    type: string
    category: visual
    required: false
    default: "md"
    values: [sm, md, lg]
    designTokens:
      sm:
        resolvesTo: "16px"
        tokenChain: "--ion-comp-radio-container-sizing-sm -> 16px"
        appliesToCssProperty: "width, height"
      md:
        resolvesTo: "20px"
        tokenChain: "--ion-comp-radio-container-sizing-md -> 20px"
        appliesToCssProperty: "width, height"
      lg:
        resolvesTo: "24px"
        tokenChain: "--ion-comp-radio-container-sizing-lg -> 24px"
        appliesToCssProperty: "width, height"
  - name: autoFocus
    type: boolean
    category: behavioral
    required: false
    default: false
    values: []
    designTokens: {}
  - name: selected
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens:
      true:
        light:
          resolvesTo: "#007de0"
          tokenChain: "--ion-comp-radio-container-color-bg-selected-enabled-subtle -> background-color with primary color"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#008af7"
          tokenChain: "--ion-comp-radio-container-color-bg-selected-enabled-subtle -> background-color with primary color"
          appliesToCssProperty: "background-color"
      false:
        light:
          resolvesTo: "#ffffff"
          tokenChain: "--ion-comp-radio-container-color-bg-enabled-subtle -> #ffffff"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#1f1e1f"
          tokenChain: "--ion-comp-radio-container-color-bg-enabled-subtle -> --ion-lit-color-palette-dark-slate-900 (#1f1e1f)"
          appliesToCssProperty: "background-color"
  - name: disabled
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens:
      true:
        light:
          resolvesTo: "#e9eaeb"
          tokenChain: "--ion-comp-radio-container-color-bg-disabled-subtle -> --ion-lit-color-palette-light-navy-200 (#e9eaeb)"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#1f1e1f"
          tokenChain: "--ion-comp-radio-container-color-bg-disabled-subtle -> --ion-lit-color-palette-dark-slate-900 (#1f1e1f)"
          appliesToCssProperty: "background-color"
  - name: disabledInternal
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
    designTokens:
      true:
        light:
          resolvesTo: "#ffffff"
          tokenChain: "--ion-comp-radio-container-color-bg-read-only-subtle -> #ffffff"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#1f1e1f"
          tokenChain: "--ion-comp-radio-container-color-bg-read-only-subtle -> --ion-lit-color-palette-dark-slate-900 (#1f1e1f)"
          appliesToCssProperty: "background-color"
  - name: readOnlyInternal
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
    default: none found
    values: []
    designTokens: {}
  - name: tabIndex
    type: string
    category: accessibility
    required: false
    default: none found
    values: []
    designTokens: {}
  - name: setFocus
    type: () => void
    category: behavioral
    required: false
    default: none found
    values: []
    designTokens: {}
events:
  - name: selectionChange
    payloadType: "CustomEvent<boolean>"
    firesWhen: "Emitted when the radio button's selection state changes - triggered by user click (if not disabled/readOnly), NOT when selected prop changes programmatically"
    detailAccess: "event.detail (boolean) - true when radio becomes selected, false when it becomes unselected"
    bindingSyntax: "(selectionChange)=\"onSelectionChange($event)\""
  - name: focusIn
    payloadType: "CustomEvent<void>"
    firesWhen: "Emitted when the radio button receives focus - when users click or tab into the radio button, or when focus is set programmatically"
    detailAccess: "void, event.detail is undefined - this event signals focus state change without carrying data"
    bindingSyntax: "(focusIn)=\"onFocusIn()\""
  - name: focusOut
    payloadType: "CustomEvent<void>"
    firesWhen: "Emitted when the radio button loses focus - when users click away, tab out, or when focus is removed programmatically"
    detailAccess: "void, event.detail is undefined - this event signals focus state change without carrying data"
    bindingSyntax: "(focusOut)=\"onFocusOut()\""
jointTokens:
  - combination: "emphasized=true, selected=true"
    resolvesTo: "#007de0"
    tokenChain: "--ion-comp-radio-container-color-bg-selected-enabled-bold -> --ion-lit-color-leonardo-base-primary (#007de0)"
    appliesToCssProperty: "background-color"
  - combination: "emphasized=true, selected=false"
    resolvesTo: "#007de0"
    tokenChain: "--ion-comp-radio-container-color-bg-enabled-bold -> --ion-lit-color-leonardo-base-primary (#007de0)"
    appliesToCssProperty: "background-color"
  - combination: "emphasized=false, selected=true"
    resolvesTo: "#007de0"
    tokenChain: "--ion-comp-radio-container-color-bg-selected-enabled-subtle -> background with primary style"
    appliesToCssProperty: "background-color"
propInteractions:
  - "readOnly prevents user interaction with the radio button - clicking has no effect and space key does not toggle selection. Used when you want to display a radio state without allowing changes."
  - "disabled completely disables the radio button - both visually (grayed appearance) and functionally (no user interaction possible). The component uses finalDisabledState = disabled || disabledInternal for combined control."
  - "readOnly also has readOnlyInternal variant for group-based control, combined as finalReadOnlyState = readOnly || readOnlyInternal."
  - "emphasized provides additional visual prominence by using stronger colors (bold styling tokens). When emphasized=true, radio uses primary brand colors for backgrounds versus neutral colors for emphasized=false."
  - "size affects multiple visual properties simultaneously: radio container dimensions (width/height), indicator size, padding, and gap between radio and label. Supports MQ design strings for responsive sizing."
  - "selected is independent of emphasized - emphasized changes color intensity while selected changes whether the radio appears selected with filled indicator, and both can combine to create different visual states."
  - "When radio button is part of a radio group, only one radio in the group can be selected at any time (based on shared 'name' attribute), but individual radio components don't enforce this group behavior directly."
  - "setFocus() method provides programmatic focus control for accessibility workflows and focus management."
  - "id is auto-generated as 'Radio-' + Date.now().toString() when not explicitly provided, ensuring proper label-radio association."
  - "ariaLabel defaults to label value when not explicitly set, providing automatic accessibility behavior."
needsReview:
  - "Dark theme tokens for emphasized and selected states - values traced for light theme but dark theme token resolution could not be fully verified. Dark theme appears to use different palette colors (e.g., #008af7 for primary) but complete token chain needs verification."
  - "Border color tokens for radio container and indicator - referenced in radio-ds.css (e.g., --ion-comp-radio-container-color-border-enabled-subtle) but specific hex values for light and dark themes could not be traced from available token definitions."
  - "Hover and active state design tokens for radio container and indicator - tokens defined in radio-ds.css but specific hex values for light and dark themes could not be traced."
  - "Indicator (inner circle) design tokens - radio-ds.css references --ion-comp-radio-indicator-color-bg-enabled-subtle and color-border-enabled-subtle but specific hex values could not be fully traced from token definitions."
  - "Gap spacing tokens between radio and label (--ion-comp-radio-container-outer-spacing-gap-md) depend on size prop but specific scaling mapping for sm/md/lg values could not be determined."
  - "Padding tokens for radio container (--ion-comp-radio-container-spacing-padding-inline-md, padding-block-md) vary by size but specific values could not be traced for all size variants."
  - "Border radius tokens (--ion-comp-radio-container-border-radius, --ion-comp-radio-indicator-border-radius) referenced but final resolved values could not be traced."
  - "Validation states (valid, invalid, warning) are defined in radio-ds.css (.ion-ds-invalid, .ion-ds-valid) but validation-specific token values could not be traced from available source material; these may be controlled by parent radio group components."
  - "MQ design string parsing behavior for size prop - the component supports responsive strings like 'xs=sm;sm=sm;md=md;lg=lg;xl=lg;xxl=md' but runtime behavior could not be verified without screen size context."
  - "disabledInternal and readOnlyInternal props - these appear to be used internally by radio group components for group-level control but documentation is minimal; interaction with regular disabled/readOnly needs runtime verification."
  - "Selection event behavior when using externally provided HTML input elements - the component checks isInputElementExternallyProvided flag and may change event emission behavior, but this couldn't be verified from available samples."
---

## Usage Notes

Boolean props on this component must always be passed with an explicit string value — e.g. `disabled="true"` or `[disabled]="isDisabled"` — never as bare attribute presence (e.g. `disabled` alone, with no value). Bare attribute presence is a native HTML convention this component does NOT support; it will not be interpreted as true.

## label

The text content displayed as the identifier for the radio button, typically positioned to the right of the radio input. Labels provide context and help users understand what the radio button represents. This is a content prop that does not affect the component's behavior or visual appearance beyond the text content.

When a label is provided, it appears as a clickable text label next to the radio circle. Clicking on the label text triggers the same selection action as clicking on the radio circle itself, providing a larger target area for user interaction.

**Important accessibility relationship**: When ariaLabel is not provided, the radio button automatically uses the label text as its aria-label value for screen reader accessibility. For radio buttons without visible labels, always provide an ariaLabel to ensure accessibility compliance.

**Label positioning and gap**: The label appears to the right of the radio container with spacing determined by design system gap tokens. The gap size depends on the selected size prop (sm/md/lg) but specific spacing values are controlled by the design system.

When no label is provided, the radio button appears as a standalone circle without explanatory text. This may be appropriate when the radio button's purpose is immediately obvious from context (e.g., in radio groups with group-level labels).

This prop is self-contained for content, though its visual presentation (font size, color, spacing) is controlled by the component's design system tokens and size prop.

## name

Provides a name for the radio button, which is primarily used when the radio button is part of an HTML form. The name attribute groups related radio buttons together, ensuring only one can be selected at a time. This is a content prop that affects form data structure and radio button grouping behavior.

The name prop accepts string values that identify the radio button group. When multiple radio buttons share the same name, they belong to the same mutually exclusive group - selecting one automatically deselects others.

**Form submission behavior**: When a radio button with a name is selected, the form submission includes that radio button's name and value pair (e.g., name="preference" and value="dark" becomes preference=dark). Only the selected radio's data is included.

**Use cases**:
- **Form submissions**: Use name to identify radio data when submitting forms
- **Radio button groups**: Multiple related radio options share the same name (e.g., name="theme" with values="light", "dark", "auto")
- **Database integration**: Name often maps to database field names for form data storage

**Accessibility**: The name attribute does not affect screen reader accessibility. Use ariaLabel or label for screen reader announcements. The name is only used for form data identification and radio group logic.

This prop is content-oriented and self-contained. It has no visual effects but is crucial for form data handling, radio group grouping, and mutual exclusion behavior.

## id

Provides a unique identifier for the radio button, which is used for HTML labeling associations and element targeting. The id attribute allows other elements (like labels) to reference this radio button specifically, and is commonly used in automation testing and JavaScript element selection. This is an accessibility/technical prop that does not affect visual appearance.

The id prop accepts string values that must be unique within the document scope. When an id is provided, it's applied to the hidden native radio input element, which allows proper association with label elements via the label's "for" attribute.

**Automatic ID generation**: When no id is provided, the component automatically generates a unique ID using the pattern "Radio-" followed by a timestamp (Date.now()). This ensures proper label-radio association even when developers don't manually specify IDs.

**Label association**: The component's label element automatically references the radio button's id via its "for" attribute, creating a proper semantic connection. This ensures that clicking the label text triggers the radio selection and that screen readers announce the relationship correctly.

**Use cases**:
- **Form element linking**: Provide explicit IDs when you need to link external labels or form elements to the radio button
- **Automated testing**: Use predictable IDs for test automation and element selection in testing frameworks
- **JavaScript targeting**: Select specific radio buttons for manipulation via document.getElementById()
- **Accessibility compliance**: Ensure proper label associations when dynamic content is generated

## value

Provides the value associated with the radio button, which is submitted with form data when the radio button is selected and part of a form. The value prop distinguishes individual radio buttons within a group that share the same name attribute. This is a content prop that affects form submission data but not visual appearance.

The value prop accepts string values that represent the data being selected. When checked, the radio's value is submitted along with its name (e.g., name="color" and value="blue" becomes color=blue in form data).

**Form submission behavior**:
- **Selected radio button**: name=value pair is included in form submission
- **Unselected radio buttons**: name=value pairs are completely excluded from form submission
- **Radio with no value**: When no value is specified, checked radios may default to the string "on" as their value

**Use cases**:
- **Options within groups**: Multiple radios with same name but different values (e.g., themes: "light", "dark", "system")
- **Data mapping**: Map radio selections to database values or API parameters
- **Form handling**: Collect user preferences for form submission

**Integration with radio groups**: In radio group components, the value prop is particularly important because the group component uses the selected radio's value as the group's value property.

This prop is content-oriented and primarily affects form submission data structure. It has no visual effects but is fundamental to form data handling and radio button identification.

## required

When true, indicates that an option must be selected from the radio button group before the form can be considered complete. This is a semantic/content prop that affects HTML attributes and can trigger validation behavior, particularly when used within radio button groups or form validation systems.

The required prop adds the required="required" attribute to the native radio input element, which is important for screen readers and assistive technologies. It creates a semantic requirement but does not automatically enforce validation or add visible required indicators.

**Validation behavior**:
- **Standalone radio button**: The required prop marks the radio button as semantically required but does not automatically validate or block form submission on its own
- **Radio button group context**: When used within radio button groups, the group validation logic checks whether a required option is selected and sets validationState accordingly
- **Form validation**: Form-level validation systems can check the radio button group's state and display required messages using this attribute

**Accessibility impact**: The required="required" attribute helps screen reader users identify which radio button groups require selection before form submission. This is particularly important for form accessibility compliance.

**Visual indicators**: The required prop itself does not add visual indicators (stars, asterisks, or "Required" text). Visual requirement indicators would typically be managed through a radio button group's necessityIndicator prop or external UI elements.

**Use cases**:
- **Mandatory selections**: Mark certain radio button groups as required choices
- **Form accessibility**: Ensure screen readers announce requirement status clearly
- **Validation integration**: Provide semantic hooks for form validation libraries

**Important relationship with radio button groups**: When used within radio button groups, the group component may use this attribute as part of its validation logic. The group's validationState prop and validationMode prop control how requirements are enforced and displayed.

This prop is semantic/accessible in nature and primarily affects HTML markup and validation behavior. It has no visual effects on its own but enables proper form validation and accessibility.

## emphasized

Controls the visual prominence of the radio button by using stronger colors and more prominent styling. When true, the radio button displays with bold styling that makes it more visually prominent in the interface. This is a visual prop that affects the radio button's appearance without changing its behavior.

**Emphasized state visual effects**:

- **Emphasized=false (subtle/default)**: Unselected radio buttons have neutral colors (light background/dark foreground), selected radio buttons have more subtle background colors. This is the restrained, default appearance that blends with the interface without drawing excessive attention.

- **Emphasized=true (bold)**: Unselected radio buttons have prominent brand colors (typically blue) for backgrounds and borders, selected radio buttons have strong background colors and visual emphasis. This creates a more visually prominent, attention-grabbing appearance.

**Important visual cues**:
- **Background color**: When emphasized=true, radio buttons use primary branding colors for backgrounds instead of neutral colors
- **Border color**: Unselected emphasized radio buttons have colored borders using brand colors
- **Selection indicator**: Selected emphasized radio buttons use bold primary colors for both container and indicator

**Use cases for emphasized state**:
- **Primary options**: Use emphasized for the primary radio button in a set to guide user selection
- **Feature highlights**: Draw attention to重要 radio buttons that represent key choices
- **Branded interfaces**: Use emphasized styling to align with brand colors and create strong visual identity
- **Dashboard widgets**: Make radio buttons in prominent positions more visually distinct

**Interaction with selected**: The emphasized and selected props work together to determine the final visual appearance. When both emphasized=true and selected=true, the radio button uses the boldest styling with filled primary colors. When emphasized=true and selected=false, the radio button still shows bold styling (colored borders/background) but without the filled selected state.

**Theme considerations**: The actual hex values for emphasized states differ between light and dark themes, with each theme using appropriate color palette tokens to ensure contrast and visual harmony.

This prop is purely visual and does not affect the radio button's behavior or interactions. It provides a design system-compliant way to create hierarchy and emphasis between different radio buttons in the interface.

## size

Controls the height, width, padding, indicator size, and spacing scale of the radio button. Size values (sm, md, lg) map to design system spacing and typography tokens that scale the entire radio button proportionally. This is a visual prop that directly impacts the user's perception of the component's scale and prominence in the interface.

The size prop affects multiple visual properties simultaneously through design system tokens:
- **Container dimensions**: Overall width and height of the radio circle
- **Indicator size**: Size of the inner selection circle
- **Internal padding**: Space between radio border and inner indicator
- **Label spacing**: Gap between radio and label text

**Size values and their visual effects**:

- **sm**: Small radio button with 16px container. The inner indicator is smaller, internal padding is tighter, and overall appearance is more compact. This is useful for dense interfaces with many radio buttons or limited space.

- **md (default)**: Medium radio button with 20px container. Standard indicator size, regular padding, balanced proportions. This is the most commonly used size and appropriate for most form interfaces.

- **lg**: Large radio button with 24px container. Larger indicator size, generous padding, more prominent appearance. Useful for interfaces with larger touch targets or when radio buttons need special emphasis.

**Important interactive benefits**:
- **Touch targets**: Larger sizes (lg) provide bigger touch targets for mobile users
- **Accessibility**: Smaller sizes may be harder to click for users with motor disabilities
- **Visual hierarchy**: Size creates effective hierarchy when different radio buttons have different sizes

**MQ string support**: The size prop can accept Media Query (MQ) responsive strings that allow different sizes at different breakpoints. For example, you could specify "xs=lg;sm=md;md=md;lg=md" to get larger radio buttons on extra-small screens for better touch targets, while maintaining medium size on larger screens.

**Label and spacing effects**: The size prop also affects the gap between the radio and label, as well as the overall spacing around the component. Larger sizes create more breathing room, while smaller sizes create tighter layouts.

**Use cases**:
- **Compact forms**: Use sm for dense interfaces with limited vertical spacing
- **Standard forms**: Use md as the default for most form inputs
- **Mobile-first interfaces**: Use lg for better touch targets on mobile devices
- **Action emphasis**: Use lg size for primary radio buttons to make them more prominent

This prop is visual and self-contained. It affects multiple design aspects simultaneously through design system tokens but does not depend on other props for its effect.

## autoFocus

When true, the radio button automatically receives focus when the component is rendered or initialized. This is a behavioral prop that affects keyboard navigation and user interaction flow but has no visual appearance.

The autoFocus prop determines whether the radio button should capture keyboard focus immediately after component initialization. When set to true, the native radio input element is focused via a setTimeout call.

**Behavior differences**:
- **autoFocus=false (default)**: The radio button does not automatically receive focus. Users navigate to it normally via tab key or by clicking. This is the standard behavior for most radio buttons.

- **autoFocus=true**: The radio button receives focus automatically after component initialization. Users will see the browser's default focus indicator around the radio button, and they can immediately select it using the space key without navigating to it first.

**Use cases**:
- **Form initialization**: Set focus on the first radio button in a group to guide users into form interaction
- **Multi-step wizards**: Automatically focus appropriate radio buttons as users progress through steps
- **Keyboard-focused interfaces**: Improve accessibility and keyboard navigation by providing automatic focus points
- **Error recovery**: After validation errors, autofocus the problematic radio button to draw user attention

**Accessibility considerations**:
- **Multiple autofocus elements**: When multiple elements have autofocus=true, browsers typically focus only the first one encountered in DOM order
- **Screen reader announcements**: Automatic focus may trigger screen reader announcements, which can be confusing if unexpected
- **Mobile considerations**: Virtual keyboards on mobile devices don't respond to radio button focus, so autofocus has different effects on mobile

**Interaction with other focus-related features**:
- **setFocus() method**: You can also call the component's setFocus() method programmatically at any time, which performs the same action regardless of the autoFocus prop value
- **focusIn event**: The focusIn event is emitted both when autofocus triggers focus and when focus is set programmatically or via user interaction
- **Tab navigation**: Users can still navigate via tab key normally; autofocus just provides initial focus

This prop is behavioral and does not have visual appearance. It affects user interaction flow and keyboard accessibility but not the radio button's visual presentation.

## selected

Controls whether the radio button is in the selected (checked) state. When true, the radio button displays a filled indicator and uses selected state styling. When false, the radio button appears as an empty circle with unselected styling. This is a visual/state prop that is central to the radio button's primary function.

**State behavior and visual effects**:

- **selected=false**: The radio button appears as an empty circle. The container background and border reflect the unselected state using neutral or emphasized color palettes depending on the emphasized prop.

- **selected=true**: The radio button displays a filled indicator (inner circle) and uses selected state styling. The background color becomes filled and borders may change based on the emphasized prop. The indicator color contrasts with the container background.

**Important radio button behavior**: As a radio button (single-select control), this radio button's selected state is meant to be managed mutually exclusively with other radio buttons that share the same name attribute. When implementing a radio button group, selecting one typically should deselect others with the same name, but the radio button component itself doesn't enforce this grouping behavior - that logic should be handled by a parent radio group component.

**State management patterns**:
- **Controlled component**: Bind selected to your state and update that state when selectionChange event fires to maintain full control
- **Uncontrolled component**: Let the radio button manage its own selected state and only read it when needed
- **Form integration**: Use selected in conjunction with value for form submission handling

**State persistence**: The radio button maintains its selected state through component re-renders unless changed by user interaction or by updating the selected prop from application code.

**Selection states vs validation**: The selected prop tracks the radio button's selection state, while validation-related props (required, validationState when in radio button groups) track whether the current state meets business rules.

**Use cases**:
- **Single choice selection**: Allow users to select one option from a mutually exclusive set
- **Preference selection**: User settings like themes, languages, or display modes
- **Choice classification**:_categorical choices like shipping methods, subscription tiers, or quality options

This prop is central to the radio button's function and affects both visual presentation and the selectionChange event emission.

## disabled

When true, the radio button becomes completely non-interactive - users cannot click to change the selection, and the radio button appears visually deactivated with reduced opacity and grayed styling. This is a visual/behavioral prop that signals and enforces an unavailable state.

**Disabled state effects**:

- **Visual**: The radio button appears "grayed out" with reduced opacity, typically around 40-60% of normal opacity. This signals visually that the element is not available for interaction.

- **Functional**: All user interaction is blocked:
  - Clicking on the radio button has no effect (selection does not change)
  - Keyboard focus navigation skips the disabled radio button
  - Space key does not trigger selection when the radio button has focus
  - The component is excluded from form submission data

- **Event emission**: The selectionChange event is NOT emitted for disabled radio buttons, even if the selected prop changes programmatically.

**Internal vs external disabled state**:
- **disabled (regular)**: The primary disabled prop that can be set directly on the radio button component
- **disabledInternal**: Used internally by radio button group components to disable individual radio buttons as part of group-level disabled state
- **Combined effect**: Final disabled state is determined by `disabled || disabledInternal`, providing both direct and group-based control

**Accessibility considerations**:
- Keyboard navigation typically skips disabled elements (tab key moves past them)
- Screen readers may announce "disabled" or similar status to indicate unavailability
- The disabled attribute is applied to the native radio input element for proper accessibility behavior

**Use cases for disabled state**:
- **Conditional availability**: Disable radio buttons when related criteria aren't met
- **Processing states**: Temporarily disable radio buttons while form submission or data processing occurs
- **Permission control**: Disable options the user doesn't have permission to change
- **Progressive disclosure**: Disable future options until previous steps are completed

**Important distinction from readOnly**:
- **disabled**: Complete non-interactive state with visual cues of unavailability
- **readOnly**: Interactive (can be viewed/examined) but selection cannot be changed

This prop provides both visual and functional disabling. It completely prevents user interaction while providing clear visual feedback about the unavailable state.

## disabledInternal

Internal disabled state used primarily by radio button group components to disable individual radio buttons when the entire group is disabled. This is a visual/behavioral prop that works in combination with the regular disabled prop.

**Combined disabled behavior**:
- The radio button uses `finalDisabledState = disabled || disabledInternal` to determine its actual disabled state
- This allows group-level control while still permitting individual radio button control
- When either prop is true, the radio button becomes completely non-interactive

**Use cases**:
- **Radio button group disabling**: When a parent radio button group is disabled, all child radio buttons get disabledInternal=true automatically
- **Individual control**: Allows overriding group-level disabling on specific radio buttons if needed
- **Conditional logic**: Provides separation between user-controlled disabled state and automatically managed disabled state

**Important pattern**: This prop is typically not used directly in template code - it's mainly for internal component communication between radio button groups and their child radio buttons.

This prop is primarily for internal component architecture and should not be used directly in most application code. Use the regular disabled prop for explicit disabling.

## readOnly

When true, the radio button maintains visual interactivity but prevents changing the selected state through user interaction. Users can click and interact with the radio button, but the selection remains unchanged. This creates a read-only presentation that allows exploration without committing changes.

**ReadOnly state effects**:

- **Visual**: The radio button appears interactive and in normal visual style (not grayed like disabled). It maintains standard colors and transparency, suggesting it can be interacted with.

- **Functional**: User interaction is limited:
  - Clicking on the radio button does not change selection
  - Space key does not trigger selection
  - The radio button still responds to hover states and shows normal visual feedback
  - Keyboard focus still works normally (can be tabbed to and focused)
  - The selectionChange event is NOT emitted when users click

**State preservation**: The radio button maintains its current selected state regardless of user interaction attempts. The selected prop can still be changed programmatically.

**Internal vs external readOnly state**:
- **readOnly (regular)**: The primary readOnly prop that can be set directly on the radio button component
- **readOnlyInternal**: Used internally by radio button group components to make individual radio buttons read-only as part of group-level read-only state
- **Combined effect**: Final read-only state is determined by `readOnly || readOnlyInternal`, providing both direct and group-based control

**Important distinction from disabled**:
- **disabled**: Complete non-interactive state with visual cues of unavailability (grayed appearance)
- **readOnly**: Interactive appearance but selection cannot be changed by users

**Use cases for readOnly state**:
- **Displaying selected states**: Show users which option is selected without allowing them to change (e.g., in review screens or displays)
- **Exploration modes**: Allow users to see what would happen if options were selected, without committing changes
- **Permission-based access**: Show options that might be available in other contexts but not changeable in current context
- **Conditional editing**: Make some radio buttons read-only while others in the same group are editable

This prop is primarily functional - it allows visual interaction but prevents state changes. It's useful for displaying static selection states while maintaining interactivity cues.

## readOnlyInternal

Internal read-only state used primarily by radio button group components to make individual radio buttons read-only when the entire group is read-only. This is a visual/behavioral prop that works in combination with the regular readOnly prop.

**Combined read-only behavior**:
- The radio button uses `finalReadOnlyState = readOnly || readOnlyInternal` to determine its actual read-only state
- This allows group-level control while still permitting individual radio button control
- When either prop is true, the radio button becomes read-only (prevents user selection changes)

**Use cases**:
- **Radio button group read-only mode**: When a parent radio button group is read-only, all child radio buttons get readOnlyInternal=true automatically
- **Individual control**: Allows overriding group-level read-only state on specific radio buttons if needed
- **Conditional logic**: Provides separation between user-controlled read-only state and automatically managed read-only state

**Important pattern**: This prop is typically not used directly in template code - it's mainly for internal component communication between radio button groups and their child radio buttons.

This prop is primarily for internal component architecture and should not be used directly in most application code. Use the regular readOnly prop for explicit read-only behavior.

## ariaLabel

Provides an accessible label for screen readers and assistive technologies. The ariaLabel prop is used for accessibility when a radio button lacks a visible text label, or when you need to provide a more descriptive label than what's shown on screen. This is an accessibility prop that affects screen reader announcements but not visual appearance.

**Accessibility behavior**:
- **When ariaLabel is provided**: Screen readers use the ariaLabel text to announce the radio button's purpose instead of or in addition to the visible label
- **When ariaLabel is not provided**: The radio button automatically uses the label text as the accessibility label for screen readers
- **For radio buttons without labels**: Always provide ariaLabel to ensure accessibility compliance

**Automatic default behavior**: When ariaLabel is not explicitly set, the component defaults to using the label property value as the aria-label. This provides automatic accessibility without requiring developers to think about it separately.

**Use cases**:
- **No visual label**: Radio buttons with only an icon or no text need ariaLabel for screen reader support
- **Supplemental descriptions**: Provide additional context or instructions that appear in screen reader announcements but not on screen
- **Technical labels**: Use more descriptive text for screen readers than what's visually displayed
- **Icon-only radio buttons**: Essential for accessibility when radio buttons use only icons

**Accessibility hierarchy**:
- **Primary source**: ariaLabel when provided
- **Fallback**: label text when ariaLabel is not provided
- **Failure**: Neither ariaLabel nor label results in inaccessible radio button for screen readers

**Screen reader announcements**:
- Typically includes the radio button state (selected/unselected)
- Announces the ariaLabel or label text as the radio button's identifier
- May announce "radio button, selected" or similar depending on screen reader

**Mobile accessibility**:
- On touch devices, the radio button uses ariaLabel for screen reader navigation
- The native input element's aria-label is managed by the radio button for accessibility

**Important distinction from label**:
- **label**: Visible text label displayed to sighted users, positioned next to radio button
- **ariaLabel**: Accessible label for screen readers, not displayed visually

**Examples**:
- **Icon-only radio button**: ariaLabel="Dark theme" when radio button has only a moon icon
- **Technical label**: label="v2.4" (visible version number), ariaLabel="Version 2.4 - Latest stable release" (more descriptive)
- **Contextual help**: label="Email updates", ariaLabel="Subscribe to email updates about your account status"

**Internationalization**:
- ariaLabel should be translated/localized like any other user-facing text
- The visible label may be abbreviated for UI constraints, while ariaLabel can use full descriptions
- Screen reader language detection uses ariaLabel's text content

This prop is purely accessibility-focused. It has no visual appearance but is essential for making radio buttons accessible to screen reader users and assistive technology users.

## tabIndex

Controls the radio button's tabindex attribute for keyboard navigation. This is an accessibility prop that determines whether and how the radio button can be focused using keyboard navigation, without affecting visual appearance.

**Tabindex behavior**:
- **When provided**: Sets the tabindex attribute directly on the native radio input element
- **When not provided**: The radio button uses default tabindex behavior (0 for focusable elements)

**Use cases**:
- **Custom tab order**: Control the order in which radio buttons receive focus during tab navigation
- **Non-standard navigation**: Remove from tab navigation (tabindex="-1") while keeping it focusable via other methods
- **Accessibility enhancement**: Ensure proper keyboard navigation patterns for complex forms

**Important accessibility considerations**:
- Radio buttons should generally remain in the normal tab navigation flow (tabindex>=0)
- Removing from tab navigation ( tabindex="-1" ) makes keyboard-only users unable to access the radio button via standard tabbing
- Set focus programmatically using the setFocus() method when using non-standard tabindex values

This prop is technical and accessibility-focused. It doesn't affect visual appearance but directly impacts keyboard navigation patterns and accessibility.

## setFocus

A method that can be called programmatically to set keyboard focus to the radio button. This is a behavioral method rather than a prop - it's part of the component's API but not a configurable property. The setFocus() method provides programmatic control over which element receives keyboard focus.

**Method behavior**:
- **Call signature**: `radioButton.setFocus()` - takes no parameters and returns void
- **Effect**: Sets keyboard focus to the radio button's native input element by querying the shadowRoot
- **Visual**: The browser's default focus indicator appears around the radio button container
- **Keyboard**: Users can immediately select the radio button with the space key after focus is set

**Implementation details**:
- The method queries the element's shadowRoot to find the hidden native input element
- Focus is applied to the native input element rather than the container element for proper accessibility behavior
- The focus effect is the same as users tabbing to the radio button naturally via keyboard navigation

**Use cases**:
- **Form management**: After validation errors, focus the first invalid radio button to draw user attention
- **Multi-step wizards**: As users progress through steps, programmatically focus the appropriate radio button in the next step
- **Accessibility enhancements**: Provide programmatic focus control for keyboard navigation flows
- **State synchronization**: When application logic determines a specific radio button needs user attention or interaction
- **Error recovery**: After errors occur programmatically, focus the problematic radio button

**Timing and lifecycle**:
- Can be called at any time after component initialization
- Most commonly called in ngAfterViewInit or in response to user actions
- Should be called after the component is fully rendered and attachments are complete
- Works regardless of the autoFocus prop value (setFocus() overrides and works independently)

**Event emission**:
- When setFocus() is called and successfully sets focus:
  - The focusIn event is emitted (same event that fires when users tab to the radio button)
  - Any attached focusIn event handlers are triggered
  - Screen reader focus announcements occur

**Error handling**:
- The method is designed to handle cases where the component or input element may not be available
- If the radio button is disabled, setFocus() may still set focus visually but interactions won't work
- If the component is destroyed or not rendered, the method may gracefully fail without throwing errors

**Accessibility integration**:
- Provides accessible way to manage keyboard focus from application code
- Enables focus management for screen reader users and keyboard-only users
- Supports proper accessibility patterns like "focus on first invalid element after form submission error"

**Comparison with autoFocus**:
- **autofocus prop**: Automatically sets focus during component initialization (declarative)
- **setFocus() method**: Sets focus programmatically at any time (imperative)
- Both achieve the same visual and functional effect (setting element focus)
- autoFocus is for initialization-time focus, setFocus() is for dynamic/flexible focus management

This is a behavioral method, not a visual prop. It provides programmatic control over keyboard focus without affecting the radio button's appearance or expressive state.

## Events

### selectionChange

A CustomEvent that fires whenever the radio button's selected state changes through user interaction. This event provides the new selected state value and is the primary way to track and respond to radio button selection changes.

**Event payload type**: `CustomEvent<boolean>`

**When it fires**:
- **User clicks**: Fires when user clicks on the radio button circle or label text (if not disabled/readOnly)
- **Keyboard interaction**: Fires when user presses Space key while radio button has focus (if not disabled/readOnly)
- **Does NOT fire**: When selected prop changes programmatically, when radio button is disabled, or when used within a radio button group and selection changes via group logic (may vary based on implementation)

**Payload content**:
- **event.detail**: `boolean` - the new selected state (true when radio button becomes selected, false when it becomes unselected)

**How to use - TypeScript handler**:
```typescript
onSelectionChange(event: CustomEvent<boolean>) {
  const isSelected = event.detail; // Access the boolean via event.detail
  console.log('Radio button selection changed to:', isSelected);
  // Update your state or perform logic based on the new selection state
}
```

**Binding syntax**:
```html
<ion-radio (selectionChange)="onSelectionChange($event)"></ion-radio>
```

**When to use**:
- **Form state management**: Track which option is selected for form submission or validation
- **Dependent controls**: Enable/disable other UI elements based on radio button selection
- **Feature toggles**: Activate/deactivate features when user toggles radio buttons
- **Data filtering**: Filter lists or apply logic based on which radio button is selected
- **State persistence**: Save radio button states to local storage or backend

**Important behaviors**:
- **CustomEvent wrapper**: Remember that event.detail contains the boolean, not event itself
- **Not programmatic changes**: Event only fires for user interactions, not when you change the selected prop yourself from component code
- **Mutual exclusion logic**: For proper radio button group behavior, when this event fires for one radio button, you should deselect other radio buttons with the same name attribute

### focusIn

A CustomEvent that fires when the radio button receives focus through any means. This event signals that the radio button is now the focused element and can be interacted with via keyboard.

**Event payload type**: `CustomEvent<void>`

**When it fires**:
- **User focuses**: When users click on the radio button or label
- **Keyboard navigation**: When users tab to the radio button during keyboard navigation
- **Programmatic focus**: When focus() method is called or when autofocus prop triggers automatic focus
- **Does NOT fire**: For other unrelated DOM events or state changes

**Payload content**:
- **event.detail**: `void` - this event carries no data payload, using event.detail will be undefined

**How to use - TypeScript handler**:
```typescript
onFocusIn(event: CustomEvent<void>) {
  // No data payload - just signals focus state change
  console.log('Radio button received focus');
  const radioElement = event.target as any; // Access the element if needed
  // Perform focus-related actions like showing help text, keyboard shortcuts, etc.
}
```

**Binding syntax**:
```html
<ion-radio (focusIn)="onFocusIn($event)"></ion-radio>
```

**When to use**:
- **Accessibility indicators**: Show help text, keyboard shortcuts, or accessibility hints when radio button gets focus
- **Focus tracking**: Track which radio button currently has focus for keyboard navigation workflows
- **UI state changes**: Update surrounding UI elements based on which radio button is focused
- **Screen reader support**: Trigger specific accessibility behaviors when focus arrives
- **Visual enhancement**: Apply focus styles or visual cues (in addition to browser default focus ring)

**Important behaviors**:
- **No payload**: This is a signalling event purpose, not a data-carrying event
- **Focus ring**: Browser will automatically show focus ring - this event is for additional custom behavior
- **Multiple focus events**: Can fire multiple times as focus moves in and out of the radio button
- **Performance**: Handler should be lightweight to avoid focus navigation delays

### focusOut

A CustomEvent that fires when the radio button loses focus. This event signals that the user has navigated away from the radio button and it's no longer the focused element.

**Event payload type**: `CustomEvent<void>`

**When it fires**:
- **User navigates away**: When users click elsewhere, tab to another element, or otherwise move focus away
- **Blur**: When the radio button loses focus for any reason
- **Does NOT fire**: For disabled radio buttons (they don't receive focus) or for unrelated state changes

**Payload content**:
- **event.detail**: `void` - this event carries no data payload, using event.detail will be undefined

**How to use - TypeScript handler**:
```typescript
onFocusOut(event: CustomEvent<void>) {
  // No data payload - just signals focus state change
  console.log('Radio button lost focus');
  const radioElement = event.target as any; // Access the element if needed
  // Perform blur-related actions like validating, saving state, hiding help text, etc.
}
```

**Binding syntax**:
```html
<ion-radio (focusOut)="onFocusOut($event)"></ion-radio>
```

**When to use**:
- **Validation**: Trigger validation when user leaves the radio button
- **State saving**: Save the selection state or related data when focus moves away
- **UI cleanup**: Hide help text, tooltips, or other UI elements that were shown on focus
- **Form logic**: Update form state when navigation occurs between form fields
- **Accessibility**: Preform accessibility cleanup when focus leaves the region

**Important behaviors**:
- **No payload**: This is a signalling event for focus state changes, not data transmission
- **Focus/blur pair**: Typically used in conjunction with focusIn to track complete focus lifecycle
- **Lost focus detection**: Helps identify when user has moved to another element
- **Timing**: Fires immediately when focus leaves, regardless of why focus moved

**Complete event binding example**:
```html
<ion-radio 
  (selectionChange)="onSelectionChange($event)"
  (focusIn)="onFocusIn($event)"
  (focusOut)="onFocusOut($event)"
  [label]="'Option A'"
  [value]="'option-a'"
  [name]="'my-radio-group'"
  [selected]="isSelected"
></ion-radio>
```

**Combined handler implementation**:
```typescript
class MyComponent {
  isSelected = false;

  onSelectionChange(event: CustomEvent<boolean>) {
    this.isSelected = event.detail;
    console.log('Selection changed:', this.isSelected);
    // Handle radio button selection change
  }

  onFocusIn(event: CustomEvent<void>) {
    console.log('Radio button focused');
    // Show help text or accessibility indicators
  }

  onFocusOut(event: CustomEvent<void>) {
    console.log('Radio button lost focus');
    // Validate selection or save state when user moves away
  }
}
```

## Examples

```html
<ion-radio label="Default Radio Button" [selected]="false" [value]="'option1'"></ion-radio>
```
Demonstrates default radio button with label and unselected state.

```html
<ion-radio 
  label="Emphasized Radio Button" 
  [emphasized]="true" 
  [selected]="true" 
  [value]="'option2'">
</ion-radio>
```
Demonstrates emphasized radio button with selected true state, showing bold styling with primary colors.

```html
<ion-radio 
  label="Small Radio Button" 
  [size]="'sm'" 
  [selected]="true" 
  [value]="'option3'">
</ion-radio>
```
Demonstrates small (sm) size radio button selection.

```html
<ion-radio 
  label="Large Radio Button" 
  [size]="'lg'" 
  [selected]="true" 
  [value]="'option4'">
</ion-radio>
```
Demonstrates large (lg) size radio button selection.

```html
<ion-radio 
  label="Read-only Radio Button" 
  [readOnly]="true" 
  [selected]="true" 
  [value]="'option5'">
</ion-radio>
```
Demonstrates read-only radio button that shows selected state but prevents user interaction.

```html
<ion-radio 
  label="Disabled Radio Button" 
  [disabled]="true" 
  [value]="'option6'">
</ion-radio>
```
Demonstrates disabled radio button that appears grayed out and prevents all interaction.

```html
<ion-radio 
  label="With Aria Label" 
  ariaLabel="Custom aria label for screen readers" 
  [value]="'option7'">
</ion-radio>
```
Demonstrates radio button with custom aria label for accessibility, independent of the visible label text.

```html
<ion-radio 
  label="Auto Focus Radio Button" 
  [autoFocus]="true" 
  [value]="'option8'">
</ion-radio>
```
Demonstrates radio button that automatically receives focus when componentrenders.

```html
<ion-radio 
  [label]="'Event Handler Radio'"
  [value]="'option9'"
  (selectionChange)="onSelectionChange($event)">
</ion-radio>
```
Demonstrates radio button with selectionChange event handler binding.

```html
<ion-radio 
  [label]="'Focus Events Radio'"
  [value]="'option10'"
  (focusIn)="onFocusIn($event)"
  (focusOut)="onFocusOut($event)">
</ion-radio>
```
Demonstrates radio button with both focusIn and focusOut event handlers for focus tracking.

```html
<ion-radio 
  [label]="'Complete Radio'"
  [value]="'option11'"
  [name]="'complete-group'"
  [size]="'md'"
  [emphasized]="false"
  [selected]="isSelected"
  [disabled]="isDisabled"
  [readOnly]="isReadOnly"
  [required]="true"
  [autoFocus]="false"
  (selectionChange)="onSelectionChange($event)"
  (focusIn)="onFocusIn($event)"
  (focusOut)="onFocusOut($event)">
</ion-radio>
```
Demonstrates radio button with comprehensive prop configuration including name, size, emphasis, state props, and all three event handlers.