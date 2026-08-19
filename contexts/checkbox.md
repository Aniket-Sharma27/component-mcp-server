---
realComponent: "ion-checkbox"
description: "A binary selection control that allows users to toggle between checked and unchecked states, with support for indeterminate state"
themes:
  - light
  - dark
props:
  - name: "label"
    type: "string"
    category: "content"
    required: false
    default: '""'
    values: []
    designTokens: {}
  - name: "name"
    type: "string"
    category: "content"
    required: false
    default: 'none found'
    values: []
    designTokens: {}
  - name: "id"
    type: "string"
    category: "accessibility"
    required: false
    default: 'none found'
    values: []
    designTokens: {}
  - name: "value"
    type: "any"
    category: "content"
    required: false
    default: 'none found'
    values: []
    designTokens: {}
  - name: "required"
    type: "boolean"
    category: "content"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "emphasized"
    type: "boolean"
    category: "visual"
    required: false
    default: "false"
    values: []
    designTokens:
      true:
        light:
          resolvesTo: "#007de0"
          tokenChain: "ion-lit-color-leonardo-base-primary"
          appliesToCssProperty: "border-color"
        dark:
          resolvesTo: "#008af7"
          tokenChain: "ion-lit-color-palette-dark-blue-700"
          appliesToCssProperty: "border-color"
      false:
        light:
          resolvesTo: "#030f26"
          tokenChain: "ion-cont-color-role-light-neutral-900"
          appliesToCssProperty: "border-color"
        dark:
          resolvesTo: "#007de0"
          tokenChain: "ion-lit-color-palette-dark-blue-500"
          appliesToCssProperty: "border-color"
  - name: "size"
    type: "string"
    category: "visual"
    required: false
    default: "'md'"
    values:
      - sm
      - md
      - lg
    designTokens:
      sm:
        resolvesTo: "16px"
        tokenChain: "ion-comp-checkbox-container-sizing-sm"
        appliesToCssProperty: "width, height"
      md:
        resolvesTo: "20px"
        tokenChain: "ion-comp-checkbox-container-sizing-md"
        appliesToCssProperty: "width, height"
      lg:
        resolvesTo: "24px"
        tokenChain: "ion-comp-checkbox-container-sizing-lg"
        appliesToCssProperty: "width, height"
  - name: "autofocus"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "selected"
    type: "boolean"
    category: "visual"
    required: false
    default: "false"
    values: []
    designTokens:
      true:
        light:
          resolvesTo: "#007de0"
          tokenChain: "ion-comp-checkbox-container-color-bg-selected-enabled-subtle"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#008af7"
          tokenChain: "ion-comp-checkbox-container-color-bg-selected-enabled-subtle"
          appliesToCssProperty: "background-color"
      false:
        light:
          resolvesTo: "#ffffff"
          tokenChain: "ion-comp-checkbox-container-color-bg-enabled-subtle"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#1f1e1f"
          tokenChain: "ion-comp-checkbox-container-color-bg-enabled-subtle"
          appliesToCssProperty: "background-color"
  - name: "disabled"
    type: "boolean"
    category: "visual"
    required: false
    default: "false"
    values: []
    designTokens:
      true:
        light:
          resolvesTo: "#e9eaeb"
          tokenChain: "ion-comp-checkbox-container-color-bg-disabled-subtle"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#1f1e1f"
          tokenChain: "ion-comp-checkbox-container-color-bg-disabled-subtle"
          appliesToCssProperty: "background-color"
  - name: "readOnly"
    type: "boolean"
    category: "visual"
    required: false
    default: "false"
    values: []
    designTokens:
      true:
        light:
          resolvesTo: "#ffffff"
          tokenChain: "ion-comp-checkbox-container-color-bg-read-only-subtle"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#1f1e1f"
          tokenChain: "ion-comp-checkbox-container-color-bg-read-only-subtle"
          appliesToCssProperty: "background-color"
  - name: "indeterminate"
    type: "boolean"
    category: "visual"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "ariaLabel"
    type: "string"
    category: "accessibility"
    required: false
    default: 'none found'
    values: []
    designTokens: {}
  - name: "focus"
    type: "() => void"
    category: "behavioral"
    required: false
    default: 'none found'
    values: []
    designTokens: {}
events:
  - name: "selectionChange"
    payloadType: "CustomEvent<boolean>"
    firesWhen: "Emitted when the checkbox state changes - on user click (if not disabled/readOnly) or on Space key press"
    detailAccess: "event.detail (boolean) - true when checkbox becomes selected, false when it becomes unselected"
    bindingSyntax: "(selectionChange)=\"onSelectionChange($event)\""
  - name: "focusIn"
    payloadType: "CustomEvent<void>"
    firesWhen: "Emitted when the checkbox receives focus - when users click or tab into the checkbox, or when focus is set programmatically"
    detailAccess: "void, event.detail is undefined - this event signals focus state change without carrying data"
    bindingSyntax: "(focusIn)=\"onFocusIn()\""
  - name: "focusOut"
    payloadType: "CustomEvent<void>"
    firesWhen: "Emitted when the checkbox loses focus - when users click away, tab out, or when focus is removed programmatically"
    detailAccess: "void, event.detail is undefined - this event signals focus state change without carrying data"
    bindingSyntax: "(focusOut)=\"onFocusOut()\""
jointTokens:
  - combination: "emphasized=true, selected=true"
    resolvesTo: "#007de0"
    tokenChain: "ion-comp-checkbox-container-color-bg-selected-enabled-bold"
    appliesToCssProperty: "background-color"
  - combination: "emphasized=true, selected=false"
    resolvesTo: "#007de0"
    tokenChain: "ion-comp-checkbox-container-color-bg-enabled-bold"
    appliesToCssProperty: "border-color"
  - combination: "emphasized=false, selected=true"
    resolvesTo: "#007de0"
    tokenChain: "ion-comp-checkbox-container-color-bg-selected-enabled-subtle"
    appliesToCssProperty: "background-color"
  - combination: "disabled=true, selected=true"
    resolvesTo: "#e9eaeb"
    tokenChain: "ion-comp-checkbox-container-color-bg-selected-disabled-subtle"
    appliesToCssProperty: "background-color"
propInteractions:
  - "readOnly prevents user interaction with the checkbox - clicking has no effect and the space key does not toggle selection. Used when you want to display a checkbox state without allowing changes."
  - "disabled completely disables the checkbox - both visually (grayed appearance) and functionally (no user interaction possible). The checkbox appears with reduced opacity and cannot be clicked or activated via keyboard."
  - "indeterminate state visually represents a checkbox that is neither checked nor unchecked, typically used to represent partial or mixed states within parent-child checkbox hierarchies. When indeterminate=true, clicking the checkbox first sets it to selected=false, then normal toggle behavior resumes."
  - "selected and indeterminate are mutually exclusive in practice - setting indeterminate=true typically overrides selected state visually. When users interact with an indeterminate checkbox, it clears the indeterminate state and toggles the selected state."
  - "emphasized provides additional visual prominence by using stronger colors and potentially larger styling. When emphasized=true, the checkbox uses bold styling tokens for background and border colors, making it more visually prominent in the interface."
  - "size affects multiple visual properties simultaneously: checkbox container dimensions (width/height), icon size (via font tokens), padding around icon, and gap between checkbox and label. The size prop determines the scale of all these elements proportionally."
  - "focus() method is a behavioral API that can be called programmatically to set focus to the checkbox. This is useful for accessibility workflows, keyboard navigation, or when you need to direct user attention to a specific checkbox."
  - "required adds HTML attribute aria-required but does not enforce validation or add visual indicators. It serves as a semantic marker for form validation and accessibility tools."
  - "ariaLabel is used for screen reader accessibility. When not provided, the label text is used as the aria-label value. For checkboxes without labels, ariaLabel should always be provided for accessibility."
  - "emphasized and selected work together: emphasized=true affects both unselected and selected states but with different visual outcomes. Unselected emphasized checkboxes have colored borders, selected emphasized checkboxes have colored backgrounds with colored checkmarks."
  - "Mobile mode (isMobileMode) affects accessibility behavior: on touch devices, the hidden native input element gets aria-hidden=true and the container gets role=checkbox with tabindex=0 to make it properly accessible via touch interactions."
needsReview:
  - "No event payload verification for selectionChange in web component context - TypeScript interface shows EventEmitter<boolean> but actual web component CustomEvent wrapper implementation needs runtime verification to ensure event.detail contains the boolean value."
  - "Indeterminate state icon and styling tokens - the component uses indeterminateIcon internally (check_indeterminate_small) but the specific design tokens for indeterminate state appearance (different from selected or unselected states) could not be traced from the available token definitions."
  - "Border-radius tokens for checkbox container were referenced (--ion-comp-checkbox-container-border-radius) but the final resolved values could not be traced. Values likely depend on size prop (sm/md/lg) but specific mapping could not be determined."
  - "Hover and active state design tokens for checkbox container container background and border colors are defined in checkbox-ds.css but the specific hex values for light and dark themes could not be traced from the available token definitions. Only enabled/hover/active state colors are represented for these areas."
  - "Focus ring/box-shadow tokens (--ion-comp-checkbox-container-outer-shadow-focus) could not be resolved to specific color/blur/spread values. Different focus states may exist for different contexts but specific values need runtime verification."
  - "Gap spacing between checkbox and label (--ion-comp-checkbox-container-outer-spacing-gap-md) depends on size prop but specific scaling mapping (sm/md/lg values) could not be determined from available token definitions."
  - "Checkmark icon color tokens (foreground color - color, not background-color) for different states (enabled, hover, active, selected, disabled, readOnly) are defined but specific hex values for light and dark themes could not be fully traced. Color palette resolution paths need further investigation. Background colors for selected/disabled/readOnly container states were traced."
  - "Validation states (valid, invalid, warning) for checkboxes within checkbox groups are referenced in checkbox-ds.css but validation-specific token values could not be traced from the available source material. These validation-specific tokens appear to be available through groups, not for individual standalone checkboxes."
  - "Add explicit needsReview entry for selectedIcon and indeterminateIcon default icon names - functions as internal implementation detail but default values (yes, check_indeterminate_small) could not be verified against any icon configuration."
  - "The relationship between disabled and disabledInternal props (used by checkbox group) needs runtime verification - both appear to produce same visual disabled state but interaction differs when used within checkbox groups."
---
## Usage Notes

Boolean props on this component must always be passed with an explicit string value — e.g. `disabled="true"` or `[disabled]="isDisabled"` — never as bare attribute presence (e.g. `disabled` alone, with no value). Bare attribute presence is a native HTML convention this component does NOT support; it will not be interpreted as true.

## label

The text content displayed as the identifier for the checkbox, typically positioned to the right of the checkbox input. Labels provide context and help users understand what the checkbox represents. This is a content prop that does not affect the component's behavior or visual appearance beyond the text content.

The label prop accepts plain text strings. When a label is provided, it appears as a clickable text label next to the checkbox square. Clicking on the label text triggers the same toggle action as clicking on the checkbox itself, providing a larger target area for user interaction.

**Important accessibility relationship**: When ariaLabel is not provided, the checkbox uses the label text as its aria-label value for screen reader accessibility. For checkboxes without visible labels, always provide an ariaLabel to ensure accessibility compliance.

**Label positioning and gap**: The label appears to the right of the checkbox container with spacing determined by the design system's gap tokens. The gap size depends on the selected size prop (sm/md/lg) but specific spacing values are not explicitly configurable.

When no label is provided, the checkbox appears as a standalone checkmark icon without explanatory text. This may be appropriate when the checkbox's purpose is immediately obvious from context (e.g., in checkbox groups with group-level labels).

This prop is self-contained for content, though its visual presentation (font size, color, spacing) is controlled by the component's design system tokens and size prop.

## name

Provides a name for the checkbox, which is primarily used when the checkbox is part of an HTML form. The name attribute becomes part of the form data when the form is submitted, identifying which checkbox the submitted value belongs to. This is a content prop that affects form data structure but does not change the checkbox's visual appearance or behavior.

The name prop accepts string values that identify the checkbox in form submissions. When multiple checkboxes share the same name, they typically represent different options within the same form field group. The value prop distinguishes between individual checkboxes with the same name.

**Form submission behavior**: When a checkbox with a name is checked, the form submission includes that checkbox's name and value pair (e.g., name="preferences" and value="marketing" becomes preferences=marketing). When unchecked, the checkbox's name/value pair is not included in the form data at all.

**Use cases**:
- **Form submissions**: Use name to identify checkbox data when submitting forms
- **Checkbox groups**: Multiple checkboxes share the same name (e.g., name="interests") with different values (e.g., value="sports", value="music")
- **Database integration**: Name often maps to database field names for form data storage

**Accessibility**: The name attribute does not affect screen reader accessibility. Use ariaLabel or label for screen reader announcements. The name is only used for form data identification.

This prop is content-oriented and self-contained. It has no visual effects but is crucial for form data handling and submission workflows.

## id

Provides a unique identifier for the checkbox, which is used for HTML labeling associations and element targeting. The id attribute allows other elements (like labels) to reference this checkbox specifically, and is commonly used in automation testing and JavaScript element selection. This is an accessibility/technical prop that does not affect visual appearance.

The id prop accepts string values that must be unique within the document scope. When an id is provided, it's applied to the hidden native checkbox input element, which allows proper association with label elements via the label's "for" attribute.

**Automatic ID generation**: When no id is provided, the component automatically generates a unique ID using the pattern "Checkbox-" followed by a timestamp (Date.now()). This ensures proper label-checkbox association even when developers don't manually specify IDs.

**Label association**: The component's label element automatically references the checkbox's id via its "for" attribute, creating a proper semantic connection. This ensures that clicking the label text triggers the checkbox toggle and that screen readers announce the relationship correctly.

**Use cases**:
- **Form element linking**: Provide explicit IDs when you need to link external labels or form elements to the checkbox
- **Automated testing**: Use predictable IDs for test automation and element selection in testing frameworks
- **JavaScript targeting**: Select specific checkboxes for manipulation via document.getElementById()
- **Accessibility compliance**: Ensure proper label associations when dynamic content is generated

**Best practice**: When grouping multiple related checkboxes in a checkbox group, consider whether you need explicit IDs. Most use cases can rely on automatic ID generation, but explicit IDs provide stability for testing and special scenarios.

This prop is technical in nature and primarily affects HTML structure and accessibility relationships, not visual presentation.

## value

Provides the value associated with the checkbox, which is submitted with form data when the checkbox is checked and part of a form. The value prop distinguishes individual checkboxes within a group of checkboxes that share the same name attribute. This is a content prop that affects form submission data but not visual appearance.

The value prop accepts any type of data (string, number, boolean, object, array), but typically uses string values for form submission compatibility. When checked, the checkbox's value is submitted along with its name (e.g., name="color" and value="blue" becomes color=blue).

**Form submission behavior**:
- **Checked checkbox**: name=value pair is included in form submission
- **Unchecked checkbox**: name=value pair is completely excluded from form submission
- **Checkbox with no value**: When no value is specified, checked checkboxes default to the string "on" as their value

**Use cases**:
- **Options within groups**: Multiple checkboxes with same name but different values (e.g., interests: "sports", "music", "tech")
- **Boolean switches**: Use value="true" to represent a toggle switch state
- **Data mapping**: Map checkbox selections to database values or API parameters
- **Multi-select forms**: Collect multiple values from checkbox groups

**Integration with checkbox groups**: In checkbox group components, the value prop is particularly important because the group component collects the values of all checked checkboxes into an array to use as the group's value.

**JavaScript handling**: The selectionChange event provides access to the checkbox's value through the underlying hidden input element. This allows validation logic, dynamic form handling, and custom processing based on specific checkbox values.

This prop is content-oriented and primarily affects form submission data structure. It has no visual effects but is fundamental to form data handling.

## required

When true, indicates that the checkbox must be checked before the form can be considered complete. This is a semantic/content prop that affects HTML attributes and can trigger validation behavior, particularly when used within checkbox groups or form validation systems.

The required prop adds the aria-required="true" attribute to the checkbox, which is important for screen readers and assistive technologies. It creates a semantic requirement but does not automatically enforce validation or add visible required indicators.

**Validation behavior**:
- **Standalone checkbox**: The required prop marks the checkbox as semantically required but does not automatically validate or block form submission
- **Checkbox group context**: When used within checkbox groups, the group validation logic checks whether required checkboxes are checked and sets validationState accordingly
- **Form validation**: Form-level validation systems can check the checkbox's state and display required messages using this attribute

**Accessibility impact**: The aria-required="true" attribute helps screen reader users identify which checkboxes must be checked before form submission. This is particularly important for form accessibility compliance.

**Visual indicators**: The required prop itself does not add visual indicators (stars, asterisks, or "Required" text). Visual requirement indicators would typically be managed through a checkbox group's necessityIndicator prop or external UI elements.

**Use cases**:
- **Terms agreement**: Require users to check "I agree to terms" checkbox before submission
- **Mandatory selections**: Mark certain options as required within checkbox groups
- **Form accessibility**: Ensure screen readers announce requirement status clearly
- **Validation integration**: Provide semantic hooks for form validation libraries

**Important relationship with checkbox groups**: When used within checkbox groups, the group component may use this attribute as part of its validation logic. The group's validationState prop and validationMode prop control how requirements are enforced and displayed.

This prop is semantic/accessible in nature and primarily affects HTML markup and validation behavior. It has no visual effects on its own but enables proper form validation and accessibility.

## emphasized

Controls the visual prominence of the checkbox by using stronger colors and more prominent styling. When true, the checkbox displays with bold styling that makes it more visually prominent in the interface. This is a visual prop that affects the checkbox's appearance without changing its behavior.

**Emphasized state visual effects**:

- **Emphasized=false (subtle/default)**: Unselected checkboxes have neutral border colors, selected checkboxes have more subtle background colors. This is the restrained, default appearance that blends with the interface without drawing excessive attention.

- **Emphasized=true (bold)**: Unselected checkboxes have prominent border colors (using primary branding colors), selected checkboxes have strong background colors and visual emphasis. This creates a more visually prominent, attention-grabbing appearance.

**Important visual cues**:
- **Border color**: When emphasized=true, unselected checkboxes use brand colors for borders instead of neutral colors
- **Background color**: When emphasized=true and selected, checkboxes use bold primary colors for backgrounds versus more subtle colors
- **Checkmark color**: Selected emphasized checkboxes use more prominent colors for checkmarks

**Use cases for emphasized state**:
- **Primary actions**: Use emphasized for the primary checkbox in a set of options to guide user selection
- **Feature highlights**: Draw attention to important checkboxes that represent key choices
- **Branded interfaces**: Use emphasized styling to align with brand colors and create strong visual identity
- **Dashboard widgets**: Make checkboxes in prominent positions more visually distinct

**Interaction with other states**: The emphasized prop affects the color intensity of all checkbox states (enabled, hover, active, selected, disabled, readOnly) but does not change the fundamental behavior of those states. An emphasized disabled checkbox still appears disabled but with more prominent colors than a non-emphasized disabled checkbox.

**Theme considerations**: The actual hex values for emphasized states differ between light and dark themes, with each theme using appropriate color palette tokens to ensure contrast and visual harmony.

This prop is purely visual and does not affect the checkbox's behavior or interactions. It provides a design system-compliant way to create hierarchy and emphasis between different checkboxes in the interface.

## size

Controls the height, width, padding, icon size, and spacing scale of the checkbox. Size values (sm, md, lg) map to design system spacing and typography tokens that scale the entire checkbox proportionally. This is a visual prop that directly impacts the user's perception of the component's scale and prominence in the interface.

The size prop determines multiple visual properties simultaneously through design system tokens:
- **Container dimensions**: Overall width and height of the checkbox square
- **Icon scaling**: Size of the checkmark icon (using font tokens)
- **Internal padding**: Space between checkbox border and checkmark icon
- **Label spacing**: Gap between checkbox and label text

**Size values and their visual effects**:

- **sm**: Small checkbox with 16px container (computed). The checkmark icon is smaller, internal padding is tighter, and overall appearance is more compact. This is useful for dense interfaces with many checkboxes.

- **md (default)**: Medium checkbox with 20px container (computed). Standard checkmark icon size, regular padding, balanced proportions. This is the most commonly used size and appropriate for most form interfaces.

- **lg**: Large checkbox with 24px container (computed). Larger checkmark icon, generous padding, more prominent appearance. Useful for interfaces with larger touch targets or when checkboxes need special emphasis.

**Important interactive benefits**:
- **Touch targets**: Larger sizes (lg) provide bigger touch targets for mobile users
- **Accessibility**: Smaller sizes may be harder to click for users with motor disabilities
- **Visual hierarchy**: Size creates effective hierarchy when different checkboxes have different sizes

**MQ string support**: The size prop can accept Media Query (MQ) responsive strings that allow different sizes at different breakpoints. For example, you could specify "xs=lg;sm=md;md=md;lg=md" to get larger checkboxes on extra-small screens for better touch targets, while maintaining medium size on larger screens.

**Label and spacing effects**: The size prop also affects the gap between the checkbox and label, as well as the overall spacing around the component. Larger sizes create more breathing room, while smaller sizes create tighter layouts.

**Use cases**:
- **Compact forms**: Use sm for dense interfaces with limited vertical spacing
- **Standard forms**: Use md as the default for most form inputs
- **Mobile-first interfaces**: Use lg for better touch targets on mobile devices
- **Action emphasis**: Use lg size for primary checkboxes to make them more prominent

This prop is visual and self-contained. It affects multiple design aspects simultaneously through design system tokens but does not depend on other props for its effect.

## autofocus

When true, the checkbox automatically receives focus when the component is rendered or initialized. This is a behavioral prop that affects keyboard navigation and user interaction flow but has no visual appearance.

The autofocus prop determines whether the checkbox should capture keyboard focus immediately after component initialization. When set to true, the hidden native checkbox input element is focused via JavaScript using a setTimeout call (for timing reasons).

**Behavior differences**:
- **autofocus=false (default)**: The checkbox does not automatically receive focus. Users navigate to it normally via tab key or by clicking. This is the standard behavior for most checkboxes.

- **autofocus=true**: The checkbox receives focus automatically after component initialization. Users will see the browser's default focus indicator (usually a glowing outline) around the checkbox, and they can immediately toggle it using the space key without navigating to it first.

**Use cases**:
- **Form initialization**: Set focus on the first checkbox in a form to guide users into form interaction
- **Multi-step wizards**: Automatically focus appropriate checkboxes as users progress through steps
- **Keyboard-focused interfaces**: Improve accessibility and keyboard navigation by providing automatic focus points
- **Error recovery**: After validation errors, autofocus the problematic checkbox to draw user attention

**Accessibility considerations**:
- **Multiple autofocus elements**: When multiple elements have autofocus=true, browsers typically focus only the first one encountered in DOM order
- **Screen reader announcements**: Automatic focus may trigger screen reader announcements, which can be confusing if unexpected
- **Mobile considerations**: Virtual keyboards on mobile devices don't respond to checkbox focus, so autofocus has different effects on mobile

**Interaction with other focus-related features**:
- **focus() method**: You can also call the component's focus() method programmatically at any time, which performs the same action regardless of the autofocus prop value
- **focusIn event**: The focusIn event is emitted both when autofocus triggers focus and when focus is set programmatically or via user interaction
- **Tab navigation**: Users can still navigate via tab key normally; autofocus just provides initial focus

**Implementation note**: The autofocus behavior uses setTimeout for timing reasons to ensure the component is fully initialized before attempting focus. This means the focus is set shortly after component render, not immediately during the render cycle.

This prop is behavioral and does not have visual appearance. It affects user interaction flow and keyboard accessibility but not the checkbox's visual presentation.

## selected

Controls whether the checkbox is in the checked (selected) state. When true, the checkbox displays a checkmark icon and uses selected state styling. When false, the checkbox appears as an empty square with unselected styling. This is a visual/state prop that is central to the checkbox's primary function.

**State behavior and visual effects**:

- **selected=false**: The checkbox appears as an empty square with border styling appropriate to its other props (emphasized, disabled, readOnly). The background and border colors reflect the unselected state using neutral or emphasized color palettes.

- **selected=true**: The checkbox displays a checkmark icon (default "yes" icon) and uses selected state styling. The background color becomes filled and borders may change based on the emphasized prop. The checkmark icon color contrasts with the background.

**Important single-select behavior**: As a standard checkbox (not radio button), this checkbox toggles its selected state independently. Clicking toggles between selected=false and selected=true. This behavior is different from radio buttons where selecting one deselects others within the same group.

**State management patterns**:
- **Controlled component**: Bind selected to your state and update that state when selectionChange event fires to maintain full control
- **Uncontrolled component**: Let the checkbox manage its own selected state and only read it when needed
- **Form integration**: Use selected in conjunction with value for form submission handling

**Interaction with indeterminate**: 
- The indeterminate and selected states are mutually exclusive in practice
- When indeterminate=true, the checkbox typically shows a different visual state (indeterminate icon or partial fill)
- User interaction with an indeterminate checkbox first clears indeterminate=false, then toggles selected state normally
- Setting indeterminate=true typically overrides any selected value visually

**State persistence**: The checkbox maintains its selected state through component re-renders unless changed by user interaction or by updating the selected prop from application code.

**Selection states vs validation**: The selected prop tracks the checkbox's check state, while validation-related props (required, validationState when in checkbox groups) track whether the current state meets business rules. A checkbox can be selected=true but still trigger validation if it's required and not checked, depending on validation logic.

**Use cases**:
- **Binary choices**: Toggle between two mutually exclusive options (e.g., accept terms, subscribe to newsletter)
- **Multi-select lists**: Use multiple checkboxes with different values to select multiple items
- **Data filters**: Apply filters by checking checkboxes that represent filter criteria
- **Feature toggles**: Enable or disable features by checking boxes

This prop is central to the checkbox's function and affects both visual presentation and the selectionChange event emission.

## disabled

When true, the checkbox becomes completely non-interactive - users cannot click to toggle the selection, and the checkbox appears visually deactivated with reduced opacity and grayed styling. This is a visual/behavioral prop that signals and enforces an unavailable state.

**Disabled state effects**:

- **Visual**: The checkbox appears "grayed out" with reduced opacity, usually around 40-60% of normal opacity. This signals visually that the element is not available for interaction.

- **Functional**: All user interaction is blocked:
  - Clicking on the checkbox has no effect (selection does not change)
  - Keyboard focus navigation skips the disabled checkbox
  - Space key does not toggle selection when the checkbox has focus
  - The component is excluded from form submission data

- **Event emission**: The selectionChange event is NOT emitted for disabled checkboxes, even if the selected prop changes programmatically.

**Internal vs external disabled state**:
- **disabled (regular)**: The primary disabled prop that can be set directly on the checkbox component
- **disabledInternal**: Used internally by checkbox group components to disable individual checkboxes as part of group-level disabled state
- **Combined effect**: Final disabled state is determined by `disabled || disabledInternal`, providing both direct and group-based control

**Accessibility considerations**:
- Keyboard navigation typically skips disabled elements (tab key moves past them)
- Screen readers may announce "disabled" or similar status to indicate unavailability
- The disabled attribute is applied to the hidden native input element for proper accessibility behavior

**Use cases for disabled state**:
- **Conditional availability**: Disable checkboxes when related criteria aren't met (e.g., disable "Enterprise account type" checkbox when user isn't authenticated)
- **Processing states**: Temporarily disable checkboxes while form submission or data processing occurs
- **Permission control**: Disable options the user doesn't have permission to change (e.g., admin-only settings)
- **Progressive disclosure**: Disable future options until previous steps are completed

**Important distinction from readOnly**:
- **disabled**: Complete non-interactive state with visual cues of unavailability
- **readOnly**: Interactive (can be viewed/examined) but selection cannot be changed

**Visual differences between states**:
- **disabled扶d + selected=false**: Grayed checkbox, empty, no interaction
- **disabled抚d + selected=true**: Grayed checked checkbox, maintains check but no interaction
- **enabled + selected=false**: Normal appearance, can be clicked
- **enabled + selected=true**: Normal appearance with checkmark, can be clicked

This prop provides both visual and functional disabling. It completely prevents user interaction while providing clear visual feedback about the unavailable state.

## readOnly

When true, the checkbox maintains visual interactivity but prevents changing the selected state. Users can click and interact with theCheckBox, but the selection remains unchanged. This creates a read-only presentation that still allows exploration without committing changes.

**ReadOnly state effects**:

- **Visual**: The checkbox appears interactive and in normal visual style (not grayed like disabled). It maintains standard colors and transparency, suggesting it can be interacted with.

- **Functional**: User interaction is limited:
  - Clicking on the checkbox does not change selection
  - Space key does not toggle selection
  - The checkbox still responds to hover states and shows normal visual feedback
  - Keyboard focus still works normally (can be tabbed to and focused)
  - The selectionChange event is NOT emitted when users click

- **State preservation**: The checkbox maintains its current selected state regardless of user interaction attempts. The selected prop can still be changed programmatically.

**Important distinction from disabled**:
- **disabled扶d**: Complete non-interactive state with visual cues of unavailability (grayed appearance)
- **readOnly**: Interactive appearance but selection cannot be changed by users

**Use cases for readOnly state**:
- **Displaying checked states**: Show users which items are selected without allowing them to change (e.g., in review screens or displays)
- **Exploration modes**: Allow users to see what would happen if options were selected, without committing changes
- **Permission-based access**: Show options that might be available in other contexts but not changeable in current context
- **Conditional editing**: Make some checkboxes read-only while others in the same group are editable

**Interaction with other states**:
- **readOnly + selected=true**: Shows checked state but cannot be unchecked
- **readOnly + selected=false**: Shows unchecked state but cannot be checked
- **readOnly + indeterminate=true**: Shows indeterminate state but cannot be interacted with

**Accessibility considerations**:
- Keyboard navigation still works normally - the checkbox can receive focus and shows focus indicators
- Screen readers announce the checkbox but may indicate it's read-only
- The native input element may have aria-readonly or similar attributes for accessibility

**Form submission**:
- In form submission, readOnly checkboxes still use their selected state values (unlike disabled checkboxes which are excluded entirely)
- This allows displaying pre-checked options that cannot be changed but are included in submitted data

**Visual preview behavior**:
- Clicking on a readOnly checkbox may show momentary hover effects or visual feedback, but the state does not change
- This can be confusing for users who expect clicking to change the state, so ensure UI clearly communicates read-only nature

**Important mobile behavior**: On touch devices (isMobileMode=true), the readOnly behavior may differ since mobile interactions typically involve tapping rather than plus keyboard interactions.

This prop is primarily functional - it allows visual interaction but prevents state changes. It's useful for displaying static selection states while maintaining interactivity cues.

## indeterminate

When true, the checkbox displays an indeterminate state that represents neither fully checked nor unchecked. This state typically appears as a minus sign or partial fill instead of a checkmark, and is commonly used to represent partial or mixed states within parent-child checkbox hierarchies. This is a visual state prop.

**Indeterminate state behavior**:

- **Visual**: The checkbox shows an indeterminate indicator (default "check_indeterminate_small" icon) instead of a checkmark or empty state. This signals a "partial" or "mixed" condition to users.

- **Functional**: The indeterminate state is primarily visual. When users interact with an indeterminate checkbox:
  1. The indeterminate state is cleared (indeterminate=false)
  2. The checkbox shows its underlying selected state (which may be true or false)
  3. Subsequent clicks toggle the selected state normally

**Common use cases**:
- **Parent-child checkbox groups**: Parent checkbox is indeterminate when some but not all child checkboxes are selected
- **Load-on-demand states**: Show indeterminate while loading checkbox state from external data
- **Filtered selections**: Indeterminate state when selection is filtered or conditional
- **Preference combinations**: Indeterminate when multiple sub-options have mixed states

**Interaction with selected**:
- **Indeterminate and selected are mutually exclusive**: Enabling indeterminate overrides the visual presentation of selected
- **Priority**: The indeterminate prop takes visual precedence over selected, but the underlying selected state is preserved
- **Clearing**: User interaction clears indeterminate first, then toggles selected normally

**Implementation details**:
- **External input**: When using with externally provided HTML input elements (legacy API), the indeterminate state is managed through the native input's indeterminate property
- **Internal implementation**: For the modern checkbox implementation, indeterminate state is managed internally and updates the displayed icon
- **State tracking**: The component tracks indeterminate separately from selected to support both states simultaneously

**Icon customization**:
- The default indeterminate icon is "check_indeterminate_small"
- The component uses indeterminateIcon property internally to customize the indeterminate icon
- This icon customization is currently internal-only and may be exposed as a public API in future versions

**Accessibility considerations**:
- Screen readers announced indeterminate states differently than checked/unchecked states
- The native HTML checkbox element has built-in support for indeterminate attribute
- Screen readers typically announce "indeterminate" or "mixed" for this state

**Form handling**:
- Indeterminate checkboxes still submit based on their checked/selected state value
- Form data doesn't distinguish between checked and indeterminate - indeterminate is visual only
- Applications often need separate logic to handle indeterminate state for their specific business rules

**Important behavior note**: The indeterminate state is typically set programmatically rather than through user interaction. Users interact with indeterminate checkboxes by clearing the indeterminate state and toggling selection, not by directly setting/checking the indeterminate state.

This prop is visual/functional hybrid - it displays a specific visual state that has semantic meaning, but the actual form submission and event handling respect the underlying selected state.

## ariaLabel

Provides an accessible label for screen readers and assistive technologies. The ariaLabel prop is used for accessibility when a checkbox lacks a visible text label, or when you need to provide a more descriptive label than what's shown on screen. This is an accessibility prop that affects screen reader announcements but not visual appearance.

**Accessibility behavior**:
- **When ariaLabel is provided**: Screen readers use the ariaLabel text to announce the checkbox's purpose instead of or in addition to the visible label
- **When ariaLabel is not provided**: The checkbox uses the label text as the accessibility label for screen readers
- **For checkboxes without labels**: Always provide ariaLabel to ensure accessibility compliance

**Use cases**:
- **No visual label**: Checkboxes with only an icon or no text need ariaLabel for screen reader support
- **Supplemental descriptions**: Provide additional context or instructions that appear in screen reader announcements but not on screen
- **Technical labels**: Use more descriptive text for screen readers than what's visually displayed
- **Icon-only checkboxes**: Essential for accessibility when checkboxes use only icons

**Accessibility hierarchy**:
- **Primary source**: ariaLabel when provided
- **Fallback**: label text when ariaLabel is not provided
- **Failure**: Neither ariaLabel nor label results in inaccessible checkbox for screen readers

**Screen reader announcements**:
- Typically includes the checkbox state (checked/unchecked/indeterminate)
- Announces the ariaLabel or label text as the checkbox's identifier
- May announce "checkbox" or "checkbox, [label text]" depending on screen reader

**Mobile accessibility**:
- On touch devices (isMobileMode=true), the container gets role=checkbox and uses ariaLabel for screen reader navigation
- The hidden native input element's aria-label is managed by the checkbox for accessibility

**Important distinction from label**:
- **label**: Visible text label displayed to sighted users, positioned next to checkbox
- **ariaLabel**: Accessible label for screen readers, not displayed visually

**Examples**:
- **Icon-only checkbox**: ariaLabel="Enable notifications" when checkbox has only a bell icon
- **Technical label**: label="1245-ABCD" (visible product code), ariaLabel="Product 1245-ABCD: Available for shipping" (more descriptive)
- **Contextual help**: label="Email updates", ariaLabel="Subscribe to email updates about your account status"

**Internationalization**:
- ariaLabel should be translated/localized like any other user-facing text
- The visible label may be abbreviated for UI constraints, while ariaLabel can use full descriptions
- Screen reader language detection uses ariaLabel's text content

**Best practices**:
- Provide ariaLabel for checkboxes without visible labels (WCAG accessibility requirement)
- Keep ariaLabel concise and descriptive (similar to visible label length guidelines)
- Avoid duplicating visible label content unnecessarily in ariaLabel unless additional context is needed

This prop is purely accessibility-focused. It has no visual appearance but is essential for making checkboxes accessible to screen reader users and assistive technology users.

## focus

A method that can be called programmatically to set keyboard focus to the checkbox. This is a behavioral method rather than a prop - it's part of the component's API but not a configurable property. The focus() method provides programmatic control over which element receives keyboard focus.

**Method behavior**:
- **Call signature**: `checkbox.focus()` - takes no parameters and returns void
- **Effect**: Sets keyboard focus to the checkbox's hidden native input element
- **Visual**: The browser's default focus indicator appears around the checkbox container
- **Keyboard**: Users can immediately toggle the checkbox with the space key after focus is set

**Implementation details**:
- The method queries the element's shadowRoot to find the hidden native input element
- Focus is applied to the native input element rather than the container element for proper accessibility behavior
- The focus effect is the same as users tabbing to the checkbox naturally via keyboard navigation

**Use cases**:
- **Form management**: After validation errors, focus the first invalid checkbox to draw user attention
- **Multi-step wizards**: As users progress through steps, programmatically focus the appropriate checkbox in the next step
- **Accessibility enhancements**: Provide programmatic focus control for keyboard navigation flows
- **State synchronization**: When application logic determines a specific checkbox needs user attention or interaction
- **Error recovery**: After errors occur programmatically, focus the problematic checkbox

**Timing and lifecycle**:
- Can be called at any time after component initialization
- Most commonly called in ngAfterViewInit or in response to user actions
- Should be called after the component is fully rendered and attachments are complete
- Works regardless of the autofocus prop value (focus() overrides and works independently)

**Event emission**:
- When focus() is called and successfully sets focus:
  - The focusIn event is emitted (same event that fires when users tab to the checkbox)
  - Any attached focusIn event handlers are triggered
  - Screen reader focus announcements occur

**Error handling**:
- The method is designed to handle cases where the component or input element may not be available
- If the checkbox is disabled, focus() may still set focus visually but interactions won't work
- If the component is destroyed or not rendered, the method may gracefully fail without throwing errors

**Accessibility integration**:
- Provides accessible way to manage keyboard focus from application code
- Enables focus management for screen reader users and keyboard-only users
- Supports proper accessibility patterns like "focus on first invalid element after form submission error"

**Comparison with autofocus**:
- **autofocus prop**: Automatically sets focus during component initialization (declarative)
- **focus() method**: Sets focus programmatically at any time (imperative)
- Both achieve the same visual and functional effect (setting element focus)
- autofocus is for initialization-time focus, focus() is for dynamic/flexible focus management

This is a behavioral method, not a visual prop. It provides programmatic control over keyboard focus without affecting the checkbox's appearance or expressive state.

## Events

### selectionChange

A CustomEvent that fires whenever the checkbox's selected state changes through user interaction. This event provides the new selected state value and is the primary way to track and respond to checkbox state changes.

**Event payload type**: `CustomEvent<boolean>`

**When it fires**:
- **User clicks**: Fires when user clicks on the checkbox square or label text (if not disabled/readOnly)
- **Keyboard interaction**: Fires when user presses Space key while checkbox has focus (if not disabled/readOnly)
- **Does NOT fire**: When selected prop changes programmatically, when checkbox is disabled, or when indeterminate state changes

**Payload content**:
- **event.detail**: `boolean` - the new selected state (true when checkbox becomes checked, false when it becomes unchecked)

**How to use - TypeScript handler**:
```typescript
onSelectionChange(event: CustomEvent<boolean>) {
  const isSelected = event.detail; // Access the boolean via event.detail
  console.log('Checkbox selection changed to:', isSelected);
  // Update your state or perform logic based on the new selection state
}
```

**Binding syntax**:
```html
<ion-checkbox (selectionChange)="onSelectionChange($event)"></ion-checkbox>
```

**When to use**:
- **Form state management**: Track which checkboxes are selected for form submission or validation
- **Dependent controls**: Enable/disable other UI elements based on checkbox selection
- **Feature toggles**: Activate/deactivate features when user toggles checkboxes
- **Data filtering**: Filter lists or apply logic based on which checkboxes are checked
- **State persistence**: Save checkbox states to local storage or backend

**Important behaviors**:
- **CustomEvent wrapper**: Remember that event.detail contains the boolean, not event itself
- **Not programmatic changes**: Event only fires for user interactions, not when you change the selected prop yourself
- **Doesn't fire for disabled**: Disabled checkboxes don't emit selectionChange when clicked
- **Doesn't fire for readOnly**: ReadOnly checkboxes show interaction but don't emit events

**Common patterns**:
```typescript
// Pattern 1: Update component state
onSelectionChange(event: CustomEvent<boolean>) {
  this.selected = event.detail;
  this.validateForm(); // Validate when state changes
}

// Pattern 2: Aggregate selection state from multiple checkboxes
onSelectionChange(event: CustomEvent<boolean>) {
  this.updateSelectedItemsCount();
  this.checkIfAllSelected();
}

// Pattern 3: Enable/disable dependent controls
onSelectionChange(event: CustomEvent<boolean>) {
  this.dependentCheckbox.disabled = event.detail;
}
```

**Accessibility considerations**:
- Event emissions are consistent with screen reader expectations users have for checkboxes
- Both click and space key interactions emit the same event for consistent behavior

### focusIn

A CustomEvent that fires when the checkbox receives keyboard focus or is focused programmatically. This event signals that the checkbox is now the active keyboard interactable element and can help track keyboard navigation patterns.

**Event payload type**: `CustomEvent<void>`

**When it fires**:
- **Tab key navigation**: When user tabs into the checkbox via keyboard
- **Shift+Tab navigation**: When user tabs backward into the checkbox
- **Programmatic focus**: When application code calls checkbox.focus() method
- **Click focus**: When user clicks the checkbox (it naturally receives focus)

**Payload content**:
- **event.detail**: `undefined` - void payload, this event signals focus state change without carrying data

**How to use - TypeScript handler**:
```typescript
onFocusIn() {
  console.log('Checkbox received focus');
  // Track which checkbox has focus for keyboard navigation analysis
  // Or show custom focus indicators beyond browser defaults
}
```

**Binding syntax**:
```html
<ion-checkbox (focusIn)="onFocusIn()"></ion-checkbox>
```

**When to use**:
- **Keyboard navigation tracking**: Monitor which checkboxes user navigates to for analytics or troubleshooting
- **Focus management**: Implement custom focus workflows or keyboard navigation patterns
- **Accessibility enhancements**: Add additional visual feedback beyond browser default focus indicators
- **Focus validation**: Trigger validation logic when user reaches specific checkboxes
- **UI assistance**: Show contextual help or guidance when certain checkboxes receive focus

**Focus events interactions**:
- **focusIn vs focusOut**: focusIn fires when checkbox receives focus, focusOut fires when it loses focus
- **Sequence**: focusIn → (user interaction) → focusOut for complete interaction tracking
- **Multiple elements**: As user tabs through multiple elements, each emits focusIn/focusOut events

**Important behaviors**:
- **Native focus behavior**: The checkbox receives standard browser focus visual indicators regardless of whether you handle this event
- **Screen reader compatibility**: Focus events work consistently with screen reader navigation patterns
- **Visual-indicator independence**: This event is separate from visual focus indicators - it fires regardless of any custom focus styling

**Common patterns**:
```typescript
// Pattern 1: Track focused checkbox for analytics
onFocusIn() {
  this.analytics.track('CheckboxFocused', { checkboxId: this.id });
}

// Pattern 2: Show contextual help
onFocusIn() {
  this.contextualHelpVisible = true;
  this.displayHelpForCheckbox(this.id);
}

// Pattern 3: Focus sequence tracking for keyboard navigation
onFocusIn() {
  this.trackKeyboardNavigation(this.id);
  this.recordFocusSequence();
}
```

**Accessibility importance**:
- Focus events are crucial for understanding keyboard navigation patterns
- Screen reader users navigate checkboxes via system focus management
- Proper focus handling is essential for WCAG keyboard accessibility compliance

### focusOut

A CustomEvent that fires when the checkbox loses keyboard focus (focus moves to a different element). This event signals that the checkbox is no longer the active keyboard interactable element and complements the focusIn event for complete focus tracking.

**Event payload type**: `CustomEvent<void>`

**When it fires**:
- **Tab key navigation**: When user tabs away from the checkbox to another element
- **Shift+Tab navigation**: When user tabs backward away from the checkbox
- **Click focus move**: When user clicks somewhere else in the interface
- **Programmatic focus**: When application code calls focus() on another element
- **Click outside focus**: When user clicks outside the checkbox area

**Payload content**:
- **event.detail**: `undefined` - void payload, this event signals focus state change without carrying data

**How to use - TypeScript handler**:
```typescript
onFocusOut() {
  console.log('Checkbox lost focus');
  // Validate when user leaves the checkbox
  // Hide contextual help or indicators
}
```

**Binding syntax**:
```html
<ion-checkbox (focusOut)="onFocusOut()"></ion-checkbox>
```

**When to use**:
- **Validation triggers**: Perform validation when user is "done" with the checkbox (tabbed away)
- **Contextual help management**: Hide help or guidance that was shown when checkbox had focus
- **State finalization**: Complete any in-progress logic related to user focus on this checkbox
- **Analytics**: Track interaction duration or completion when focus moves away
- **Focus management**: Implement custom focus-based workflows

**Focus navigation patterns**:
- **Element-to-element tracking**: Paired with focusIn, you can track complete navigation sequences
- **Direction awareness**: Not inherently directional, but can track movement patterns
- **Focus loss scenarios**: Different scenarios (tab to next, tab to previous, click away, programmatic) may be relevant for different logic

**Important behaviors**:
- **Focus loss during interaction**: Clicking the checkbox itself causes focus events (focusIn before click, potentially focusOut after if focus moves elsewhere)
- **Related to validation**: When validation occurs onBlur depends on validationMode configuration
- **Independence from selection**: focusOut fires regardless of whether selection changed during focus period

**Complete focus tracking example**:
```typescript
// Track focus duration for analytics
private focusStartTime: number;

onFocusIn() {
  this.focusStartTime = performance.now();
  console.log('Focus start time recorded');
}

onFocusOut() {
  const focusDuration = performance.now() - this.focusStartTime;
  this.analytics.track('CheckboxFocusDuration', {
    duration: focusDuration,
    checkboxId: this.id
  });
  console.log(`User spent ${focusDuration}ms on checkbox`);
}
```

**Common patterns**:
```typescript
// Pattern 1: Validate on blur
onFocusOut() {
  this.validateCheckbox();
  this.updateFormValidity();
}

// Pattern 2: Hide contextual elements
onFocusOut() {
  this.contextualHelpVisible = false;
  this.clearFocusIndicators();
}

// Pattern 3: Save user progress
onFocusOut() {
  this.saveProgress();
  this.recordInteraction();
}
```

**Accessibility relationship**:
- Screen reader navigation moves through checkboxes using focus changes
- FocusIn/focusOut sequence helps understand user interaction patterns
- Essential for keyboard accessibility compliance and understanding

## Complete event binding example

Below is a complete example showing all three events wired up together on one element, with a combined handler implementation that demonstrates how the events work together:

```html
<ion-checkbox
  [label]="checkboxLabel"
  [selected]="selected"
  [disabled]="disabled"
  (selectionChange)="onSelectionChange($event)"
  (focusIn)="onFocusIn()"
  (focusOut)="onFocusOut()"
></ion-checkbox>
```

**Combined handler implementation**:
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-example',
  template: `<!-- Template above -->`
})
export class ExampleComponent {
  checkboxLabel = 'Accept terms and conditions';
  selected = false;
  disabled = false;
  focusStartTime: number = 0;
  lastInteractionType: 'click' | 'keyboard' | 'programmatic' | null = null;

  onSelectionChange(event: CustomEvent<boolean>) {
    const newSelectionState = event.detail;
    this.lastInteractionType = 'keyboard'; // Could differentiate click vs keyboard
    console.log(`Selection changed to: ${newSelectionState}`);
    console.log(`Interaction type: ${this.lastInteractionType}`);

    // Validation logic can run selection change
    this.validateForm();
    this.synchronizeRelatedControls(newSelectionState);
  }

  onFocusIn() {
    this.focusStartTime = performance.now();
    console.log('Checkbox received focus, starting tracking');
    // Show contextual help when user navigates to checkbox
    this.showContextualHelp(this.checkboxLabel);
  }

  onFocusOut() {
    if (this.focusStartTime) {
      const focusDuration = performance.now() - this.focusStartTime;
      console.log(`Checkbox lost focus after ${focusDuration}ms`);
    }
    // Hide contextual help when user moves away
    this.hideContextualHelp();

    // Validate when user is "done" with checkbox
    this.validateOnBlur();
  }

  // Supporting methods
  showContextualHelp(label: string) {
    console.log(`Showing help for: ${label}`);
    // Implementation to display contextual help UI
  }

  hideContextualHelp() {
    console.log('Hiding contextual help');
    // Implementation to remove help UI
  }

  validateForm() {
    console.log('Validating form after selection change');
    // Form validation logic
  }

  validateOnBlur() {
    console.log('Validating on blur (focus out)');
    // Validation logic for blur scenario
  }

  synchronizeRelatedControls(isSelected: boolean) {
    console.log(`Synchronizing related controls based on selection: ${isSelected}`);
    // Logic to enable/disable related UI elements
  }
}
```

**Event sequence example**:
1. User tabs to checkbox → focusIn fires (focusStartTime recorded)
2. User presses space → selectionChange fires with detail=true
3. User tabs away → focusOut fires (focus duration calculated, help hidden)

This complete example demonstrates how the three events work together in typical checkbox interaction patterns, with focus tracking, selection handling, and validation logic integrated through the event system.

## Examples

```html
<ion-checkbox
  [selected]="false"
  [label]="'Default checkbox'"
></ion-checkbox>
```

**Demonstrates**: Basic checkbox with default unselected state and label text. Shows standard visual styling for an unselected normal checkbox. Used in "Default" story to show component baseline appearance.

```html
<ion-checkbox
  [selected]="true"
  [emphasized]="false"
  [label]="'Label'"
></ion-checkbox>
<ion-checkbox
  [selected]="true"
  [emphasized]="true"
  [label]="'Label'"
></ion-checkbox>
```

**Demonstrates**: Comparison of emphasized boolean values when selected is true. Shows visual difference between normal subtle styling and emphasized bold styling for selected checkboxes. Used in "Emphasized" story to demonstrate emphasis effect on selected state.

```html
<ion-checkbox
  [selected]="true"
  [size]="'sm'"
  [label]="'Label'"
></ion-checkbox>
<ion-checkbox
  [selected]="true"
  [size]="'md'"
  [label]="'Label'"
></ion-checkbox>
<ion-checkbox
  [selected]="true"
  [size]="'lg'"
  [label]="'Label'"
></ion-checkbox>
```

**Demonstrates**: All three size values (sm, md, lg) with selected=true and consistent labeling. Shows proportional scaling of checkbox dimensions, icon size, and spacing. Used in "Size" story to demonstrate responsive sizing options.

```html
<ion-checkbox
  [selected]="false"
></ion-checkbox>
<ion-checkbox
  [selected]="false"
  [label]="'Label'"
></ion-checkbox>
```

**Demonstrates**: Label presence/absence with selected=false state. Shows checkbox visual without label (standalone) versus with label text. Used in "Label" story to show label placement and appearance.

```html
<ion-checkbox
  [selected]="false"
  [label]="'Label'"
></ion-checkbox>
<ion-checkbox
  [selected]="true"
  [label]="'Label'"
></ion-checkbox>
```

**Demonstrates**: Selected boolean values (false and true) with label text present. Shows visual difference between unselected (empty) and selected (checked with fill) states. Used in "Selected" story to show primary state indication.

```html
<ion-checkbox
  [indeterminate]="false"
  [label]="'Label'"
></ion-checkbox>
<ion-checkbox
  [indeterminate]="true"
  [label]="'Label'"
></ion-checkbox>
```

**Demonstrates**: Indeterminate boolean values (false and true) without selection context. Shows visual difference between normal and indeterminate states. Used in "Indeterminate" story to demonstrate the indeterminate/minus appearance.

```html
<ion-checkbox
  [selected]="false"
  [readOnly]="false"
  [label]="'Label'"
></ion-checkbox>
<ion-checkbox
  [selected]="false"
  [readOnly]="true"
  [label]="'Label'"
></ion-checkbox>
```

**Demonstrates**: ReadOnly boolean values with selected=false. Shows interaction difference between editable and read-only checkboxes with same visual appearance. Used in "ReadOnly" story to show behavioral difference while appearance remains similar.

```html
<ion-checkbox
  [selected]="true"
  [readOnly]="false"
  [label]="'Label'"
></ion-checkbox>
<ion-checkbox
  [selected]="true"
  [readOnly]="true"
  [label]="'Label'"
></ion-checkbox>
```

**Demonstrates**: ReadOnly boolean values with selected=true for selected state context. Shows that readOnly checkboxes maintain selected appearance but prevent interaction changes. Complements previous readOnly example with different selection state.

```html
<ion-checkbox
  [selected]="false"
  [disabled]="false"
  [label]="'Checkbox'"
></ion-checkbox>
<ion-checkbox
  [selected]="false"
  [disabled]="true"
  [label]="'Checkbox'"
></ion-checkbox>
```

**Demonstrates**: Disabled boolean values with selected=false. Shows visual difference between interactive and disabled (grayed) unselected checkboxes. Used in "Disabled" story to demonstrate complete disabling effect.

```html
<ion-checkbox
  [selected]="true"
  [disabled]="false"
  [label]="'Checkbox'"
></ion-checkbox>
<ion-checkbox
  [selected]="true"
  [disabled]="true"
  [label]="'Checkbox'"
></ion-checkbox>
```

**Demonstrates**: Disabled boolean values with selected=true for selected disabled state. Shows that disabled maintains the selected visual appearance but with reduced opacity and prevents all interaction. Complements previous disabled example with different selection state.

```html
<ion-checkbox
  [selected]="false"
  [autoFocus]="false"
  [label]="'Label'"
></ion-checkbox>
<ion-checkbox
  [selected]="false"
  [autoFocus]="true"
  [label]="'Label'"
></ion-checkbox>
```

**Demonstrates**: AutoFocus boolean values with consistent selected=false state. Shows behavioral difference (focus behavior) between autofocused and non-autofocused checkboxes. Used in "AutoFocus" story to demonstrate programmatic focus capability.

```html
<ion-checkbox
  [selected]="false"
  [label]="'Label'"
></ion-checkbox>
<ion-checkbox
  [selected]="false"
  [ariaLabel]="'Custom aria label. If not provided, label will be used as aria-label'"
  [label]="'Label'"
></ion-checkbox>
```

**Demonstrates**: AriaLabel presence/absence with selected=false and visual label present. Shows that ariaLabel provides additional accessibility information beyond the visual label. Used in "AriaLabel" story to demonstrate accessibility customization.

```html
<ion-checkbox
  [autofocus]="autofocus"
  [label]="label"
  [disabled]="disabled"
  [readOnly]="readOnly"
  [emphasized]="emphasized"
  [selected]="selected"
  [size]="size"
  [ariaLabel]="ariaLabel"
  [indeterminate]="indeterminate"
  [required]="required"
  (selectionChange)="onSelectionChange($event)"
></ion-checkbox>
```

**Demonstrates**: Comprehensive example with all major props and selectionChange event binding. Shows combination of visual props (size, emphasized, disabled, readOnly), state props (selected, indeterminate), content props (label, ariaLabel, required), behavioral prop (autofocus), and event binding. Used in "Playground" story to demonstrate complete component API.