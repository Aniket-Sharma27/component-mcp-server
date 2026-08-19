---
realComponent: "ion-checkbox-group"
description: "A container component that groups multiple ion-checkbox elements together, managing shared state, validation, and layout for multi-select interfaces"
themes:
  - light
  - dark
apiTypes:
  - element
relatedComponents:
  - name: "ion-checkbox"
    relationship: "child"
    whenToUse: "Use ion-checkbox-group instead of multiple standalone checkbox elements when rendering 2+ checkboxes together - it manages shared name/selection state, keyboard navigation, validation across the group, and provides coordinated layout. Individual ion-checkbox elements must be rendered as direct children of ion-checkbox-group to benefit from group-level coordination."
props:
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
          tokenChain: "ion-comp-checkbox-container-color-bg-enabled-bold"
          appliesToCssProperty: "border-color, background-color"
        dark:
          resolvesTo: "#008af7"
          tokenChain: "ion-comp-checkbox-container-color-bg-enabled-bold"
          appliesToCssProperty: "border-color, background-color"
      false:
        light:
          resolvesTo: "#030f26"
          tokenChain: "ion-cont-color-role-light-neutral-900"
          appliesToCssProperty: "border-color"
        dark:
          resolvesTo: "#007de0"
          tokenChain: "ion-lit-color-palette-dark-blue-500"
          appliesToCssProperty: "border-color"
  - name: "label"
    type: "string"
    category: "content"
    required: false
    default: "\"\""
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
    designTokens:
      vertical:
        resolvesTo: "column"
        tokenChain: "flex-direction"
        appliesToCssProperty: "flex-direction"
      horizontal:
        resolvesTo: "row"
        tokenChain: "flex-direction"
        appliesToCssProperty: "flex-direction"
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
  - name: "contentOrientation"
    type: "ContentOrientation"
    category: "visual"
    required: false
    default: "vertical"
    values:
      - vertical
      - horizontal
    designTokens:
      vertical:
        resolvesTo: "column"
        tokenChain: "flex-direction"
        appliesToCssProperty: "flex-direction"
      horizontal:
        resolvesTo: "row"
        tokenChain: "flex-direction"
        appliesToCssProperty: "flex-direction"
  - name: "name"
    type: "string"
    category: "content"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "defaultValue"
    type: "any[]"
    category: "behavioral"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "value"
    type: "any[]"
    category: "behavioral"
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
  - name: "maxSelection"
    type: "number"
    category: "behavioral"
    required: false
    default: "none found"
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
      valid:
        light:
          resolvesTo: "#2dc168"
          tokenChain: "ion-lit-color-leonardo-base-positive"
          appliesToCssProperty: "color"
      invalid:
        light:
          resolvesTo: "#c70000"
          tokenChain: "ion-lit-color-leonardo-base-negative"
          appliesToCssProperty: "color"
      warning:
        light:
          resolvesTo: "#fe7f2a"
          tokenChain: "ion-lit-color-leonardo-base-warning"
          appliesToCssProperty: "color"
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
  - name: "ariaLabel"
    type: "string"
    category: "accessibility"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "description"
    type: "string"
    category: "content"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "orientation"
    type: "LabelPlacement"
    category: "visual"
    required: false
    default: "none found"
    values:
      - vertical
      - horizontal
    designTokens: {}
events:
  - name: "selectionChange"
    payloadType: "CustomEvent<ICheckboxGroupValueChangeEventArgs>"
    firesWhen: "DEPRECATED - fires when checkbox selection state changes - on user click (if not disabled/readOnly) or when value prop changes. Use valueChange event instead."
    detailAccess: "event.detail (object) - contains { name: string, value: any[] } where value is array of selected checkbox values"
    bindingSyntax: '(selectionChange)="onSelectionChange($event)"'
  - name: "valueChange"
    payloadType: "CustomEvent<ICheckboxGroupValueChangeEventArgs>"
    firesWhen: "Fires when checkbox selection state changes - on user click (if not disabled/readOnly) or when value prop changes"
    detailAccess: "event.detail (object) - contains { name: string, value: any[] } where value is array of selected checkbox values"
    bindingSyntax: '(valueChange)="onValueChange($event)"'
jointTokens: []
propInteractions:
  - "disabled state propagates to all child checkboxes - when disabled=true, all checkboxes within the group become disabled via disabledInternal prop, preventing any user interaction with individual checkboxes."
  - "readOnly state propagates to all child checkboxes - when readOnly=true, all checkboxes maintain their visual state but cannot be toggled by user interaction, providing a display-only view of the selection."
  - "size prop propagates to all child checkboxes - when size is set on the group, it automatically applies to all checkboxes, ensuring consistent sizing across the group."
  - "emphasized prop propagates to all child checkboxes - when emphasized=true, all checkboxes use bold styling for more visual prominence throughout the group."
  - "name prop propagates to all child checkboxes - when name is set on the group, it applies to all child checkboxes, sharing the same form submission name."
  - "value prop controls checkbox selection state - when value array is updated, it automatically selects/deselects checkboxes based on whether their value is included in the array. Children checkboxes must have matching value props for this coordination to work."
  - defaultValue prop provides initial uncontrolled state - when defaultValue is set and value is undefined, checkboxes are initially selected based on defaultValue array. This establishes the initial selection state without requiring controlled binding."
  - "maxSelection enforces limit on selections - when specified, automatically disables unselected checkboxes once the max number of checkboxes are selected. Users must deselect before selecting additional options."
  - "required prop enables group-level validation - when required=true and validationMode is active, the group validates that at least one checkbox is selected and sets validationState to invalid if no checkboxes are checked."
  - "validationMode + validationState + validationMode work together - validationMode determines when validation runs (onChange, onBlur, onSubmit), validationState provides the current validation result (valid, invalid, warning, none), and validationMode triggers validation. The group runs validation when conditions match validationMode."
  - "helperMessage and validationState interact - when validationState changes to invalid/warning, the helperMessage may be replaced with validation message text. In normal states, helperMessage displays helpful guidance text."
  - "labelPlacement determines label vs content layout - labelPlacement controls whether the group label appears above (vertical) or beside (horizontal) the checkbox content area. When horizontal, labelAlignment and labelWidth become applicable."
  - "contentOrientation determines checkbox layout - contentOrientation controls whether individual checkboxes are stacked vertically or arranged horizontally within the content area. This affects the overall structure and space utilization."
  - "necessityIndicator adds visual requirement indicator - when combined with required=true, displays an asterisk (requiredMarker) or text label (requiredLabel/optionalLabel) to visually communicate requirement status."
  - "description prop is deprecated - use helperMessage instead. Both props serve similar purposes but description is the older API."
  - "orientation prop is deprecated - use labelPlacement instead. They control the same layout aspects but labelPlacement is the modern API."
  - "Indeterminate checkbox usage pattern - when using indeterminate checkbox as parent for child checkboxes, the parent checkbox should NOT be part of the checkbox-group. Instead, create a separate indeterminate checkbox and a separate checkbox-group for the children. The parent checkbox manages its own indeterminate state while the group manages the child selections."
needsReview:
  - "Checkbox group container padding tokens for different size variants (sm/md/lg) could not be traced. The CSS references tokens like --ion-comp-checkbox-group-container-spacing-padding-block-start-vertical-sm but the specific resolved values for light and dark themes could not be determined from the available source material."
  - "Checkbox group container gap/spacing tokens for different orientations (vertical/horizontal) and sizes could not be traced. Tokens mentioned include --ion-comp-checkbox-group-container-spacing-column-gap-vertical-md and row-gap equivalents, but specific spacing values could not be resolved."
  - "Validation state color tokens (valid, invalid, warning) for checkbox groups were found with single theme values but dark theme equivalents could not be traced. Light theme uses base leonardo tokens but whether dark theme uses the same tokens or different palette tokens could not be confirmed."
  - "Border-radius tokens for checkbox container were referenced in CSS but final resolved values could not be traced. Values likely depend on size prop but specific mapping could not be determined from available token definitions."
  - "Hover and active state design tokens for checkbox container background and border colors are defined in checkbox-ds.css but the specific hex values for light and dark themes could not be traced from the available token definitions."
  - "Checkmark icon color tokens (foreground color) for different states (enabled, selected, disabled, readOnly, validation states) were referenced but specific hex values for light and dark themes could not be fully traced. Background colors were traced more completely."
  - "The selectionChange event is marked as deprecated in the code with a comment to remove it in version 164, but the exact deprecation timeline and migration guidance could not be confirmed from the available documentation."
  - "ariaLabel vs label priority for accessibility - the code constructs ariaLabelMessage combining multiple sources but the exact priority order (ariaLabel first, then label, then other attributes) was not explicitly documented in the available source material."
  - "Mobile interaction behavior differences (isMobileMode affects checkbox behavior) need runtime verification for checkbox-group specifically, as the checkbox component has mobile-specific logic but group-level mobile behavior could not be fully traced."
---

## Usage Notes

Boolean props on this component must always be passed with an explicit string value — e.g. `disabled="true"` or `[disabled]="isDisabled"` — never as bare attribute presence (e.g. `disabled` alone, with no value). Bare attribute presence is a native HTML convention this component does NOT support; it will not be interpreted as true.

## Related Components

The `ion-checkbox-group` component is designed to work with `ion-checkbox` child elements. When you need to present multiple checkboxes together, use `ion-checkbox-group` instead of rendering individual `ion-checkbox` elements. The group provides:

- **Shared state management**: Coordinates selection state across all child checkboxes
- **Unified styling**: Applies size, emphasized, disabled, and other visual props to all checkboxes automatically  
- **Form coordination**: Uses a shared `name` for all checkboxes in the group for form submission
- **Validation**: Group-level validation with `required`, `validationState`, and `validationMode` props
- **Layout control**: Manages both label placement (`labelPlacement`) and checkbox arrangement (`contentOrientation`)

Individual `ion-checkbox` elements must be direct children of `ion-checkbox-group` and should have matching `value` props that correspond to items in the group's `value` array for proper coordination.

## size

Controls the height, width, and overall scale of all checkboxes within the group. Size values (sm, md, lg) map to design system spacing tokens that scale every checkbox proportionally. This is a visual prop that directly impacts the user's perception of the component's scale and prominence in the interface.

The size prop determines multiple visual properties simultaneously through design system tokens:
- **Container dimensions**: Overall width and height of each checkbox square
- **Icon scaling**: Size of the checkmark icon (using font tokens)
- **Internal padding**: Space between checkbox border and checkmark icon
- **Label spacing**: Gap between checkbox and label text in individual checkboxes

**Size values and their visual effects**:

- **sm**: Small checkboxes with 16px container (computed). The checkmark icon is smaller, internal padding is tighter, and overall appearance is more compact. This is useful for dense interfaces with many checkboxes where vertical space is at a premium.

- **md (default)**: Medium checkboxes with 20px container (computed). Standard checkmark icon size, regular padding, balanced proportions. This is the most commonly used size and appropriate for most form interfaces.

- **lg**: Large checkboxes with 24px container (computed). Larger checkmark icon, generous padding, more prominent appearance. Useful for interfaces with larger touch targets or when checkboxes need special emphasis for accessibility or mobile-first design.

**Important interactive benefits**:
- **Touch targets**: Larger sizes (lg) provide bigger touch targets for mobile users
- **Accessibility**: Smaller sizes may be harder to click for users with motor disabilities  
- **Visual hierarchy**: Size creates effective hierarchy when different checkbox groups have different sizes

**MQ string support**: The size prop can accept Media Query (MQ) responsive strings that allow different sizes at different breakpoints. For example, you could specify "xs=lg;sm=md;md=md;lg=md" to get larger checkboxes on extra-small screens for better touch targets, while maintaining medium size on larger screens.

**Group-level coordination**: When you set size on the checkbox-group, it automatically propagates to all child checkboxes, ensuring all checkboxes in the group are consistently sized. This eliminates the need to set size on each individual checkbox.

## emphasized

Controls the visual prominence of all checkboxes within the group by using stronger colors and more prominent styling. When true, all checkboxes in the group display with bold styling that makes them more visually prominent in the interface. This is a visual prop that affects the checkboxes' appearance without changing their behavior.

**Emphasized state visual effects**:

- **Emphasized=false (subtle/default)**: Unselected checkboxes have neutral border colors, selected checkboxes have more subtle background colors. This is the restrained, default appearance that blends with the interface without drawing excessive attention.

- **Emphasized=true (bold)**: Unselected checkboxes have prominent border colors (using primary branding colors), selected checkboxes have strong background colors and visual emphasis. This creates a more visually prominent, attention-grabbing appearance for all checkboxes in the group.

**Important visual cues**:
- **Border color**: When emphasized=true, unselected checkboxes use brand colors for borders instead of neutral colors
- **Background color**: When emphasized=true and selected, checkboxes use bold primary colors for backgrounds versus more subtle colors
- **Checkmark color**: Selected emphasized checkboxes use more prominent colors for checkmarks

**Use cases for emphasized state**:
- **Primary actions**: Use emphasized for checkboxes that represent primary options or frequently used features
- **Feature highlights**: Draw attention to important checkbox groups that represent key choices
- **Branded interfaces**: Use emphasized styling to align with brand colors and create strong visual identity
- **Dashboard widgets**: Make checkboxes in prominent positions more visually distinct

**Interaction with other states**: The emphasized prop affects the color intensity of all checkbox states (enabled, hover, active, selected, disabled, readOnly) for all checkboxes in the group, but does not change the fundamental behavior of those states. An emphasized disabled checkbox still appears disabled but with more prominent colors than a non-emphasized disabled checkbox.

**Group-level coordination**: When you set emphasized on the checkbox-group, it automatically propagates to all child checkboxes, ensuring all checkboxes in the group have consistent emphasis styling. This creates visual cohesion across the entire group.

**Theme considerations**: The actual hex values for emphasized states differ between light and dark themes, with each theme using appropriate color palette tokens to ensure contrast and visual harmony.

## label

Provides the text content displayed as the identifier for the checkbox group, typically positioned above or beside the checkbox content area based on the labelPlacement prop. Labels provide context and help users understand what the checkbox group represents. This is a content prop that does not affect the component's behavior or visual appearance beyond the text content itself.

The label prop accepts plain text strings. When a label is provided, it appears as descriptive text associated with the group of checkboxes. The precise positioning of the label relative to the checkbox content is controlled by the labelPlacement prop (vertical/horizontal).

**Important accessibility relationship**: When ariaLabel is not provided, the checkbox group uses the label text as part of its accessible name for screen reader accessibility. For checkbox groups that immediately follow descriptive content (headings, paragraphs), the label may be optional provided sufficient context exists.

**Label positioning and layout**: The label position is controlled by labelPlacement:
- **labelPlacement="vertical"**: Label appears above the checkbox content area (default)
- **labelPlacement="horizontal"**: Label appears beside the checkbox content area

When labelPlacement="horizontal", the labelWidth and labelAlignment props become applicable to control the horizontal spacing and alignment of the label.

When no label is provided, the checkbox group appears without a descriptive label. This may be appropriate when the group's purpose is immediately obvious from context (e.g., immediately following a section heading).

This prop is self-contained for content, though its visual presentation (font size, color, spacing) is controlled by the component's design system tokens and the labelPlacement layout configuration.

## labelPlacement

Controls the layout of the group label relative to the checkbox content area. This visual prop determines whether the label appears above or beside the checkboxes, affecting the overall structure and space utilization of the component.

**Layout behaviors**:

- **labelPlacement="vertical" (default)**: The label appears above the checkbox content area. Checkboxes are stacked or aligned vertically underneath the label. This is the most common layout and provides clear visual hierarchy with label as section header.

- **labelPlacement="horizontal"**: The label appears beside the checkbox content area. Checkboxes are arranged in a row alongside the label. This layout is more compact and useful for wide interfaces where horizontal space is available.

**Interaction with other props**:

- **labelAlignment**: Only applicable when labelPlacement="horizontal". Controls whether the label is aligned to the start (left) or end (right) of the horizontal layout.

- **labelWidth**: Only applicable when labelPlacement="horizontal". Specifies the width of the label area in pixels or other CSS units, providing precise control over the horizontal space allocated to the label.

- **contentOrientation**: Independent of labelPlacement. Controls whether the individual checkboxes within the content area are stacked vertically or arranged horizontally.

**Use cases**:
- **Vertical label**: Most common, works well for forms, stacked layouts, mobile interfaces, and when labels are longer
- **Horizontal label**: Compact alternative for wide interfaces, dashboard widgets, comparison tables, or when fitting multiple groups side-by-side

**Accessibility**: Regardless of labelPlacement, the semantic relationship between the label and checkbox group is properly established for screen readers. The prop only affects visual presentation, not accessibility structure.

**Visual considerations**: Vertical label placement creates stronger visual hierarchy and is often easier to scan. Horizontal placement creates more compact layouts but may be less readable if labels are long or checkboxes are numerous.

## labelAlignment

Controls the horizontal alignment of the label relative to the checkbox content area when labelPlacement="horizontal". This visual prop only applies to horizontal label layouts and determines whether the label appears at the start (left) or end (right) of the row.

**Alignment behaviors**:

- **labelAlignment="start" (default when horizontal)**: The label appears at the left side of the horizontal layout, with checkboxes to its right. This follows left-to-right reading patterns and is the most common alignment for Western languages.

- **labelAlignment="end"**: The label appears at the right side of the horizontal layout, with checkboxes to its left. This can be useful for right-to-left languages or specific design patterns where the label should follow the checkboxes.

**Use cases**:
- **labelAlignment="start"**: Standard left-to-right reading order, most common for English and other Western languages
- **labelAlignment="end"**: Right-to-left languages, specialized design patterns, cultural conventions, or when checkboxes should come before labels

**Visual hierarchy**: Label direction affects the reading flow and visual hierarchy. Start alignment (labels before checkboxes) tends to establish context before presenting options. End alignment (labels after checkboxes) may be used when the checkboxes themselves are the primary focus.

**Layout impact**: When labelAlignment="start", you might want to set a specific labelWidth to ensure consistent spacing. When labelAlignment="end", the labelWidth still applies but the label appears at the right edge of the layout.

**Accessibility**: The order of elements in the DOM (label before checkboxes for start alignment, or checkboxes before label for end alignment) can affect screen reader announcements and keyboard navigation order. Consider accessibility implications when choosing alignment for RTL languages or custom layouts.

## labelWidth

Specifies the width of the label area in CSS units (pixels, percentage, em, etc.) when labelPlacement="horizontal". This visual prop provides precise control over how much horizontal space is allocated to the label before the checkbox content area begins.

**Width behaviors**:

- **When specified**: The label area takes exactly the specified width, with the checkbox content area filling the remaining horizontal space. This ensures consistent alignment across multiple checkbox groups.

- **When not specified**: The label area takes only as much space as needed for the label text content, with the checkbox content area beginning immediately after the label ends.

**CSS unit options**:
- **Pixels**: `labelWidth="150px"` for fixed pixel width
- **Percentage**: `labelWidth="25%"` for percentage-based width
- **EM units**: `labelWidth="15em"` for relative text-based sizing
- **Other units**: Any valid CSS length unit can be used

**Use cases**:
- **Consistent alignment**: Set equal label widths across multiple groups to vertically align checkbox content
- **Fixed layouts**: Use pixel widths for precise design control
- **Responsive layouts**: Use percentage widths for flexible layouts that adapt to container width
- **Text-based scaling**: Use em units to scale label width with text size

**Layout interaction**: labelWidth only applies when labelPlacement="horizontal". For vertical label placement, this prop has no effect.

**Accessibility considerations**: Avoid using label widths that are too narrow for the label text, as this could cause text overflow and reduce readability. Ensure adequate space for proper text rendering.

**Visual harmony**: When using multiple checkbox groups with horizontal labels, consistent labelWidth values create visual alignment and make the interface easier to scan.

## required

When true, indicates that at least one checkbox within the group must be selected before the form can be considered complete. This is a semantic/content prop that enables validation behavior and may trigger visual requirement indicators.

**Validation behavior**:
- **Validation modes**: The required prop works in conjunction with validationMode to determine when validation occurs (onChange, onBlur, onSubmit)
- **Validation result**: When validation runs and no checkboxes are selected, validationState is set to "invalid" and helperMessage may display an error message
- **Form validation**: Form-level validation systems can check the group's value array to ensure it's not empty when required is true

**Accessibility impact**: The required prop adds aria-required="true" to the checkbox group's accessible name. This helps screen reader users identify which checkbox groups have mandatory selections. Combined with necessityIndicator, it provides comprehensive requirement communication.

**Visual indicators**: The required prop itself does not add visual indicators. Use necessityIndicator prop to display asterisks (requiredMarker), text labels (requiredLabel), or explicit "optional" labels (optionalLabel) as visual requirement indicators.

**Validation integration**:
- **validationMode="none"**: No automatic validation, required is only a semantic marker
- **validationMode="onChange"**: Validation runs immediately when checkboxes are selected/deselected
- **validationMode="onBlur"**: Validation runs when the checkbox group loses focus
- **validationMode="onSubmit"**: Validation runs on form submission (triggered by your application code)

**Use cases**:
- **Mandatory selections**: Require at least one checkbox selection (e.g., "Select at least one interest")
- **Form compliance**: Mark required sections to ensure users don't skip important choices
- **Accessibility**: Assistive technologies announce requirement status
- **Business rules**: Enforce minimum selection requirements for data completeness

**Validation message**: When required validation fails, the component's helperMessage may be replaced with a system validation message from the Strings.DESIGN_SYSTEM_VALIDATION_MULTI_SELECT_REQUIRED constant, but custom validation messages can also be set programmatically.

**No individual checkbox enforcement**: The required prop applies to the group as a whole, not individual checkboxes. It requires at least one checkbox to be selected, not a specific checkbox or minimum number of selections. Use maxSelection for limiting selections.

## necessityIndicator

Controls the type of visual indicator that communicates requirement status when combined with the required prop. This visual prop adds UI elements that help users quickly understand whether checkbox group selection is mandatory or optional.

**Indicator types and their visual effects**:

- **requiredMarker (default)**: Displays an asterisk (*) next to the label. This is the most compact visual indicator commonly used in forms. The asterisk typically appears immediately after the label text.

- **requiredLabel**: Displays "Required" text next to the label. This provides more explicit text-based communication of requirement status. The text appears in the same font size as the label.

- **optionalLabel**: Displays "Optional" text next to the label. This explicitly communicates when a checkbox group is NOT required, helping reduce user uncertainty. Useful for long forms with mix of required and optional sections.

- **none**: No visual requirement indicator is displayed. The requirement status is only communicated semantically via aria-required attribute for screen readers.

**Interaction with required prop**:
- **required=true**: Shows the specified indicator (requiredMarker or requiredLabel) to communicate that selection is mandatory
- **required=false**: Shows optionalLabel indicator if specified, otherwise shows nothing (none behavior)

**Visual placement**: The necessity indicator typically appears next to the label in the same font size but with slightly reduced emphasis. It's positioned after the label text to avoid interfering with label scanning.

**Use cases**:
- **requiredMarker**: Compact forms, mobile interfaces, when space is limited, industry standard for required fields
- **requiredLabel**: Enterprise applications, explicit communication needs, forms with mixed requirement complexity
- **optionalLabel**: Long forms, reduce user uncertainty, avoid assumption that fields are required by default
- **none**: Forms with consistent requirement status, reliance on other visual cues, international contexts where symbols may cause confusion

**Accessibility**: Regardless of the necessityIndicator setting, the semantic requirement status is always communicated via aria-required attribute for screen readers. The visual indicator is primarily for sighted users.

**Design system consistency**: Use consistent necessityIndicator values across a form or application to establish predictable patterns. For example, always use requiredMarker for all required fields or always use requiredLabel for explicit communication.

## contentOrientation

Controls the layout arrangement of individual checkboxes within the content area. This visual prop determines whether the checkboxes are stacked vertically or arranged horizontally, affecting the overall structure and space utilization of the checkbox group.

**Layout behaviors**:

- **contentOrientation="vertical" (default)**: Checkboxes are stacked vertically, one above another. Each checkbox occupies a full row, with labels text flowing left to right. This is the most common layout and provides clear visual hierarchy and scannability for lists of options.

- **contentOrientation="horizontal"**: Checkboxes are arranged horizontally in a row, with each checkbox appearing beside the previous one. This layout is more compact and useful for wide interfaces where horizontal space is available and you want to display multiple options in a condensed format.

**Interaction with other props**:

- **labelPlacement**: Independent of contentOrientation. Controls where the group label appears relative to the entire checkbox content area, not how individual checkboxes are arranged within that area.

- **Checkbox wrapping**: When contentOrientation="horizontal" and the checkboxes extend beyond the container width, wrapping behavior depends on the available space and CSS settings. Consider horizontal layout for small groups in wide containers to avoid awkward wrapping.

**Use cases**:
- **Vertical layout**: Most common, works well for forms, mobile interfaces, longer checkbox labels, when vertical space is available, and for clear option scanning
- **Horizontal layout**: Compact alternative for wide interfaces, dashboard widgets, short checkbox labels, when fitting many options in limited vertical space, and for configuration panels

**Accessibility**: Regardless of contentOrientation, checkbox elements maintain proper keyboard navigation order (tabbing) and screen reader announcements. The prop only affects visual presentation.

**Visual considerations**: 

- **Vertical**: Easier to scan, works well with long labels, natural reading order for lists, better for mobile where vertical scrolling is standard
- **Horizontal**: More compact, better for limited vertical space, can be harder to scan with many options, may require horizontal scrolling or wrapping

**Responsive design**: Consider using contentOrientation="vertical" on mobile devices (where vertical space is more abundant than horizontal space) and horizontal on desktop large screens to optimize space usage. This can be combined with MQ string support for responsive sizing.

## name

Provides a shared name for all checkboxes within the group, which is primarily used when the checkboxes are part of an HTML form. The name attribute becomes part of the form data when the form is submitted, identifying which checkbox group the submitted values belong to. This is a content prop that affects form data structure but does not change the checkboxes' visual appearance or behavior.

The name prop accepts string values that identify the checkbox group in form submissions. When set, this name is automatically applied to all individual ion-checkbox elements within the group, creating a shared form submission name.

**Form submission behavior**: 
- When checkboxes within the group are checked and have a shared name, the form submission includes multiple name=value pairs (e.g., name="interests" with values=["sports","music"] results in interests=sports and interests=music)
- The group collects selected checkbox values into an array for the value prop, which can be used for programmatic form handling
- Each individual checkbox still maintains its own value prop to distinguish which specific option was selected

**Use cases**:
- **Form submissions**: Use name to identify checkbox group data when submitting forms
- **Data aggregation**: Group related checkboxes under a single form field name
- **Backend integration**: Name often maps to database field names or API parameters
- **Form organization**: Structure form data by grouping related checkboxes

**Accessibility**: The name attribute does not directly affect screen reader accessibility outside of form submission context. Use label and ariaLabel for accessible names and descriptions.

**Group-level coordination**: When you set name on the checkbox-group, it automatically propagates to all child ion-checkbox elements. This ensures all checkboxes share the same form submission name without requiring individual checkbox configuration.

**Validation compatibility**: The name prop works seamlessly with validation props (required, validationState, validationMode) and value management, providing both form submission semantics and validation coordination.

## defaultValue

Provides the initial selection state for checkboxes within the group when not using controlled value binding. This is a behavioral prop that establishes the default checked state without requiring continuous value tracking or two-way binding.

**Behavior patterns**:

- ** defaultValue + value = undefined**: Checkboxes are selected based on values in the defaultValue array. The group tracks user selections and emits valueChange events, but you don't have full programmatic control over selection state.

- **defaultValue + value = [] (empty array)**: The empty array clears all checkbox selections, establishing no initial selections as the default state. Same effect as having no defaultValue or defaultValue set to undefined.

- **defaultValue with value=<array>**: The value prop takes precedence and controls selection state, making defaultValue irrelevant. The controlled value overrides the default.

**Value array structure**: The defaultValue should be an array containing the value props of checkboxes that should initially be selected. Each ion-checkbox element must have a matching value prop for this coordination to work.

**Uncontrolled vs controlled components**:
- **Uncontrolled**: Use defaultValue when you want the group to manage its own selection state internally, and you only need to know about changes via valueChange events
- **Controlled**: Use the value prop when you need full programmatic control over which checkboxes are selected, often driven by application state

**Use cases**:
- **Form initialization**: Set initial selections based on user preferences or default configurations
- **Survey defaults**: Pre-select commonly chosen options to improve user experience
- **Feature toggles**: Set default enabled/disabled states for optional features
- **Simple state tracking**: Avoid complex state management when you only need to capture user selections

**Interaction with valueChange**: Even when using defaultValue, the group still emits valueChange events when users select/deselect checkboxes. You can track these changes without having to continuously update the value prop.

**Form submission**: When using defaultValue (uncontrolled), you can still access the current selections via the group's value property (reading it rather than setting it) for form submission or validation.

## value

Controls which checkboxes are selected within the group. When provided as an array of values, it sets the selection state of all checkboxes - checkboxes whose value appear in the array become selected, others become unselected. This is a controlled behavioral prop that provides full programmatic control over checkbox selection state.

**Controlled vs uncontrolled patterns**:

- **Controlled component**: When you bind to value, you have full control over selection state. You must update the value array (or use valueChange to update your state) when user interactions occur, otherwise the checkboxes won't update their selection state.

- **Uncontrolled component**: When value is undefined or not provided, use defaultValue instead. The group manages its own selection state internally, emitting valueChange events to inform you of changes but not requiring continuous value updates.

**Value array structure**: The value should be an array containing the value props of ion-checkbox elements that should be selected. Each ion-checkbox element must have a matching value prop for this coordination to work.

**ValueChange event propagation**: The group emits valueChange events whenever checkbox selections change. The event payload includes the updated value array, allowing you to keep your application state synchronized with checkbox selection state.

**Use cases**:
- **Form state management**: Track which checkboxes are selected for form submission or validation
- **Dependent controls**: Enable/disable other UI elements based on checkbox selection patterns
- **Data filtering**: Apply logic based on which items are selected
- **State persistence**: Save checkbox selections to local storage or backend
- **React to external state**: Programmatically update selections based on API data or other application state

**Interaction with other props**:
- **required**: The value array is used to validate whether at least one checkbox is selected when required=true
- **maxSelection**: The value array length is checked against maxSelection to prevent exceeding selection limits
- **defaultValue**: When value is set, defaultValue is ignored; value takes precedence

**Form submission**: The value array represents the current selection state and can be directly used in form submission data. When the checkbox group has a name prop, the value array provides the form submission values.

**Empty array behavior**: An empty array (`[]`) means no checkboxes are selected. This is different from `undefined` or not providing the value prop (which triggers uncontrolled behavior with defaultValue if provided, or no selections by default).

**Validation integration**: The value array is validated against business rules (required, maxSelection) to set validationState and trigger validation messages in helperMessage when validation failures occur.

## helperMessage

Provides a brief explanatory message or guidance text that appears below the checkbox group label or near the checkbox content area. This message offers contextual help, instructions, or validation feedback to users. This is a content prop that affects user guidance and validation communication.

**Message types and contexts**:

- **Helpful guidance**: Provides instructions or tips about how to use the checkbox group, what selections are recommended, or any relevant information that aids users in making selections.

- **Validation feedback**: When validationState is set to invalid/warning/valid, the helperMessage may display validation-specific messages like "At least one option must be selected" for required groups or other custom validation messages.

- **Error recovery**: Provides guidance about how to fix validation errors or recover from invalid states.

**Message priority**: 
- **Validation state messages**: When validationState changes from the default "none" state, system validation messages may replace the original helperMessage to communicate urgent validation feedback
- **Programmatic overrides**: You can programmatically update helperMessage to provide specific messages or clear validation messages

**Use cases**:
- **Usage instructions**: "Select all options that apply to your situation"
- **Helpful tips**: "Choose your top 3 preferences" (when combined with maxSelection=3)
- **Validation guidance**: "At least one checkbox must be selected" (for required groups)
- **Error recovery**: "Please select at least two options to continue"

**Visual presentation**: The helperMessage appears in a standard font size and color appropriate to the current validation state:
- **Normal state**: Neutral text color for helpful guidance
- **Invalid state**: Error-colored text for validation failures
- **Warning state**: Warning-colored text for warning conditions
- **Valid state**: Success-colored text for positive confirmation

**Accessibility**: Helper message text should be clear, concise, and immediately actionable. Avoid technical jargon. The message should be scoped to the checkbox group, not broader form context.

**Interaction with validationState**: When validation runs and sets validationState to invalid or warning, the helperMessage may be programmatically set to a validation error message. This interaction is managed by the group's validation logic, but you can also set helperMessage directly for custom messaging.

**Localization**: Like all user-facing text, helperMessage should be internationalized/translated for different language contexts. Support different text lengths and cultural expectations for helpful messaging.

## maxSelection

Controls the maximum number of checkboxes that can be selected within the group. When set to a number, the group automatically disables unselected checkboxes once that many checkboxes have been selected, preventing additional selections until some are deselected. This is a behavioral prop that enforces selection limits.

**Behavior patterns**:

- **maxSelection undefined**: No limit on selections - users can select any number of checkboxes, from 0 up to all checkboxes in the group.

- **maxSelection = N**: Users can select at most N checkboxes. Once N checkboxes are selected, all other unselected checkboxes become automatically disabled (grayed out and unclickable). Users must deselect some currently selected checkboxes before they can select additional options.

- **maxSelection = 0**: Effectively treats as undefined or causes a warning. This value should be avoided in practice.

**Automatic disabling behavior**:
- When the number of selected checkboxes reaches maxSelection, the group identifies all unselected checkboxes and sets their disabledInternal property to true, making them visually disabled and non-interactive.
- When a checkbox is deselected (reducing selection count below maxSelection), the group re-enables previously disabled checkboxes by setting disabledInternal back to false.

**Interaction with disabled prop**:
- **disabled=false + maxSelection=N**: Checkboxes beyond the N selections are only disabled when the selection limit is reached, otherwise all checkboxes are interactive
- **disabled=true + maxSelection=N**: All checkboxes are disabled regardless of maxSelection (the prop-level disabled state takes precedence)
- The group only maxSelection controls which checkboxes are disabled as a result of the selection limit, not which are disabled due to the group-level disabled state

**Use cases**:
- **Limited selections**: "Select up to 3 options" (maxSelection=3)
- **Quotas and limits**: Enforce system limits like "maximum 5 file types"
- **Business rules**: Implement "choose at most 2 categories" constraints
- **User experience**: Prevent overwhelming selections in complex preference systems

**Accessibility considerations**: 
- When maxSelection is reached, the disabled state of unselected checkboxes should be communicated to screen readers via aria-disabled attributes
- Consider providing helperMessage guidance like "Select up to N options" to make the limit clear to users before they encounter it

**Validation integration**: maxSelection works independently from required validation. You can have both constraints simultaneously - for example, "Select between 2 and 5 options" (maxSelection=5, enforced via custom validation, with required validation ensuring at least 2 selections).

**Counting behavior**: Only selected checkboxes count toward maxSelection. Indeterminate checkbox states or partially selected checkboxes (if supported) are counted based on their underlying selected state, not their visual appearance.

## validationState

Controls the current validation status of the checkbox group, providing visual feedback about whether the current selection meets validation criteria. This visual prop affects the appearance validation indicators and typically triggers color changes associated with different validation states.

**Validation state values and their visual effects**:

- **validationState="none" (default)**: No validation state has been set. The checkbox group appears in its normal visual style without validation-specific coloring or indicators. This is the default state used when validation hasn't run yet or when validations passed without any status.

- **validationState="valid"**: The group indicates successful validation or that current selections meet all requirements. This state typically uses success colors (green) for validation-specific indicators like icons, borders, or helperMessage text.

- **validationState="invalid"**: The group indicates validation failure - current selections don't meet requirements (e.g., no checkboxes selected when required=true). This state typically uses error colors (red) for validation-specific indicators, drawing attention to the issue.

- **validationState="warning"**: The group indicates a cautionary validation condition - selections might not meet all requirements but aren't completely invalid. This state typically uses warning colors (amber/orange) for validation-specific indicators.

**Visual indicators**:
- **Helper message color**: When validationState is set, helperMessage text typically uses colors corresponding to the validation state (green for valid, red for invalid, amber for warning)
- **Border or accent colors**: Other validation-specific UI elements may use colors matching the validation state
- **Icons**: Validation icons (checkmarks, warning symbols, error indicators) may appear in colors corresponding to the state

**Use cases**:
- **validationState="none"**: Initial form load, cleared validation, reset state, or when validation hasn't been run yet
- **validationState="valid"**: Successful form submission, successful validation, or confirmation of valid selections
- **validationState="invalid"**: Required checkboxes not selected, validation failure, or error condition that needs user attention
- **validationState="warning"**: Cautionary validation, incomplete selections, or conditions that aren't fully invalid

**Interaction with validationMode**:
- **validationMode controls when**: ValidationMode determines when validation runs and consequently when validationState is updated
- **validationState shows the result**: validationState displays the current validation status after validation has run

**Programmatic control**: You can set validationState directly from your application code for custom validation logic beyond the built-in required validation. This allows implementing complex business rules while still using the component's visual feedback system.

**Accessibility**: Validation state changes should be announced to screen readers, particularly when switching to invalid states that require user action. The helperMessage text combined with validationState provides comprehensive accessibility communication.

**Form integration**: validationState is part of the form validation API, allowing form-level validation logic to check group state and provide appropriate user feedback.

## validationMode

Controls when the checkbox group executes validation logic and updates validationState. This behavioral prop determines the validation timing strategy for the group, affecting when users see validation feedback and how interactive the validation feels.

**Validation mode values and their behaviors**:

- **validationMode="none" (default)**: No automatic validation occurs. The group never runs validation logic and validationState is never automatically updated. This provides the most interactive experience but requires manual validation triggering or external validation logic.

- **validationMode="onChange"**: Validation runs immediately whenever checkbox selections change (on any click that affects which checkboxes are selected). This provides immediate feedback but may feel eager or trigger validation prematurely while users are still exploring options.

- **validationMode="onBlur"**: Validation runs when the checkbox group loses focus (when users click away or tab to another element). This provides feedback after users have finished making selections, reducing premature validation but potentially delaying feedback.

- **validationMode="onSubmit"**: Validation only runs when triggered by application code (typically on form submission). This defers validation until users are ready to submit, providing the least intrusive experience but potentially allowing users to proceed with invalid submissions until submission time.

**Validation trigger behaviors**:

- **onChange**: Fires validation on every click that changes selection state, including both selections and deselections. Best for immediate feedback loops and when you want users to see validation right away.

- **onBlur**: Fires validation when users leave the checkbox group (click elsewhere or tab to next element). Using a 20ms timeout to wait for focus to settle before validating, which prevents validation when focus moves within the group (e.g., from one checkbox to another).

- **onSubmit**: Doesn't automatically trigger - you must programmatically call validation when ready to submit. This requires more control in your application but avoids premature validation.

**Interaction with validationState**:
- **validationMode controls when**: ValidationMode determines timing for when validation runs
- **validationState shows the result**: After validation runs, validationState is updated based on the validation outcome

**Use cases**:
- **validationMode="none"**: When you want manual validation control, custom validation timing, or when validation logic is completely external to this component
- **validationMode="onChange"**: When you want immediate feedback, real-time validation updates, or when validation is simple and non-intrusive
- **validationMode="onBlur"**: When you want feedback after users complete their selections but before they move on, avoiding interruption of user flow
- **validationMode="onSubmit"**: When you want deferred validation until submission time, less intrusive experience, or when validation may be more complex

**Performance considerations**: onChange validation can trigger many validation runs in a complex form, potentially affecting performance. Validate onBlur tends to be more efficient while still providing timely feedback.

**Accessibility**: Validation feedback timing affects accessibility. Early feedback (onChange) helps users correct errors before continuing. Deferred feedback (onBlur/onSubmit) may make it harder to relate validation errors to the specific choices that caused them.

**Form integration**: validationMode works with form-level validation systems. Commonly used with validationState to create comprehensive validation across all form elements.

## disabled

When true, the entire checkbox group becomes non-interactive - users cannot select or deselect any of the individual checkboxes, and all checkboxes appear visually deactivated with reduced opacity and grayed styling. This is a visual/behavioral prop that signals and enforces an unavailable state for the entire group.

**Disabled state effects**:

- **Visual**: All checkboxes within the group appear "grayed out" with reduced opacity, typically around 50-60% of normal opacity. This signals visually that the entire element is not available for interaction.

- **Functional**: All user interaction is blocked across the entire group:
  - Clicking on any checkbox has no effect (selections cannot be changed)
  - Keyboard focus navigation skips the disabled group and its checkboxes
  - Space key does not toggle selections when checkboxes have focus
  - The group is excluded from form submission data as necessary

- **Event emission**: The valueChange event is NOT emitted for disabled checkboxes, even if there were internal selection changes (which is prevented by the disabled state anyway).

**Group-level vs item-level disabled state**:
- **disabled (group-level)**: The primary disabled prop that disables the entire group and all its checkboxes
- **disabledInternal (checkbox-level)**: Only checked by individual checkboxes when determining their disabled state, primarily used by maxSelection logic
- **Combined effect**: Final disabled state for each checkbox is determined by `disabled || disabledInternal`, but when group-level disabled=true, the maxSelection logic becomes irrelevant since all interactions are blocked anyway

**Accessibility considerations**:
- Keyboard navigation typically skips disabled elements (tab key moves past the entire group)
- Screen readers may announce "disabled" or similar status to indicate unavailability
- The disabled attribute is propagated to individual checkboxes for proper accessibility behavior

**Use cases for disabled state**:
- **Conditional availability**: Disable the group when related criteria aren't met (e.g., disable preference checkboxes when user has read-only permissions)
- **Processing states**: Temporarily disable selections while form submission or data processing occurs
- **Permission control**: Disable options the user doesn't have permission to change (admin-only preferences)
- **Progressive disclosure**: Disable future option groups until previous steps are completed

**Important distinction from readOnly**:
- **disabled**: Complete non-interactive state with visual cues of unavailability (grayed appearance) across entire group
- **readOnly**: Interactive appearance but selections cannot be changed by users, with normal visual presentation

**maxSelection interaction**: When disabled=true, the maxSelection logic is effectively irrelevant since all interactions are blocked regardless of selection count.

This prop provides both visual and functional disabling for the entire group, preventing any user interaction while providing clear visual feedback about the unavailable state.

## readOnly

When true, the checkbox group maintains visual interactivity but prevents changing the selection state of any checkboxes within it. Users can click and interact with checkboxes visually, but selections remain unchanged. This creates a read-only presentation that still allows exploration without committing changes.

**ReadOnly state effects**:

- **Visual**: The group and its checkboxes appear interactive and in normal visual style (not grayed like disabled). They maintain standard colors and transparency, suggesting they can be interacted with.

- **Functional**: User interaction is limited across the entire group:
  - Clicking on any checkbox does not change selection
  - Space key does not toggle selections on focused checkboxes
  - The checkboxes still respond to hover states and show normal visual feedback
  - Keyboard focus still works normally (can be tabbed to and focused)
  - The valueChange event is NOT emitted when users click

- **State preservation**: The group maintains its current selection state regardless of user interaction attempts. The value prop can still be changed programmatically from application code.

**Important distinction from disabled**:
- **disabled**: Complete non-interactive state with visual cues of unavailability (grayed appearance) across entire group
- **readOnly**: Interactive appearance but selections cannot be changed by users throughout the group

**Use cases for readOnly state**:
- **Displaying selections**: Show users which items are selected without allowing them to change (e.g., in review screens, displays, or confirmation dialogs)
- **Exploration modes**: Allow users to see what would happen if options were selected, without committing changes
- **Permission-based access**: Show options that might be available in other contexts but not changeable in current context
- **Conditional editing**: Make some checkbox groups read-only while others in the same form remain editable

**Interaction with props**:
- **readOnly + required**: The group maintains its requirement status semantically (for forms) even though users can't modify selections
- **readOnly + maxSelection**: The maxSelection limit is visually displayed but not enforced since users can't change selections anyway

**Accessibility considerations**:
- Keyboard navigation still works normally - checkboxes can receive focus and show focus indicators
- Screen readers announce the checkboxes but may indicate they're read-only
- The components may have aria-readonly or similar attributes for accessibility

**Form submission**: 
- In form submission, readOnly checkbox groups still use their current selection state values (unlike disabled groups which are excluded entirely)
- This allows displaying pre-selected options that cannot be changed but are included in submitted data

**Visual preview behavior**: Clicking on readOnly checkboxes may show momentary hover effects or visual feedback, but the selection state doesn't change. This can be confusing for users who expect clicking to change the state, so ensure UI clearly communicates read-only nature through helperMessage or other indicators.

This prop is primarily functional - it allows visual interaction but prevents selection changes throughout the group. It's useful for displaying static selection states while maintaining interactivity cues and accessibility structure.

## ariaLabel

Provides an accessible label for screen readers and assistive technologies for the checkbox group. The ariaLabel prop is used for accessibility when the group lacks a visible text label, or when you need to provide a more descriptive label than what's shown on screen. This is an accessibility prop that affects screen reader announcements but not visual presentation.

**Accessibility behavior**:
- **When ariaLabel is provided**: Screen readers use the ariaLabel text to announce the checkbox group's purpose instead of or in addition to the visible label (if any)
- **When ariaLabel is not provided**: The component uses the label text as the primary accessibility label for screen readers
- **For groups without labels**: Always provide ariaLabel to ensure accessibility compliance

**Use cases**:
- **No visual label**: Checkbox groups with no visible label text need ariaLabel for screen reader support
- **Supplemental descriptions**: Provide additional context or instructions that appear in screen reader announcements but not on screen
- **Technical labels**: Use more descriptive text for screen readers than what's visually displayed
- **Groups following headings**: May ariaLabel when the group immediately follows a descriptive heading and the label would be redundant

**Accessibility hierarchy**:
- **Primary source**: ariaLabel when provided
- **Fallback**: label text when ariaLabel is not provided
- **Next fallback**: content from description/helperMessage when label is also not provided
- **Failure**: None of the above results in inaccessible checkbox group for screen readers

**Screen reader announcements**:
- Includes the group's current validation state (when validationState is set to invalid/warning/valid)
- May announce requirement status (required/optional) from required prop and necessityIndicator
- May include the helperMessage text for additional context
- Typically announces "checkbox group, [ariaLabel or label text]" depending on screen reader

**Group vs individual checkbox accessibility**:
- **Group-level**: ariaLabel applies to the entire group as a whole, describing what the collection of checkboxes represents
- **Individual checkbox**: Each ion-checkbox still has its own label and ariaLabel for describing individual options
- This two-level accessibility structure provides comprehensive navigation and understanding

**Complex interactions**: The component constructs ariaLabelMessage combining multiple sources including ariaLabel, label, necessityIndicator, required, readOnly, validationState, and helperMessage. This provides comprehensive accessibility announcements.

**Internationalization**:
- ariaLabel should be translated/localized like any other user-facing text
- The visible label may be abbreviated for UI constraints, while ariaLabel can use full descriptions
- Screen reader language detection uses ariaLabel's text content

**Best practices**:
- Provide ariaLabel for checkbox groups without visible labels (WCAG accessibility requirement)
- Keep ariaLabel concise and descriptive (similar to visible label length guidelines)
- Avoid duplicating visible label content unnecessarily in ariaLabel unless additional context is needed
- Differentiate group-level ariaLabel (describing the group's purpose) from individual checkbox labels (describing each option)

This prop is purely accessibility-focused. It has no visual appearance but is essential for making checkbox groups accessible to screen reader users and assistive technology users, especially when groups lack visible labels.

## description

DEPRECATED - use helperMessage instead. Provides descriptive text or guidance for the checkbox group. This is a content prop that affects user guidance. The description prop is the older API and has been replaced by helperMessage, but is maintained for backward compatibility.

**Deprecated status**: This prop should no longer be used in new code. Use helperMessage instead, which provides the same functionality with better integration with validation states and clearer naming.

**Legacy behavior**: When description is provided (and helperMessage is not), the text appears in the same location as helperMessage would - typically below the checkbox group label or near the checkbox content area. This provides guidance, instructions, or tips to users.

**Migration guidance**: Replace description prop usage with helperMessage prop. The functionality is identical, but helperMessage provides better integration with validation states and follows modern API conventions.

**Technical note**: The component internally handles both description and helperMessage props, treating them as equivalent. If both are provided, preview to determine which takes precedence, or whether the more recent API (helperMessage) is preferred.

## orientation

DEPRECATED - use labelPlacement instead. Controls the layout of the label relative to the checkbox content area. This is a visual prop that determines whether the label appears above or beside the checkboxes.

**Deprecated status**: This prop should no longer be used in new code. Use labelPlacement instead, which provides clearer semantics about what the prop controls (label placement specifically, not general component orientation).

**Legacy behavior**: The orientation prop works identically to labelPlacement:
- **orientation="vertical"**: Label appears above the checkbox content area (same as labelPlacement="vertical")
- **orientation="horizontal"**: Label appears beside the checkbox content area (same as labelPlacement="horizontal")

**Migration guidance**: Replace orientation prop usage with labelPlacement prop. The functionality is identical, but labelPlacement provides clearer naming and better describes what the prop actually controls.

**Technical note**: The component internally handles both orientation and labelPlacement props, treating them as equivalent. If both are provided, the preview to determine which takes precedence, or whether conflicts are resolved with a specific precedence rule.

## Events

### selectionChange

DEPRECATED - Emitted when checkbox selection state changes. Use the valueChange event instead. This event provides the updated selection state and was the original API before valueChange was introduced.

**Event payload type**: `CustomEvent<{ name: string, value: any[] }>`

**When it fires**:
- **User clicks**: Fires when user clicks on any checkbox within the group (if the group is not disabled/readOnly)
- **Value changes**: Fires when the value prop is programmatically updated
- **MaxSelection changes**: Fires when checkboxes are automatically enabled/disabled due to maxSelection limits being reached

**Payload content**:
- **event.detail.name**: `string` - the group's name prop value (for form submission)
- **event.detail.value**: `any[]` - array of selected checkbox values (the values of checkboxes whose selection state is true)

**How to use - TypeScript handler**:
```typescript
onSelectionChange(event: CustomEvent<{ name: string, value: any[] }>) {
  const groupName = event.detail.name;
  const selectedValues = event.detail.value;
  console.log('Checkbox group', groupName, 'selection changed to:', selectedValues);
  // Update your state or perform logic using the new selection array
}
```

**Binding syntax**:
```html
<ion-checkbox-group (selectionChange)="onSelectionChange($event)">
</ion-checkbox-group>
```

**When to use**:
- DEPRECATED - Only use this event for maintaining backward compatibility with older code
- For new development, use the valueChange event instead, which provides identical functionality with clearer naming

**Important behaviors**:
- **CustomEvent wrapper**: Remember that event.detail contains the selection data object, not the event itself
- **Emitting behavior**: This event is emitted alongside valueChange for backward compatibility, but may be removed in future versions
- **User vs programmatic changes**: The event fires for both user interactions and programmatic value changes

**Complete example handling**:
```typescript
onSelectionChange(event: CustomEvent<{ name: string, value: any[] }>) {
  // Access the selection data via event.detail (NOT event itself)
  const { name, value } = event.detail;
  
  if (!value.length) {
    console.log('No checkboxes selected in group:', name);
    // Handle empty selection case
  } else {
    console.log(`Selected ${value.length} checkbox(es):`, value);
    // Process selections
  }
}
```

### valueChange

Emitted when checkbox selection state changes within the group. This is the current event API for tracking selection changes. The event provides the updated selection state and is the primary mechanism for responding to user interactions with the checkbox group.

**Event payload type**: `CustomEvent<{ name: string, value: any[] }>`

**When it fires**:
- **User clicks**: Fires when user clicks on any checkbox within the group (if the group is not disabled/readOnly)
- **Programmatic changes**: Fires when the value prop is programmatically updated
- **MaxSelection enforcement**: Fires when checkboxes are automatically enabled/disabled due to maxSelection limits being reached
- **Does NOT fire**: When the group is disabled or readOnly, since user interactions don't cause state changes in those cases

**Payload content**:
- **event.detail.name**: `string` - the group's name prop value (used for form submission identification)
- **event.detail.value**: `any[]` - array containing the value props of currently selected checkboxes (the values of checkboxes whose selection state is true). Empty array `[]` means no checkboxes are selected.

**How to use - TypeScript handler**:
```typescript
onValueChange(event: CustomEvent<{ name: string, value: any[] }>) {
  const groupName = event.detail.name;
  const selectedValues = event.detail.value;
  console.log('Checkbox group', groupName, 'value changed to:', selectedValues);
  
  if (selectedValues.length === 0) {
    console.log('No checkboxes selected - validation may fail if required=true');
  } else {
    console.log(`Selected ${selectedValues.length} option(s):`, selectedValues);
  }
}
```

**Binding syntax**:
```html
<ion-checkbox-group (valueChange)="onValueChange($event)">
</ion-checkbox-group>
```

**When to use**:
- **Form state management**: Track which checkboxes are selected for form submission or validation
- **Dependent controls**: Enable/disable other UI elements based on which checkboxes are selected
- **Data filtering**: Apply logic based on checkbox selections (e.g., filter lists, show/hide overlay content)
- **State persistence**: Save checkbox selections to local storage or backend
- **UI updates**: Update other parts of the interface in response to selection changes

**Important behaviors**:
- **CustomEvent wrapper**: Critical - event.detail contains the selection data object, not the event itself. Access data via event.detail.value and event.detail.name.
- **Array value format**: The value is always an array, even when no checkboxes are selected (empty array). This differs from single checkbox selectionChange which returns a boolean.
- **Complete state**: The event provides the complete selection state (all selected values), not just what changed. This makes it easier to work with than incremental updates.
- **User vs programmatic changes**: The event fires for both user interactions and programmatic value changes.

**Complete example handling**:
```typescript
onValueChange(event: CustomEvent<{ name: string, value: any[] }>) {
  // Access the selection data via event.detail (NOT event itself)
  const { name, value: selectedValues } = event.detail;
  
  // Example: Update local component state with new selections
  this.selectedOptions = selectedValues;
  
  // Example: Run validation based on current selections
  if (this.required && selectedValues.length === 0) {
    this.validationState = 'invalid';
    this.helperMessage = 'At least one option must be selected';
  }
  
  // Example: Enable/disable dependent UI based on selection count
  this.canProceed = selectedValues.length > 0;
  
  // Example: Log selection changes for debugging
  console.log(`Group "${name}" selection: ${selectedValues.join(', ')}`);
}
```

**Complete event binding example** (combining both events for backward compatibility):
```html
<ion-checkbox-group 
  [name]="interests"
  [value]="selectedInterests"
  [required]="true"
  (selectionChange)="onSelectionChange($event)"
  (valueChange)="onValueChange($event)">
  <ion-checkbox *ngFor="let interest of interestOptions" 
    [label]="interest.label" 
    [value]="interest.value">
  </ion-checkbox>
</ion-checkbox-group>
```

```typescript
// Combined handler implementation
onSelectionChange(event: CustomEvent<{ name: string, value: any[] }>) {
  // DEPRECATED: Only maintaining for backward compatibility
  console.log('[DEPRECATED] Selection changed:', event.detail.value);
}

onValueChange(event: CustomEvent<{ name: string, value: any[] }>) {
  // Current API - use this event for all new development
  const { name, value } = event.detail;
  this.selections = value;
  
  // Run validation if needed
  if (this.required && value.length === 0) {
    this.validationState = 'invalid';
  }
}
```

## Examples

### Basic Checkbox Group
```html
<ion-checkbox-group 
  [label]="Select your preferences" 
  (valueChange)="onPreferenceChange($event)">
  <ion-checkbox label="Email updates" value="email"></ion-checkbox>
  <ion-checkbox label="SMS notifications" value="sms"></ion-checkbox>
  <ion-checkbox label="Push notifications" value="push"></ion-checkbox>
</ion-checkbox-group>
```
**Demonstrates**: Basic checkbox group with label and event handling

### Checkbox Group with Size Variants
```html
<ion-checkbox-group 
  label="Size: sm" 
  size="sm" 
  (valueChange)="onSizeChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>

<ion-checkbox-group 
  label="Size: md" 
  [size]="'md'" 
  (valueChange)="onSizeChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>

<ion-checkbox-group 
  label="Size: lg" 
  [size]="'lg'" 
  (valueChange)="onSizeChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>
```
**Demonstrates**: Different size variants (sm, md, lg) applied to checkbox groups

### Checkbox Group with Emphasis
```html
<ion-checkbox-group 
  [emphasized]="false" 
  [value]="selectedOptions"
  (valueChange)=" onEmphasisChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>

<ion-checkbox-group 
  [emphasized]="true" 
  [value]="selectedOptions"
  (valueChange)="onEmphasisChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>
```
**Demonstrates**: Emphasized vs non-emphasized checkbox groups with visual styling differences

### Checkbox Group with Label Placement Options
```html
<ion-checkbox-group 
  [label]="Label" 
  [label-placement]="'vertical'" 
  (valueChange)="onLabelPlacementChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>

<ion-checkbox-group 
  [label]="Label" 
  [label-placement]="'horizontal'" 
  (valueChange)="onLabelPlacementChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>
```
**Demonstrates**: Vertical vs horizontal label placement affecting layout

### Checkbox Group with Content Orientation
```html
<ion-checkbox-group 
  [label]="Label" 
  [value]="selectedOptions"
  [content-orientation]="'vertical'" 
  (valueChange)="onOrientationChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>

<ion-checkbox-group 
  [label]="Label" 
  [value]="selectedOptions"
  [content-orientation]="'horizontal'" 
  (valueChange)="onOrientationChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>
```
**Demonstrates**: Vertical vs horizontal arrangement of checkboxes within the group

### Checkbox Group with Default Value
```html
<ion-checkbox-group 
  [label]="Label" 
  [defaultValue]="['Option1', 'Option2']" 
  (valueChange)="onDefaultValueChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>
```
**Demonstrates**: Using defaultValue to set initial selections (uncontrolled pattern)

### Checkbox Group with Validation States
```html
<ion-checkbox-group 
  [label]="Label" 
  [helper-message]="Helper Message" 
  [validation-state]="'none'" 
  (valueChange)="onValidationChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>

<ion-checkbox-group 
  [label]="Label" 
  [helper-message]="Valid Helper Message" 
  [validation-state]="'valid'" 
  (valueChange)="onValidationChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>

<ion-checkbox-group 
  [label]="Label" 
  [helper-message]="Invalid Helper Message" 
  [validation-state]="'invalid'" 
  (valueChange)="onValidationChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>

<ion-checkbox-group 
  [label]="Label" 
  [helper-message]="Warning Helper Message" 
  [validation-state]="'warning'" 
  (valueChange)="onValidationChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>
```
**Demonstrates**: Different validation states with appropriate helper messages and colors

### Checkbox Group with Max Selection
```html
<ion-checkbox-group 
  [label]="Label" 
  [value]="selectedOptions"
  [max-selection]="null" 
  (valueChange)="onMaxSelectionChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>

<ion-checkbox-group 
  [label]="Label" 
  [value]="selectedOptions"
  [max-selection]="2" 
  (valueChange)="onMaxSelectionChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>
```
**Demonstrates**: No limit vs maximum 2 selections, with automatic disabling when limit reached

### Checkbox Group with Required and Necessity Indicator
```html
<ion-checkbox-group 
  [required]="false" 
  [necessity-indicator]="'requiredMarker'" 
  [label]="Checkbox Group" 
  (valueChange)="onRequiredChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>

<ion-checkbox-group 
  [required]="true" 
  [necessity-indicator]="'requiredMarker'" 
  [label]="Checkbox Group" 
  (valueChange)="onRequiredChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>
```
**Demonstrates**: Required vs optional states with necessity indicator display

### Checkbox Group with Validation Mode
```html
<ion-checkbox-group 
  [label]="Label" 
  [label-placement]="'vertical'" 
  [required]="true" 
  [validation-mode]="'onBlur'" 
  (valueChange)="onValidationModeChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>

<ion-checkbox-group 
  [label]="Label" 
  [label-placement]="'vertical'" 
  [required]="true" 
  [validation-mode]="'onChange'" 
  (valueChange)="onValidationModeChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>
```
**Demonstrates**: Different validation modes (onBlur vs onChange) affecting when validation runs

### Complete Playground Example
```html
<ion-checkbox-group 
  [size]="'medium'" 
  [emphasized]="false" 
  [label]="Label" 
  [label-placement]="'vertical'" 
  [label-alignment]="'start'" 
  [label-width]="" 
  [required]="false" 
  [necessity-indicator]="'requiredMarker'" 
  [content-orientation]="'vertical'" 
  [name]="" 
  [value]="options" 
  [default-value]="[]" 
  [helper-message]="" 
  [max-selection]="3" 
  [validation-state]="'none'" 
  [validation-mode]="'none'" 
  [disabled]="false" 
  [readOnly]="false" 
  [aria-label]="'Aria Label'" 
  (valueChange)="onValueChange($event)">
  <ion-checkbox *ngFor="let opt of options" [label]="opt" [value]="opt"></ion-checkbox>
</ion-checkbox-group>
```
**Demonstrates**: Complete configuration with all props for interactive exploration

### Indeterminate Checkbox with Checkbox Group Pattern
```html
<!-- Parent indeterminate checkbox (NOT part of checkbox-group) -->
<ion-checkbox 
  label="Select all options" 
  [indeterminate]="indeterminateState" 
  [selected]="selectAllState" 
  (selectionChange)="onSelectAllChange($event)"></ion-checkbox>

<!-- Checkbox group for child options -->
<ion-checkbox-group 
  [value]="selectedChildOptions" 
  (valueChange)="onChildSelectionChange($event)">
  <ion-checkbox *ngFor="let child of childOptions" [label]="child.label" [value]="child.value"></ion-checkbox>
</ion-checkbox-group>
```
**Demonstrates**: Pattern for parent-child checkbox relationships where parent uses indeterminate state while children use checkbox-group