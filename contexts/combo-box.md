---

realComponent: "ion-combo-box"
description: "An advanced form component that combines text input with dropdown selection, supporting filtering, dynamic options, custom values, and multi-select with tag-based interactions"
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
  - name: "disableEdit"
    type: "boolean"
    category: "behavioral"
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
  - name: "loadThrottle"
    type: "number"
    category: "behavioral"
    required: false
    default: "300"
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
  - name: "loading"
    type: "boolean"
    category: "visual"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "headerElement"
    type: "string | IonElement"
    category: "content"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "footerElement"
    type: "string | IonElement"
    category: "content"
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
  - name: "allowCustomValue"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "limit"
    type: "number"
    category: "behavioral"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "disableTags"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "true"
    values: []
    designTokens: {}
  - name: "filterMode"
    type: "FilterMode"
    category: "behavioral"
    required: false
    default: "SingleToken"
    values:
      - SingleToken
      - MultiToken
      - StartsWith
    designTokens: {}
  - name: "filterKeys"
    type: "string[]"
    category: "behavioral"
    required: false
    default: '["label"]'
    values: []
    designTokens: {}
  - name: "caseSensitiveFilter"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "disableDefaultSorting"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "disableSpellCheck"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "hideArrowButton"
    type: "boolean"
    category: "visual"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "selectOptionsOnPaste"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "disableVirtualScroll"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "groupSelectedOptions"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "true"
    values: []
    designTokens: {}
  - name: "maxVisibleRows"
    type: "number"
    category: "visual"
    required: false
    default: "1"
    values: []
    designTokens: {}
  - name: "tagDisplay"
    type: "TagDisplay"
    category: "visual"
    required: false
    default: "collapsed"
    values:
      - collapsed
      - wrap
    designTokens: {}
  - name: "overflowMode"
    type: "OverflowMode"
    category: "behavioral"
    required: false
    default: "clip"
    values:
      - clip
      - scroll
    designTokens: {}
  - name: "disableFullScreenMode"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "mobileDrawerHeight"
    type: "number"
    category: "visual"
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
  - name: "setSearchText"
    type: "(value: string) => void"
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
  - name: "maxLength"
    type: "number"
    category: "behavioral"
    required: false
    default: "-1"
    values: []
    designTokens: {}
  - name: "optionTemplate"
    type: "IonElement<IDropdownOption>"
    category: "visual"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "textTransform"
    type: "string"
    category: "visual"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "disableWhiteSpaceTrimming"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "false"
    values: []
    designTokens: {}
jointTokens: []
propInteractions:
  - "disableEdit disables text input while still allowing dropdown selection, preventing users from typing to filter options but permitting selection from the dropdown menu. When disableEdit=true, the input field becomes read-only but users can still click to open and select from the dropdown menu."
  - "filterMode controls how the combo-box filters options based on user input: SingleToken (matches individual tokens/words), MultiToken (matches multiple tokens), StartsWith (matches beginning of strings). Only applies when disableEdit=false."
  - "caseSensitiveFilter determines whether filtering considers case matching (caseSensitiveFilter=true) or performs case-insensitive matching (caseSensitiveFilter=false). Only applies when disableEdit=false."
  - "filterKeys specifies which properties of option objects are used for filtering. Default is ['label'], but can be extended to other properties like description or custom fields. Only applies when disableEdit=false."
  - "disableDefaultSorting controls whether options are automatically sorted based on matching scores (disableDefaultSorting=false) or maintain their original order (disableDefaultSorting=true). Only affects filtering behavior when disableEdit=false."
  - "allowCustomValue enables users to input and select values that don't exist in the predefined options list. When allowCustomValue=true, typed non-matching values become valid selections and are stored. When allowCustomValue=false, non-matching input is rejected on blur."
  - "selectOptionsOnPaste enables automatic option selection when users paste text containing the separator character into the input field. When selectOptionsOnPaste=true, pasted text is split by separator and matching options are auto-selected. Only applies when multiSelect=true."
  - "virtualScroll is automatically enabled for dynamic options (when options is a function) or static options with 15+ items. disableVirtualScroll explicitly disables virtual scrolling even when it would normally be auto-enabled."
  - "disableTags controls how selected values are displayed in multi-select mode. When disableTags=true, selected values appear as comma-separated text; when disableTags=false, they appear as removable tags. Only applies when multiSelect=true."
  - "tagDisplay controls the layout behavior for tags vs non-tags display: tagDisplay=collapsed shows single row with +N overflow indicator that expands on click; tagDisplay=wrap allows tags to wrap to multiple rows. Works with both disableTags=true and disableTags=false."
  - "overflowMode controls how selected options overflow beyond maxVisibleRows: overflowMode=clip hides excess options and shows +N counter; overflowMode=scroll makes the container scrollable. Only applies when maxVisibleRows > 1 and tagDisplay=wrap or when overflowCountClick is true."
  - "maxVisibleRows controls the number of rows used for displaying selected options. In collapsed mode, initially shows 1 row with +N overflow indicator that expands to maxVisibleRows. In wrap mode, constrains to maxVisibleRows with scroll overflow. Interacts with tagDisplay and overflowMode for final handling."
  - "totalSelected changes the display of selected options when multiSelect=true. When totalSelected=true, shows 'X selected' count instead of individual labels, except when all options are selected and allSelectionValue is set, then shows allSelectionValue text."
  - "confirmOnApply controls multi-select confirmation behavior: when confirmOnApply=false, changes are applied immediately; when confirmOnApply=true, changes are applied only after user clicks Apply button. When confirmOnApply=true, Clear and Apply buttons appear in the dropdown footer."
  - "disableFullScreenMode controls mobile behavior: when disableFullScreenMode=true on mobile devices, uses popover instead of full-screen drawer; when disableFullScreenMode=false (default), uses drawer for better mobile UX. On desktop, this prop has no effect."
  - "groupSelectedOptions controls how selected options are organized in the dropdown when multiSelect=true. When groupSelectedOptions=true, selected options are grouped together at the top of their respective groups; when false, selections stay in their original positions."
  - "showSelectAll adds a 'select all' checkbox at the top of the dropdown when multiSelect=true and showSelectAll=true. This allows users to select all visible options with a single click."
  - "maxSelection and groupMaxSelection both limit multi-select but at different scopes: maxSelection applies to all options in the dropdown, groupMaxSelection applies per option group. Both default to Infinity (no limit) when not set."
  - "mobileDrawerHeight controls the height of the mobile drawer in pixels when disableFullScreenMode=false. This prop only applies on mobile devices using drawer mode, no desktop impact."
  - "clearButton and confirmOnApply interact: when confirmOnApply=true, the field-level clearButton is hidden (confirmOnApply logic applies instead of clearButton). clearButton is only visible when confirmOnApply=false."
  - "disableEdit and confirmOnApply interact: when disableEdit=true, users cannot type in the input field but can still select from dropdown; when both disableEdit=true and confirmOnApply=true, the multi-select confirmation workflow applies to dropdown selections only."
  - "disableEdit and selectOptionsOnPaste interact: selectOptionsOnPaste requires disableEdit=false for typing and paste functionality, and multiSelect=true for the selection behavior that pasted options should populate."
  - "tagDisplay and overflowMode interact: when tagDisplay=wrap and maxVisibleRows >= 3, scroll mode is used automatically; when tagDisplay=collapsed, clip mode shows +N counter."
  - "overflowMode and maxVisibleRows interact: when overflowMode=scroll, all selected options are visible and scrollable; when overflowMode=clip, excess options are hidden and shown as +N counter."
  - "maxVisibleRows and tagDisplay interaction: maxVisibleRows limits number of rows, tagDisplay determines wrapping vs single-row behavior for those rows."
  - "limit controls visible filtered options count but enforce selection limits via maxSelection and groupMaxSelection - different scoping with limit being for display only."
  - "totalSelected and allSelectionValue work together: when totalSelected=true and all options are selected, allSelectionValue is displayed in the field instead of the comma-separated list of option labels."
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
  - "Tag styling tokens for selected option tags could not be fully traced. While dropdown-ds.css contains dropdown item styling, specific tag styling tokens (ion-comp-tag-non-selectable-*) were referenced but not fully documented."
  - "Virtual scroll behavior and performance thresholds (Static_Options_Virtualization_Threshold = 15) are implemented but the exact rendering performance characteristics were not fully traceable from the available code."
  - "Search engine configuration (FilterMode options: SingleToken, MultiToken, StartsWith) was defined but the exact fuzzy search algorithms and scoring mechanisms could not be fully traced from the available source code."
  - "Mobile drawer mode vs popover mode decision logic based on disableFullScreenMode and device detection is implemented but the exact breakpoints and responsive behavior could not be fully traced."
  - "textTransform and disableWhiteSpaceTrimming props exist but their effect on styling could not be traced through available CSS/LESS files."
  - "The toggleDropdownOnClick prop exists in the source code (line 2366-2374) but is not documented in the public interface IComboBoxComponent interface - this may be an internal-only property."
  - "The _inputValue property exists in source code (lines 435-450) but there is no public input signal that would correspond - users interact via the textChange event instead."
  - "The searchEngine and filteredOptions properties are internal implementation details not exposed as public props - users interact via filtering props like filterMode, filterKeys, caseSensitiveFilter, and filtering events."
  - "The RawOptions type (IDropdownItem[] | IDropdownOptionGroup[]) and IDropdownValueChangeEventArgs interface are internal types used by the combo-box implementation, not documented as public interfaces for external use."
  - "The NativeGroupedOptions type is an internal implementation for native select mode, not a public interface for external use."
  - "The _dropdownMenuState (IDropdownMenuState) and toggleDropdownOnClick properties are internal implementation details not exposed as public interface elements."
  - "The drawerOpen property and related drawer service integration are internal implementation details for mobile drawer presentation."
  - "The searchEngineFactory and ISearchEngine types are internal for implementing advanced search functionality - users interact via filterMode, filterKeys, etc."
  - "The MqDesignStringParserService parsing behavior for responsive sizes could not be fully traced - only the output parsing logic was examined, not the configuration format."
  - "The debounce function and loadThrottle behavior for dynamic options could not be fully traced through the async option fetching logic."
  - "The componentAnalyticsService.track() calls throughout the code suggest analytics integration but the specific tracking implementation and data model could not be fully traced."
  - "The componentService.asIonElement() usage for optionTemplate is referenced but the template function signature and IonElement contract were not fully documented from the public API."
  - "The loadThrottle defaults to 300ms but the relationship between debounce timing and actual network request timing could not be fully transparent from the provided code."
  - "The isNative boolean flag controls internal native select rendering on mobile devices based on design system configuration - this is implementation detail, not a public prop."
  - "The isMobileDevice flag is internal environment service state for responsive behavior - not exposed as a public prop."
  - "The valueLabelMap Map is internal for value-to-label resolution - users interact via the value prop and providing options."
  - "The inputFieldWidth calculation and responsive componentDeregister are internal layout management details not exposed as public concerns."
  - "The toggleDropdownOnClick flag is internal dropdown Interaction logic control, not a documented public prop."
  - "overflowCountClick is mentioned in propInteractions but was not found as a documented public prop - this may be an internal implementation detail."
events:
  - name: "valueChange"
    payloadType: "CustomEvent<{ name: string, value: any }>"
    firesWhen: "Emitted whenever the selected option(s) changes - on every selection change in single-select mode, on confirmation in multi-select with confirmOnApply=true, and when custom values are entered and validated with allowCustomValue=true"
    detailAccess: "event.detail.name (string) - the combo-box's name attribute if set; event.detail.value (any) - the selected value (single value for single-select, array of values for multi-select)"
    bindingSyntax: "(valueChange)=\"onValueChange($event)\""
  - name: "dropdownStateChanged"
    payloadType: "CustomEvent<boolean>"
    firesWhen: "Emitted when the combo-box panel opens or closes - fires with true when opening, false when closing"
    detailAccess: "event.detail (boolean) - true if combo-box is opening, false if combo-box is closing"
    bindingSyntax: "(dropdownStateChanged)=\"onDropdownStateChanged($event)\""
  - name: "focusIn"
    payloadType: "CustomEvent<void>"
    firesWhen: "Emitted when the combo-box field receives focus - when users click or tab into the field, or when focus is set programmatically"
    detailAccess: "void, event.detail is undefined - this event signals focus state change without carrying data"
    bindingSyntax: "(focusIn)=\"onFocusIn()\""
  - name: "focusOut"
    payloadType: "CustomEvent<void>"
    firesWhen: "Emitted when the combo-box field loses focus - when users click away, tab out, or when focus is removed programmatically"
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
  - name: "keyDown"
    payloadType: "CustomEvent<KeyboardEvent>"
    firesWhen: "Emitted when keyboard events occur within the combo-box field - includes special handling for navigation, selection, and editing interactions"
    detailAccess: "event.detail (KeyboardEvent) - the native keyboard event with key code, modifiers, and other event properties"
    bindingSyntax: "(keyDown)=\"onKeyDown($event)\""
  - name: "textChange"
    payloadType: "CustomEvent<{ value: string, reason: \"TextInput\" | \"Blur\" | \"SelectionChange\" | \"ItemRemove\" }>"
    firesWhen: "Emitted when the text input value changes - on each keystroke (TextInput), when field loses focus (Blur), when an option is selected (SelectionChange), or when a tag is removed (ItemRemove)"
    detailAccess: "event.detail (object) - event.detail.value (string): the new text input value; event.detail.reason (string): the reason for the change - \"TextInput\", \"Blur\", \"SelectionChange\", or \"ItemRemove\""
    bindingSyntax: "(textChange)=\"onTextChange($event)\""
  - name: "filteredOptionsLengthChanged"
    payloadType: "CustomEvent<number>"
    firesWhen: "Emitted when the number of filtered options changes due to typing, search, or options loading - useful for showing/hiding 'no results' messages or updating UI based on available options"
    detailAccess: "event.detail (number) - the count of currently filtered options available in the dropdown"
    bindingSyntax: "(filteredOptionsLengthChanged)=\"onFilteredOptionsLengthChanged($event)\""
---

## Usage Notes

Boolean props must use explicit string values in HTML templates (e.g., `disabled="true"`, `disabled="false"`), not bare attributes like `disabled` or `disabled` alone.

## size

Controls the height, padding, typography size, and arrow icon dimensions of the combo-box field. Size values (sm, md, lg) map to design system spacing and typography tokens that scale the entire field vertically. This is a visual prop that directly impacts the user's perception of the component's scale and prominence in the interface.

The actual rendered size is determined by MQ (Media Query) responsive strings that allow different sizes at different breakpoints. Without an MQ string, the size translates directly (sm=small, md=medium, lg=large). With MQ strings, each breakpoint can map to a different size - for example, the default behavior is xs=lg, sm=md, md=md, lg=md, xl=md, which means extra-small screens get large fields for touch targets, while medium through extra-large screens get medium-sized fields.

**Visual cues for each size**:
- **sm**: Shorter field height, smaller padding, smaller font for selected text, smaller arrow icon (16px), tighter internal spacing
- **md**: Medium field height (default), standard padding, regular font size for selected text, medium arrow icon (24px), standard internal spacing  
- **lg**: Taller field height, larger padding, larger font for selected text, larger arrow icon (32px), more generous internal spacing

This prop is self-contained and does not depend on other props for its effect. It drives multiple visual properties simultaneously (height, padding, typography, icon size) through the component's CSS classes that map to design tokens.

**Important interaction with disableEdit**: When disableEdit=true, the size prop still applies since it affects the entire field appearance, but the input area is read-only while still maintaining its size.

**Important interaction with clearButton**: The clear button icon automatically scales to match the combo-box's size prop (16px for sm, 24px for md, 32px for lg).

Values:
- `sm`: Small size for compact layouts
- `md`: Default medium size
- `lg`: Large size for prominence

Usage: `size="lg"`

## disabled

When true, the combo-box field becomes completely non-interactive - users cannot click to open the dropdown menu, and the field appears visually deactivated with reduced opacity (typically 0.4) and grayed styling. This is a visual/behavioral prop that signals and enforces unavailable state.

The disabled state prevents any user interaction with the combo-box - clicking on the field does not open the dropdown menu, typing is disabled, keyboard navigation is disabled, and the clear button (if enabled) is also non-functional. The combo-box maintains its selected value but users cannot change it.

**Visual indicators of disabled state**:
- Reduced opacity field (approx. 60% of normal opacity)
- Grayed appearance for text and icons
- Non-interactive cursor (not clickable)
- All interactive elements within the combo-box (arrow icon, clear button, enhancers) appear disabled

This prop is self-contained and does not depend on other props. It overrides all interactive behavior regardless of other settings.

**Important interaction with disableEdit**: When disabled=true, the disableEdit prop has no effect since all interaction is already blocked by the disabled state.

**Important interaction with readOnly**: Disabled and readOnly have different use cases - disabled completely prevents interaction, while readOnly allows limited interaction (opening dropdown). Do not use both together; if both are set, disabled takes precedence.

Usage: `disabled="true"`

## readOnly

When true, the combo-box field maintains user interaction for opening the dropdown menu but prevents typing to filter or entering custom values. Users can click to expand and view the dropdown options, but the text input area is read-only. This creates a read-only presentation that still allows exploring the option list.

The readOnly state allows users to see the full dropdown menu and all available options but commits no text input changes. This is useful for scenarios where you want users to be able to select from predefined options only, without the ability to type custom values or filter.

**Visual indicators of readOnly state**:
- Field appears interactive (normal opacity, interactive cursor)
- Arrow icon indicates dropdown can be opened
- Text input area has read-only appearance (cursor may indicate non-editable)
- Clear button (if enabled) works for clearing selections

**Important interaction with disableEdit**: ReadOnly and disableEdit are mutually exclusive in behavior:
- readOnly=true: Prevents text input but allows dropdown selection from options
- disableEdit=true: Makes input field read-only but allows dropdown selection
- Both achieve similar text input restriction but readOnly is the primary property for this behavior

**Important interaction with allowCustomValue**: When readOnly=true, the allowCustomValue prop has no effect since users cannot type custom values anyway. Conversely, when allowCustomValue=true, readOnly should not be used together as they represent conflicting interaction models.

**Use cases**: 
- **Predefined option selection**: Use readOnly when users should only select from available options
- **Dropdown-only interaction**: Use readOnly when you want dropdown selection but no text filtering
- **Protected fields**: Use readOnly when the field should not be editable but users need to see and select from options

This prop is self-contained and does not depend on other props for its core behavior. It provides read-only access to the dropdown's option list while preventing text input.

Usage: `readOnly="true"`

## disableEdit

Disables text input while still allowing dropdown selection, preventing users from typing to filter options but permitting selection from the dropdown menu. When disableEdit=true, the input field becomes read-only but users can still click to open and select from the dropdown menu. This is a behavioral prop that creates a dropdown-only interaction mode while the input area is non-editable.

The disableEdit state makes the combo-box behave more like a traditional dropdown - users select from predefined options but cannot type to filter or enter custom values. The text input area appears read-only (possibly with visual indication like cursor change or reduced opacity) but the dropdown arrow remains functional.

**Visual indicators of disableEdit state**:
- Input field appears read-only (different cursor, possibly styling changes)
- Dropdown arrow remains interactive and clickable
- Combination box shows selected value but does not accept keyboard typing
- Clear button (if enabled) works for clearing selections

**Important interaction with filterMode**: The filterMode prop only applies when disableEdit=false. When disableEdit=true, filtering is not applicable since users cannot type to filter options. Filtering properties (filterKeys, caseSensitiveFilter, disableDefaultSorting) have no effect.

**Important interaction with allowCustomValue**: When disableEdit=true, the allowCustomValue prop has no effect since users cannot type custom values into the input field. Custom values can only be entered when both disableEdit=false and allowCustomValue=true.

**Important interaction with selectOptionsOnPaste**: Select options on paste functionality requires disableEdit=false for typing and paste functionality. When disableEdit=true, the selectOptionsOnPaste prop is ignored since pasting is not possible in the read-only input.

**Important interaction with confirmOnApply**: When disableEdit=true and confirmOnApply=true (in multi-select mode), the confirmation workflow only applies to dropdown selections. Users cannot type but can select from dropdown, then confirm with Apply button.

**Use cases**:
- **Dropdown-only interaction**: Use disableEdit when you want users to select from options only, no typing
- **Predefined selections**: Use disableEdit when filtering would be distracting or unnecessary
- **Touch-friendly interfaces**: Use disableEdit for dropdown interaction without text input on touch devices

This prop is behavioral and affects how users interact with the combo-box. It is particularly useful when you want dropdown selection behavior without text filtering capabilities.

Usage: `disableEdit="true"`

## label

The text content displayed as the field's identifier, typically positioned above (vertical placement) or beside (horizontal placement) the combo-box field. Labels provide context and help users understand what the combo-box is for. This is a content prop that does not affect the component's behavior or visual appearance beyond the text content.

The label prop accepts plain text strings. The visual presentation (font size, weight, placement, spacing) is controlled by other props like labelPlacement, labelWidth, and the overall component size.

When no label is provided, the combo-box field appears without a text identifier, which may be appropriate when a label is provided elsewhere in the UI (e.g., adjacent to the field as part of a larger form layout).

**Visual presentation**: The label uses styling from the design system (typography, color, weight) that creates clear hierarchy with the field text. In vertical placement, the label appears above the field with appropriate spacing. In horizontal placement, the label and field share horizontal space.

**Important interaction with labelPlacement**: The label's position is controlled by labelPlacement - vertical (above field, default) or horizontal (beside field). The label content remains the same regardless of placement.

**Important interaction with labelWidth**: When labelWidth is specified and labelPlacement=horizontal, the label's width is constrained to the specified value. Otherwise, the label takes its natural content width.

**Important interaction with necessityIndicator**: The necessity indicator (asterisk or "Required"/"Optional" text) appears next to the label text when configured via the necessityIndicator prop.

This prop is self-contained for content but its visual presentation depends on labelPlacement and labelAlignment.

Usage: `label="Select an option"`

## labelPlacement

Controls whether the label appears above the field (vertical) or beside it (horizontal). This is a visual/layout prop that affects the overall structure of the component and how it integrates with surrounding layout.

**Label placement values**:
- **vertical**: Label appears above the combo-box field, stacked vertically. This is the default and most common pattern for form fields where labels identify what each field does independently.
- **horizontal**: Label appears beside the combo-box field, arranged horizontally. This is useful for compact forms or when you want the label and field to fit within a single row.

**Visual cues for each placement**:
- **vertical**: Label positioned above the field, field spans full container width below the label, ideal for detailed labels or when multiple fields stack vertically
- **horizontal**: Label positioned to the left of the field, label and field share horizontal space within container, useful for compact layouts or short labels

This prop's effect is independent of other props, but its practical use often correlates with labelAlignment (only relevant for horizontal placement) and labelWidth (most commonly used with horizontal placement to control label-to-field spacing).

**Important interaction with labelAlignment**: The labelAlignment prop only has visual effect when labelPlacement=horizontal. When labelPlacement=vertical, labelAlignment has no effect because the label occupies the full width above the field.

**Important interaction with labelWidth**: The labelWidth prop is most useful with labelPlacement=horizontal to create consistent label-to-field spacing across multiple fields in a form. When labelWidth is not specified and labelPlacement=horizontal, the label takes its natural width based on content.

**Important interaction with component size**: The label line height scales with the component size prop to maintain consistent vertical rhythm. Larger size fields have appropriately scaled label typography.

Values:
- `vertical`: Label appears above the field (default)
- `horizontal`: Label appears to the left of the field

Usage: `labelPlacement="horizontal"`

## labelAlignment

Controls whether the label is aligned to the start (left in LTR, right in RTL) or end (right in LTR, left in RTL) of the label area when labelPlacement=horizontal. This is a visual prop that only affects horizontal label arrangements and has no effect when labelPlacement=vertical.

**Label alignment values**:
- **start**: Label aligns to the start of the label area - left for left-to-right locales, right for right-to-left locales. This is the default and most common alignment.
- **end**: Label aligns to the end of the label area - right for left-to-right locales, left for right-to-left locales. This creates a rarer right-aligned label pattern, useful for specific design needs.

**Important interaction with labelPlacement**: This prop only has a visual effect when labelPlacement=horizontal. When labelPlacement=vertical, labelAlignment has no effect because the label occupies the full width above the field.

**Visual cues for each alignment (when labelPlacement=horizontal)**:
- **start**: Label text starts at the left edge of the label area, creating left-aligned appearance in LTR. Most common pattern and familiar to users.
- **end**: Label text aligns to the right edge of the label area, creating right-aligned appearance in LTR. Less common pattern, used for specific design requirements.

**Important interaction with labelWidth**: When labelWidth is also specified, the labelAlignment controls text positioning within that constrained width. For example, with labelWidth="150px" and labelAlignment="end", the label text aligns to the right edge of that 150px area.

This prop is dependent on labelPlacement=horizontal for its effect. When used without setting labelPlacement=horizontal, it appears to have no effect.

Values:
- `start`: Left-aligned label (default)
- `end`: Right-aligned label

Usage: `labelAlignment="end"`

## labelWidth

Controls the width of the label area when labelWidth is explicitly set. This is a visual/layout prop that allows precise control over how much horizontal space the label occupies when labelPlacement=horizontal. The value accepts CSS length units (e.g., "100px", "30%", "12rem") and is applied directly to the label container.

Label width is most commonly used with labelPlacement=horizontal to create consistent label-to-field spacing across multiple fields in a form. When labelWidth is not specified, the label takes its natural width based on the content.

**Important interaction with labelPlacement**: This prop primarily affects horizontal label arrangements. When labelPlacement=vertical, labelWidth still applies but has less visual impact since the label occupies the full width above the field anyway.

**Visual cues for different label widths (with labelPlacement=horizontal)**:
- **Narrow label** (e.g., "80px"): Label text may wrap or truncate, field takes more horizontal space, useful for short labels like "Name" or "ID"
- **Wide label** (e.g., "300px"): Label has ample space, field may be constrained, useful for detailed labels in compact forms
- **No labelWidth specified**: Label takes natural content width, field fills remaining horizontal space

**Important interaction with labelAlignment**: When labelWidth and labelAlignment are both specified, labelAlignment controls text positioning within the constrained label width. For example, labelWidth="200px" + labelAlignment="end" aligns label text to the right edge within that 200px area.

**Important interaction with component size**: The label width value does not automatically scale with the component size prop - you need to account for size scaling in your labelWidth values if you want consistent proportion across different sizes.

**Use cases**:
- **Consistent form layout**: Use labelWidth to ensure all labels have the same width across a form, creating visual alignment
- **Compact horizontal forms**: Use labelWidth to control label-to-field ratio in horizontal layouts
- **Responsive considerations**: LabelWidth values may need adjustment for different breakpoints

This prop is most useful when combined with labelPlacement=horizontal. When labelPlacement=vertical, applying this prop has minimal visual effect since the label already occupies the full width above the field.

Usage: `labelWidth="150px"`

## helperMessage

Brief explanatory text displayed below the combo-box field to provide guidance, instructions, or contextual information to users. The helper message appears inline (below the field) by default, but can be displayed as a tooltip by setting helperMessageAsTooltip=true. This is a content prop that provides supplementary information without affecting the component's behavior.

The helper message serves as additional context for users - it can explain what the combo-box is for, provide format instructions, or offer other helpful information. The message appears in a smaller/lighter font weight than the label to create visual hierarchy.

**Important interaction with validationState**: When a validationState is set (valid, warning, invalid), the helperMessage is overridden by the validation message. The validation message takes precedence and replaces any helperMessage content. This makes the combo-box's inline message area single-purpose - it shows either help guidance OR validation feedback, not both simultaneously.

**Visual presentation**: The helper message uses smaller font size and lighter font weight than the label, appearing below the combo-box field in a neutral color. The exact styling follows the design system's helper message patterns.

**Important interaction with helperMessageAsTooltip**: When helperMessageAsTooltip=true, the helper message is displayed as a tooltip instead of inline. This saves vertical space and shows the message only on hover/focus. When helperMessageAsTooltip=false (default), the message appears inline below the field, always visible.

**Important interaction with Multi-select and totalSelected**: In multi-select mode with totalSelected=true, the field displays "X selected" instead of individual option labels. The helper message appears below this count display as normal, providing guidance about what selections mean.

**Use cases**:
- **Field explanation**: Use helperMessage to explain what the combo-box is for and what the selected options represent
- **Format instructions**: Use helperMessage to provide guidance on selection requirements or constraints
- **Contextual help**: Use helperMessage to offer additional information that helps users make selections
- **Tooltip help**: Set helperMessageAsTooltip=true when you want to conserve vertical space or when the help is supplementary rather than essential

This prop is self-contained for content, but its display behavior depends on helperMessageAsTooltip and may be overridden by validationState.

Usage: `helperMessage="Select a status from the list"`

## helperMessageAsTooltip

When true, the helper message is displayed as a tooltip instead of being rendered inline below the combo-box field. This is a behavioral prop that affects how the helperMessage content is presented to users.

**Behavior differences**:
- **helperMessageAsTooltip=false (default)**: Helper message appears inline below the combo-box field, always visible, takes up permanent vertical space in the layout
- **helperMessageAsTooltip=true**: Helper message appears in a tooltip on hover/focus, saves vertical space, message only appears when users interact with the field

**Tooltip behavior**:
- Tooltip appears on hover for mouse users, on focus for keyboard users using the field
- Tooltip positioning defaults to "right" for mobile/smaller screens, can be customized via design system tooltip positioning
- Tooltip follows similar timing as other component tooltips (delay on open, delay on close)

**Important interaction with helperMessage**: The prop is dependent on helperMessage for content. It has no effect if helperMessage is not provided. The tooltip simply enables an alternative presentation method for the same helper message content.

**Important interaction with validationState**: This prop does not affect validation messages - those still display inline regardless of helperMessageAsTooltip. Validation messages always appear below the field to provide clear, immediate feedback about validation problems.

**Important interaction with Multi-select fields**: In multi-select mode, the tooltip behavior works the same - the helper message appears as a tooltip when helperMessageAsTooltip=true, whether the field shows individual labels or "X selected" count.

**Accessibility considerations**: Tooltip presentation can affect screen reader users differently than inline messages. Screen readers may announce tooltips differently, and keyboard users may need to interact with the field to see the tooltip. For critical information, consider keeping helperMessageAsTooltip=false (inline).

**Use cases**:
- **Space-constrained layouts**: Use helperMessageAsTooltip=true to save vertical space in dense forms
- **Supplementary help**: Use tooltip presentation when the helper message provides nice-to-have but not essential information
- **Essential guidance**: Use inline presentation (helperMessageAsTooltip=false) when users need to see the help guidance without interacting with the field
- **Touch interfaces**: Consider inline presentation for touch devices where hovering is less natural

This prop is behavioral and affects presentation method only. It depends on helperMessage for content and does not affect validation messages.

Usage: `helperMessageAsTooltip="true"`

## validationState

Controls the visual validation state of the combo-box field. Border colors are resolved via design tokens but dark-theme-specific tokens were not traced - only light theme tokens were documented from ds_tokens.css.

Values:
- `none`: No validation state (default), resolves to `#030f26` via `ion-cont-color-role-light-neutral-900`
- `valid`: Valid state, resolves to `#2dc168` via `ion-lit-color-leonardo-base-positive`
- `warning`: Warning state, resolves to `#fe7f2a` via `ion-lit-color-leonardo-base-warning`
- `invalid`: Invalid state, resolves to `#c70000` via `ion-lit-color-leonardo-base-negative`

Usage: `validationState="valid"`

## validationMode

Controls when validation logic is executed and the validationState is updated. This is a behavioral prop that determines whether validation runs automatically based on user interaction or requires manual triggering. Unlike validationState (which sets the visual appearance), validationMode controls the timing of validation execution.

**Validation mode values and their behavior**:

- **none (default)**: No automatic validation occurs. The validationState must be set manually by application code. This is useful when you want complete control over when validation happens and when to display validation feedback.

- **onChange**: Validation runs on every value change. Each time the user selects a different option in the combo-box, validation logic executes and potentially updates validationState. This provides immediate feedback but may feel excessive if users haven't finished selecting or if they're typing for filtering.

- **onBlur**: Validation runs when the combo-box field loses focus (when user clicks away or tabs out). ValidationState is updated at that point. This provides feedback after the user has finished interacting with the field but before they move to the next element.

- **onSubmit**: Validation runs when the parent form submits. ValidationState is updated only at form submission time. This defers feedback until the submission moment, which is traditional for many form validation workflows.

**Important relationship with required**: The validationMode prop works in conjunction with the required prop. When required=true and validationMode is not "none", validation automatically checks whether the combo-box has a selected value. The component includes built-in validation logic for required fields:
- Required+validationMode=onChange: Checks if value is selected each time it changes
- Required+validationMode=onBlur: Checks if value is selected when field loses focus
- Required+validationMode=onSubmit: Checks if value is selected during form submission
- Required+validationMode=none: No automatic validation of required state

**Important relationship with validationState**: The validationMode prop controls WHEN validation runs, but validationState controls WHAT is displayed. After validation runs (whether automatically via validationMode or manually), the validationState prop is set to reflect the result. Separating timing (validationMode) from presentation (validationState) allows flexible validation workflows.

**Important interaction with combo-box filtering**: In combo-box, validationMode=onChange can be particularly sensitive because every keystroke for filtering triggers validation. This means if you have complex validation logic, it will run on every character typed. For combo-box with filtering, consider using validationMode=onBlur as the default unless you have specific reasons to use onChange - this prevents validation running repeatedly as users type.

**Messages**: When validation fails for required fields, the component automatically sets the helperMessage to "This field is required" (or localized equivalent). This message appears in the interface with the invalid validationState styling.

**Use cases**:
- **none**: When you want manual control over validation timing, or when validation requires server-side confirmation that you don't want to trigger on every interaction
- **onChange**: When you want immediate validation feedback for simple validation rules (e.g., required field), but consider the filtering behavior in combo-box
- **onBlur**: When you want to validate after the user has finished interacting with the combo-box field, avoiding excessive validation during typing/filtering
- **onSubmit**: When you want to defer all validation until form submission, traditional form validation approach

This prop is behavioral and does not have visual presentation on its own - it triggers validation logic that updates validationState. It works independently of other props but is commonly paired with required and validationState for complete validation workflows.

Values:
- `none`: No validation (default)
- `onChange`: Validate on value change
- `onBlur`: Validate on field blur
- `onSubmit`: Validate on form submission

Usage: `validationMode="onChange"`

## required

When true, indicates that the combo-box field must have a selected value before the form can be considered complete. This is a semantic/content prop that affects validation behavior and can trigger visual indicators (via necessityIndicator). The required prop itself does not enforce the selection - it marks the field as required, and validation logic checks compliance.

**Required behavior combinations with validationMode**:

- **required=true + validationMode=none**: The field is semantically required (marked in HTML), but no automatic validation occurs. Your application code must manually validate that the field has a selected value.
- **required=true + validationMode=onChange**: Automatic validation runs on each value change. In combo-box, this includes both selection changes AND text input changes during filtering. If the field is left empty (no selection), validationState is set to invalid with "This field is required" message. This can trigger validation on every keystroke during filtering.
- **required=true + validationMode=onBlur**: Automatic validation runs when the field loses focus. If the field is empty, validationState is set to invalid with "This field is required" message immediately after the user tabs out or clicks away.
- **required=true + validationMode=onSubmit**: Automatic validation runs during form submission. If the field is empty, validationState is set to invalid with "This field is required" message at submission time.
- **required=false**: The field is optional. No automatic validation ensures a selection is made. Users can submit the form whether or not they've made a selection.

**Visual indication**: The required prop works with necessityIndicator to visually signal to users that a field requires input:
- **required=true + necessityIndicator=requiredMarker (default)**: Displays an asterisk (*) next to the label
- **required=true + necessityIndicator=requiredLabel**: Displays "Required" text next to the label
- **required=true + necessityIndicator=optionalLabel**: Displays "Optional" text next to the label (even though field is marked required)
- **required=true + necessityIndicator=none**: No visual indicator appears despite field being semantically required

**Accessibility**: The required prop adds the aria-required="true" attribute to the combo-box field's input element, which is important for screen readers and assistive technologies. This helps users understand which fields are required before they attempt form submission.

**Important interaction with multi-select**: For multi-select combo-boxes (multiSelect=true), empty means no options selected (value=[]). If required=true, having zero selected options will fail validation. Having even one option selected satisfies the required condition.

**Important interaction with custom values**: For combo-boxes with allowCustomValue=true, empty means no selection AND no custom input. If a user types a custom value but doesn't select it (e.g., types something but blurs without entering), the required check typically sees this as empty unless the custom value has been committed through the combo-box's custom value logic.

This prop is content/semantic in nature but has behavioral effects when combined with validationMode and visual effects when combined with necessityIndicator.

Usage: `required="true"`

## necessityIndicator

Controls the visual indicator that signals to users whether the combo-box field is required or optional. This is a visual prop that adds visual cues (asterisk, text labels) next to the field's label to communicate necessity status.

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

**Important interaction with accessibility**: Screen readers read the necessity indicator along with the label. For example, with requiredLabel, they may announce "Country, Required, combo box, collapsed" or similar. this helps screen reader users understand the field's requirement status. However, the semantic meaning comes from the required prop and aria-required attribute, not just the visual indicator.

**Visual appearance**: The necessity indicator appears next to the label text, typically in the same font weight and size as the label, positioned after (or before) the label text. The indicator does not affect the label's color, size, or other styling properties.

**Use cases**:
- **requiredMarker (default)**: Most common pattern, familiar to users, minimal visual impact
- **requiredLabel**: More explicit for users who may not understand the asterisk convention, or when you want very clear verbal communication
- **optionalLabel**: Helps identify exceptions in mostly-required forms, reduces user confusion about which fields are truly optional
- **none**: When you want custom presentation through helperMessage or other UI elements, or to avoid visual clutter in dense forms

This prop is visual and does not affect the component's behavior - it only adds visual communication. However, its accuracy relative to the actual required prop affects user communication quality and accessibility.

Values:
- `requiredMarker`: Show required marker (default)
- `requiredLabel`: Show required label
- `optionalLabel`: Show optional label
- `none`: No indicator

Usage: `necessityIndicator="optionalLabel"`

## startEnhancer

Adds visual content (text, icon, or category icon) at the start of the combo-box field, positioned before the field's text input area. Enhancers provide additional context, affordance, or visual interest to help users understand the field's purpose. This is a visual prop that accepts an object configuration rather than a simple text value.

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

- **type="icon-button"**: Displays an interactive button with an icon at the start of the field. The value prop specifies the icon name to display on the button. The button is clickable and triggers the startEnhancerButtonClick event. This is useful for adding interactive functionality like opening a search dialog, picking from a list, or other actions. The button has its own hover and focus states and does not interfere with the combo-box's opening functionality.

- **type="category"**: Displays a category-colored icon at the start of the field. This appears similar to type="icon" but uses category color styling rather than default field color. The value prop specifies the icon name. Category colors provide visual differentiation for different types of content (e.g., red for negative/warning items, green for positive ones, etc.).

**Visual positioning**: The start enhancer appears to the left of the field's text input area, Inline with the field content. It maintains consistent vertical alignment based on the field's size (taller matching for larger sizes). The space allocated to the enhancer scales based on its type (icons take less space than text, category icons take similar space to regular icons).

**Icon sizing**: Icon-based enhancers (type="icon", "icon-button", "category") automatically scale based on the combo-box's size prop:
- **size=sm**: Icon size is 16px
- **size=md (default)**: Icon size is 24px
- **size=lg**: Icon size is 32px

**Accessibility**: For type="icon-button", you should provide an ariaLabel to ensure screen readers announce the button's purpose. For other enhancer types, the ariaLabel is optional but recommended for icons whose meaning may not be visually obvious.

**Important interaction with input filtering**: When disableEdit=false (users can type/filter), the text input area appears after the start enhancer. Users can still type to filter options, and the start enhancer remains visible as a permanent prefix. This is useful for numeric prefixes like "+91" where you want to always show the country code.

This prop is visual and does not affect the component's behavior (except type="icon-button" which adds a clickable button). It does not depend on other props for its appearance but interacts visually with the field's layout.

Usage: `startEnhancer="Search"`

## endEnhancer

Adds visual content (text, icon, or clickable icon-button) at the end of the combo-box field, positioned after the field's text input area and before the dropdown arrow icon. End enhancers provide additional functionality or affordance on the right side of the field. This is a visual prop that accepts an object configuration similar to startEnhancer but positioned differently.

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

- **type="icon-button"**: Displays an interactive button with an icon at the end of the field, before the dropdown arrow. The value prop specifies the icon name to display on the button. The button is clickable and triggers the endEnhancerButtonClick event. This is useful for adding actions like clearing the field, showing help, opening a dialog, or other contextual functionality. The button has its own hover and focus states and does not interfere with the combo-box's opening functionality.

**Visual positioning and layout**: The end enhancer is positioned between the field's text input area and the dropdown arrow indicator. It maintains consistent vertical alignment based on the field's size. When multiple end elements are present (clearButton, endEnhancer, dropdown arrow), they stack horizontally in this order from left to right: field text → clear button (if enabled) → end enhancer → dropdown arrow.

**Icon sizing and interaction**: Icon-based enhancers automatically scale based on the combo-box's size prop, identical to start enhancers:
- **size=sm**: Icon size is 16px
- **size=md (default)**: Icon size is 24px
- **size=lg**: Icon size is 32px

For type="icon-button", the interactive button includes proper focus and hover states, keyboard support (Enter key to activate), and accessibility attributes (role="button", aria-label).

**Important positioning relative to dropdown arrow**: The end enhancer appears before (to the left of) the dropdown arrow indicator. This means the dropdown arrow is always the rightmost interactive element at the end of the field. Users interact with end enhancers first, then see the dropdown arrow as an affordance for opening the options list.

**Use cases**:
- **Informational icons**: Add help icons, info icons, or status indicators that provide additional context
- **Action buttons**: Add buttons for common actions like "clear", "reset", "search", or other field-specific operations
- **Units/suffixes**: Add text suffixes like "USD", "items", "people" to indicate the type of content expected
- **Field-specific actions**: Add actions specific to the combo-box's purpose, like "add new" buttons when the combo-box is used for selection from a list that can be extended

This prop is visual and does not affect the component's behavior (except type="icon-button" which adds a clickable button). It is positioned independently of startEnhancer and positioned before the dropdown arrow indicator.

Usage: `endEnhancer="More"`

## clearButton

When true, displays a clear button (typically an X icon) inside the combo-box field that appears when the combo-box has a selected value and clears the selection when clicked. This is a behavioral/visual prop that conditional rendering and interaction behavior.

**Clear button behavior**:

- **clearButton=false (default)**: No clear button is displayed. Users cannot clear the combo-box's selection through this UI. If they want to deselect an option, they would need to select a different option (or your application code could clear the selection programmatically).

- **clearButton=true**: A clear button appears inside thecombo-box field when:
  1. The combo-box has a selected value (the value prop is not empty/null)
  2. The clear button position (after endEnhancer, before dropdown arrow) is available
  3. The combo-box is not disabled or read-only (button only appears in interactive state)

The clear button is only displayed when there's a value to clear. When no option is selected, the button remains hidden to avoid clutter.

**Clear button positioning**: The clear button appears in the end area of the field, positioned after endEnhancer (if any) and before the dropdown arrow indicator. When multiple end elements are present, they stack horizontally: field text → clear button (when value exists) → end enhancer → dropdown arrow.

**Clear button visual appearance**: The clear button displays as an X or close icon, scaled to match the combo-box's size (16px for sm, 24px for md, 32px for lg). The button appears only when the field has a selected value and disappears when the field is empty. The button has hover and focus states for proper interaction feedback.

**Clear button interaction**: Clicking the clear button:
1. Clears the combo-box's selection (sets value to empty/null or empty array for multi-select)
2. Triggers the valueChange event with empty value
3. Clears any validationState (resets to "none")
4. Hides the clear button itself (since there's no longer a value to clear)
5. Moves focus to the combo-box field for continued interaction

**Important interaction with confirmOnApply**: When confirmOnApply=true, the clearButton is not displayed even if clearButton=true is set. This is because confirmOnApply provides its own Clear button in the dropdown footer for multi-select confirmation scenarios. The two mechanisms don't mix - you use either clearButton (immediate clearing) OR confirmOnApply (confirmation workflow), not both.

**Important interaction with multi-select**: For multi-select combo-boxes (multiSelect=true), clicking the clear button clears ALL selections (sets value to empty array []). This is different from single-select where it only clears the one selected option.

**Important interaction with custom values**: For combo-boxes with allowCustomValue=true, clicking the clear button clears both any selected options AND any custom values that were entered. The field becomes completely empty.

**Keyboard accessibility**: The clear button is focusable via keyboard navigation (Tab key) and can be activated with Enter or Space keys. It has appropriate ARIA attributes for screen readers.

**Use cases**:
- **Quick reset**: Allow users to quickly clear their selection and start over
- **Form reset**: When you want users to be able to clear selections without leaving the field
- **User control**: Give users explicit control over clearing selections without needing to select a different option
- **Avoid in confirmation workflows**: Don't use clearButton when confirmOnApply=true, as the confirmation workflow provides its own Clear mechanism

This prop is behavioral (adds click interaction) and visual (conditionally displayed). It depends on having a selected value to appear and interacts with confirmOnApply for multi-select scenarios.

Usage: `clearButton="true"`

## placeholder

The text displayed inside the combo-box field when no option is selected. This is a content prop that provides guidance or context to users about what they should select. The placeholder appears in lighter styling than entered content to distinguish it as instructional text rather than actual selected value.

**Placeholder behavior and usage**:

- **No placeholder provided**: When no option is selected, the field shows empty space or displays nothing beyond the arrow icon. Users interact with an empty field, which may be disorienting if there's no guidance about what to select or type.

- **Placeholder provided (e.g., placeholder="Select a status")**: When no option is selected, the field shows "Select a status" in a lighter color/weight to indicate this is instructional text, not an actual selection. When an option becomes selected or a custom value is entered, the placeholder is replaced by the selected option's label or the entered text.

**Visual appearance**: The placeholder text is displayed using the CSS class ion-ds-field-text-placeholder with lighter styling (typically reduced opacity or lighter color) to visually differentiate it from actual selected content. The placeholder uses the same font family and size as selected content but with this visual distinction.

**Important interaction with disableEdit**: When disableEdit=true (users cannot type to filter), the placeholder still appears when no option is selected. The placeholder gives users guidance that they can select from the dropdown options. Users cannot type in the field to clear the placeholder - they must select an option from the dropdown.

**Important relationship with multi-select and totalSelected**: When multiSelect=true and totalSelected=true, the placeholder handling is more complex:
- When no options are selected (value=[]), the placeholder appears normally
- When one or more options are selected, totalSelected=true typically shows "X selected" instead of the individual labels, which replaces the placeholder display
- The placeholder only appears when truly no options are selected and no custom values have been entered

**Important relationship with custom values**: For combo-boxes with allowCustomValue=true, the placeholder disappears when users start typing their custom input. As soon as text is entered, the placeholder is replaced by the user's input text. If they then select an option or tab out without selecting, the placeholder may reappear if no value was committed.

**Important interaction with value change**: The placeholder automatically hides when the combo-box has any value (either selected option or custom value). If the value is cleared programmatically or via clear button, the placeholder reappears.

**Use cases**:
- **No placeholder**: Appropriate when the field's purpose is obvious from context or label, or when you prefer a cleaner, minimalist appearance
- **Simple instructional text (e.g., "Select")**: Common pattern for combo-boxes when users need basic guidance about what action to take
- **Contextual placeholder (e.g., "Choose a category")**: More specific guidance when the field's purpose may not be immediately clear
- **Format guidance (e.g., "DD/MM/YYYY")**: Less common for combo-boxes but could be used if the combo-box represents a structured format or validation pattern

**Accessibility**: The placeholder text is not announced by screen readers when the field is empty (typical HTML behavior for placeholder attributes). Instead, the field's label and helperMessage provide the primary accessibility description. The placeholder primarily serves sighted users as visual guidance about what to expect from the field.

This prop is content-only and does not affect the component's behavior. It is self-contained but its visual presentation is enhanced by multiSelect, totalSelected, and allowCustomValue functionality.

Usage: `placeholder="Select a status"`

## tabIndex

Controls the keyboard tab order and focusability of the combo-box field. This is an accessibility prop that determines whether the field can receive focus via keyboard navigation and in what order relative to other focusable elements.

**Tab index values and their behavior**:

- **tabIndex > 0** (e.g., tabIndex="1", tabIndex="2"): The field can receive keyboard focus and participates in the tab order. Fields with lower positive tabIndex values are focused first in the tab sequence. For example, if Field A has tabIndex="1" and Field B has tabIndex="2", users tab to Field A first, then Field B.

- **tabIndex="0"** (default): The field can receive keyboard focus and participates in the natural tab order determined by its position in the DOM. Fields with tabIndex="0" are tabbed to in the order they appear in the page, which is the default and recommended approach for most form fields.

- **tabIndex < 0** (typically tabIndex="-1"): The field is not focusable via tab key but can receive focus programmatically (e.g., via the focus() method). This is useful when you want to make a field focusable for programmatic interaction but not part of the normal keyboard navigation flow.

**Important default behavior**: When tabIndex is not explicitly set, the combo-box field uses the default value of 0, making it focusable and part of the natural tab order created by its DOM position. This is almost always the appropriate behavior for form fields.

**Important interaction with disableEdit**: For combo-box fields, keyboard interaction includes both focus navigation AND text input for filtering (when disableEdit=false). The tabIndex controls the focus order, but disableEdit controls whether keyboard typing is allowed. A field with tabIndex="0" but disableEdit=true can still be focused and navigated via keyboard, but users cannot type to filter.

**Accessibility implications**: The tab index affects keyboard navigation, which is critical for users who rely on keyboard navigation instead of mouse/touch. Managing tab order properly ensures that keyboard users can navigate through form fields in a logical, predictable sequence. Proper tab order is especially important for combo-boxes because they have rich keyboard interaction (arrow keys for navigation, typing for filtering, etc.).

**Important relationship with disabled and readOnly**: The combo-box field is only actually focusable and interactive when disabled=false and readOnly=false. Setting a positive tabIndex on a disabled or readOnly combo-box doesn't make it interactive - those props take precedence for interactivity.

**Important interaction with mobile/native mode**: On mobile devices where the combo-box may render in native mode (if configured), the tabIndex behavior may differ. Native HTML select elements have their own focus behavior that browsers control, which may override or interact with tabIndex settings differently than the custom implementation.

**Keyboard navigation in combo-box**: When a combo-box has focus, keyboard users can:
- Tab into and out of the field (controlled by tabIndex)
- Type to filter options (when disableEdit=false)
- Use arrow keys to navigate options when dropdown is open
- Use Enter/Space to open dropdown or select options
- Use Escape to close dropdown

**Recommended usage**: For most combobox form scenarios, do not explicitly set tabIndex and let it default to 0. Only adjust tabIndex when you have a specific reason to modify the default tab order (e.g., when you need to override a confusing automatic tab order, or when you're implementing a custom keyboard navigation workflow).

This prop is accessibility-focused and affects keyboard navigation. It does not affect the visual appearance or other behavior beyond focusability.

Usage: `tabIndex="0"`

## autoFocus

When true, the combo-box field automatically receives focus when the component loads or mounts. This is a behavioral prop that affects initial focus placement and can improve usability by placing focus where users are expected to start.

**Auto focus behavior**:

- **autoFocus=false (default)**: The combo-box does not automatically receive focus when the component loads. Focus remains where it was before component mounted (typically not in the combo-box). Users must click or tab to the combo-box to interact with it.

- **autoFocus=true**: The combo-box field receives focus immediately when the component loads, before any user interaction. This calls the browser's focus() method on the combo-box's input element programmatically, making it the currently focused element. Users can immediately interact with the combo-box without needing to click or tab to it first.

**Browser behavior differences**: The autoFocus prop wraps the HTML autofocus attribute and calls the focus() method. Different browsers may handle autofocus differently:
- Most browsers properly autofocus the first element with autoFocus=true
- Some browsers require user interaction before allowing programmatic focus
- The component tries different approaches to ensure cross-browser compatibility

**Important relationship with multiple elements**: When multiple form elements all have autoFocus=true, only one will actually receive focus - typically the first one encountered by the browser. You should not set autoFocus=true on multiple elements in the same view as this creates unpredictable behavior.

**Important relationship with validation and combo-box filtering**: If the combo-box requires immediate validation (e.g., a required field that should be filled first), autoFocus=true can ensure that users start with the most important field. However, this can also be disorienting if focus unexpectedly jumps. For combo-boxes, this also means users are immediately in typing mode (if disableEdit=false), so they can immediately start filtering options.

**Important interaction with mobile**: On mobile devices where the combo-box may render as a native select or full-screen drawer, autoFocus behavior may differ. Some mobile browsers may show virtual keyboard immediately, while others may wait for user interaction. The exact behavior depends on the mobile browser and implementation.

**Accessibility considerations**: Auto focus can be helpful (users immediately land on the element they need to interact with) but also potentially disruptive (focus jumps without user control). For accessibility, consider whether auto focus truly improves user experience or creates confusion. Screen reader users may expect focus to start at the top of the page or content, not jump to a form field. WCAG guidelines specifically caution against changing focus without user preparation.

**Important interaction with component lifecycle**: autoFocus only triggers when the component initially mounts. If the combo-box conditionally unmounts and remounts (e.g., in a v-if or *ngIf condition), autoFocus will trigger again when it remounts. However, if the combo-box stays mounted and only its props change, autoFocus won't trigger again.

**Use cases**:
- **Dialog/modal forms**: Set autoFocus=true on the most important field so users can immediately start interacting
- **Single-field dialogs**: Set autoFocus=true on the only field to save users a click
- **Sequential data entry**: Set autoFocus=true on the first field in a multi-step form
- **Search boxes**: Set autoFocus=true on search combo-boxes so users can immediately type to find items
- **Avoid in most cases**: Let users control focus flow by clicking/tabbing naturally

This prop is behavioral and does not affect visual appearance. It is self-contained but may be affected by browser behavior and should not be used on multiple elements in the same view.

Usage: `autoFocus="true"`

## name

Sets the HTML name attribute for the combo-box field, which is important for form submission. The name attribute identifies the field when the form is submitted, allowing server-side code to associate submitted data with specific form elements. This is a content/behavioral prop that's critical for form data handling.

**Name behavior and usage**:

- **name not set (or empty string)**: The combo-box is still functional for interaction, but if it's part of a form that submits via standard HTML form submission, the combo-box's value won't be included in the submitted data (or may be included with an empty name). This may be acceptable when using AJAX submission or when the combo-box value is obtained programmatically rather than through form submission.

- **name set (e.g., name="country")**: The combo-box includes name="country" in its underlying input element, and when the parent form submits, the selected value is sent as country=value (where value is the selected option's value or custom value). This allows server-side code to access the combo-box's value via the name attribute.

**Form submission behavior**: When using standard HTML form submission (not AJAX or custom submission), the browser automatically includes the name-value pair for all form elements with:
1. A name attribute set
2. A non-empty value (selected option or custom value)

The combo-box component properly integrates with this behavior by setting the name attribute on its underlying input element.

**Multi-select naming in form submission**: When multiSelect=true, the combo-box's value is an array of selected values. Standard HTML form submission handles this by submitting multiple name-value pairs with the same name attribute. For example, if name="colors" and ["red", "blue"] are selected, the form submission includes: colors=red&colors=blue. Server-side code can access this as an array for the "colors" field.

**Important relationship with custom values**: For combo-boxes with allowCustomValue=true, the value submitted via the name attribute includes both selected options AND custom values that users have entered and committed. If a user types "Custom Color" and it's committed as a value, the form will submit colors=Custom+Color (URL-encoded) along with any selected standard options.

**Important relationship with value change events**: The name prop is included in the valueChange event payload, specifically as the name property in IDropdownValueChangeEventArgs. This allows your event handler to identify which combo-box fired the event, which is useful when you have multiple combo-boxes sharing the same event handler.

**Important interaction with empty states**: When the combo-box has no selected value and no custom value:
- In single-select: No value is submitted for that field (or it may submit as an empty string depending on server configuration)
- In multi-select: No name-value pairs are submitted (empty array)

**Accessibility and debugging**: The name attribute doesn't directly affect accessibility but can help with debugging form submissions, since you can see which named values correspond to which fields in browser developer tools. It also helps with form serialization libraries that rely on name attributes.

**Use cases**:
- **Standard form submission**: Set name when using traditional HTML form submission with server-side processing
- **AJAX serialization**: Set name so form serialization libraries can properly include this field's value
- **Multiple combo-boxes**: Use different names for each combo-box to distinguish values in submission
- **Array notation**: Use names like "colors[]" or colors[0], colors[1] pattern if your backend expects array format

**Code examples**:
```typescript
// Simple naming
name="country" // Submits as: country=us

// Multi-select naming
name="colors" // Submits as: colors=red&colors=blue&colors=green

// Array notation (some servers expect this)
name="user interests[]" // Submits as: user interests[]=tech&user interests[]=design

```

This prop is important for form submission behavior and event handling. It doesn't affect visual appearance or interaction behavior beyond form submission and event identification.

Usage: `name="status"`

## ariaLabel

Provides an accessible label for screen readers when the standard label prop is not sufficient or available. The aria-label attribute is read aloud by screen readers to identify the combo-box field to users who cannot see it visually. This is an accessibility prop that ensures users with visual impairments understand what the combo-box is for.

**ARIA label behavior**:

- **ariaLabel not set (or empty string)**: Screen readers announce the combo-box's purpose based on the label prop (if available). For example, if label="Country", screen readers may say "Country, combo box, collapsed" or similar. This is usually sufficient for accessibility when a clear label is provided.

- **ariaLabel set (e.g., ariaLabel="Select your country of residence")**: Screen readers use this aria-label text instead of or in addition to the visual label. For example, screen readers would say "Select your country of residence, combo box, collapsed". This can provide clearer, more descriptive text than the visual label.

**Important relationship with label prop**: When both label and ariaLabel are provided, screen readers typically use the more specific ariaLabel value rather than repeating the visual label. The ariaLabel is intended for cases where the visual label is either insufficient for blind users or when you want to provide alternative text.

**Important interaction with label placement**: Whether the label appears above/beside the field (labelPlacement), the ariaLabel is always available for screen readers. Visual placement doesn't affect the accessibility label - screen readers always have access to the ariaLabel if provided.

**Use cases for ariaLabel**:

- **Different text for screen readers**: You may want screen readers to hear more descriptive text than what's visually shown. For example, label="Country" but ariaLabel="United States or Canada selection" for context specific to your application.

- **No visual label**: If the combo-box has no label prop (or the interface is minimal without explicit labels), ariaLabel provides the only accessibility identification for screen readers.

- **Icon-only fields**: If the combo-box uses only visual icons without text labels (e.g., in a toolbar or other compact interface), ariaLabel provides the text description for screen readers.

- **Helper context**: You can include additional context in ariaLabel that helps screen reader users understand the field's purpose but would be verbose visually. For example, "Country selection for shipping address - must be a US state or territory".

- **Dynamic accessibility**: When the combo-box's purpose changes based on application state, you can update ariaLabel to match the current purpose while keeping the visual label generic.

**Implementation note**: The component combines prop values for accessibility - the ariaLabelMessage getter in the TypeScript code shows that the a11y label is `ariaLabel || label + (necessityIndicator === "optionalLabel" ? " optional" : "")`. This means if ariaLabel is provided, it's used alone; otherwise the label is used with optional marker if configured.

**Important interaction with multi-select**: For multi-select combo-boxes, screen readers typically announce additional information like "combo box, multiple selection, expanded, 3 of 5 selected". The ariaLabel is announced before this additional state information, so it describes what the field is for while the browser announces the current state.

**Important interaction with disableEdit**: Whether disableEdit=true or disableEdit=false, the ariaLabel describes the field's purpose but screen readers will also announce the interaction capabilities (e.g., "you can type to search" vs "combo box collapsed").

**Accessibility impact**: ARIA labels are critical for accessibility. Screen reader users depend on accurate, descriptive ARIA labels to understand form fields. Without proper ARIA labels, screen reader users may not understand what the combo-box is for, may misinterpret its purpose, or may not know that they can type to filter options (when disableEdit=false).

**Best practices**:
- Keep ariaLabel concise but descriptive (avoid overly long text)
- Include the field's purpose, not just its appearance
- Consider the user's context when choosing ariaLabel text
- Update ariaLabel when the field's purpose changes dynamically
- Test with actual screen readers to ensure proper announcement

This prop is accessibility-focused and does not affect visual appearance. It is important for compliance with accessibility standards (WCAG) and ensuring usable experiences for screen reader users.

Usage: `ariaLabel="Status selection combo box"`

## value

The currently selected value(s) of the combo-box. This is a content prop that represents which option(s) are currently selected. The value prop can be set initially (controlled component) or updated via valueChange events (uncontrolled component). The prop handles both single-select, multi-select, and custom value scenarios automatically.

**Value behavior for single-select (multiSelect=false)**:

- **value type**: Accepts the actual value of the selected option (e.g., if option has value="us", then value="us"), OR a custom user-entered value (when allowCustomValue=true)
- **Empty state**: value=null or value=undefined or value="" means no option is selected and no custom value has been entered
- **Manual setting**: You can programmatically set the value to a different option, which updates the displayed selection and triggers the valueChange event
- **Event updates**: When users select an option or enter/confirm a custom value, the valueChange event fires with the new value, and you can update your bound value accordingly

**Value behavior for multi-select (multiSelect=true)**:

- **value type**: Expects an array of selected option values (e.g., if options "us" and "ca" are selected, then value=["us", "ca"]), OR an array that includes both selected options and custom values
- **Empty state**: value=[] (empty array) means no options are selected - not null/undefined which would be misinterpreted
- **Manual setting**: You can programmatically set the value to an array of selected values
- **Event updates**: When users select/deselect options or add/remove custom values, the valueChange event fires with the updated array, and you can update your bound value accordingly

**Value behavior with custom values (allowCustomValue=true)**:

- When allowCustomValue=true, the value can include values that don't exist in the options array - these are custom values entered by users
- Custom values are treated identically to predefined option values for purposes of value matching, display, and form submission
- If a custom value matches an option value exactly (same type and equality), the combo-box may treat it as that option rather than a distinct custom value

**Value normalization**: The component normalizes values internally to match the expected format for the current mode:
- If multiSelect=true and you provide a single value (not array), it's automatically converted to array: [value]
- If multiSelect=false and you provide an array, it automatically uses the last value in the array

**Value matching logic**: For value to match an option, the component uses a deep equality comparison helper. This means:
- Simple values (strings, numbers, booleans): Compared by value (us matches "us", 5 matches 5)
- Complex values (objects, arrays): Compared by structure and content (not reference). For example, {id: 1, name: "Smith"} matches an option with same structure and content, even if different object reference.

**Important interaction with filtering**: In combo-box, the value prop controls what's displayed in the field AND what's used for filtering. When users type to filter options:
- The input text is separate from the value prop until a selection is made
- Once an option is selected, the value prop updates to that option's value
- The input text then shows that option's label
- If allowCustomValue=true and user enters a custom value, that becomes the value prop

**Important relationship with defaultValue**: If defaultValue is provided and value is not initially set, the component uses defaultValue as the initial selection. Once users interact, value overrides defaultValue. This is useful for pre-filling a default selection that users can override.

**Important relationship with validation and required**: The required property checks whether the combo-box has a valid selected value. For multiSelect, a non-empty array is considered "has value". For single-select, any non-null/non-empty value is considered "has value". When allowCustomValue=true, any committed custom value also satisfies the required condition.

**Important interaction with disableEdit**: When disableEdit=true (cannot type users can only select from dropdown), the value can still be set programmatically and updated via dropdown selection. The value prop works the same regardless of disableEdit - the only difference is how users change the value (dropdown selection only vs. dropdown selection + typing for filtering/custom values).

**Code examples - single-select**:
```typescript
// Setting initial selection
value="us"

// Responding to selection change
onValueChange(event) {
  this.value = event.detail.value; // Gets selected value (e.g., "us")
  Event detail: { name: "country", value: "us" }
}

// Handling custom value
onValueChange(event) {
  this.value = event.detail.value; // Could be "custom-service" if user typed it
}
```

**Code examples - multi-select**:
```typescript
// Setting initial selections
value=["us", "ca", "mx"]

// Responding to selection changes
onValueChange(event) {
  this.value = event.detail.value; // Gets array of values (e.g., ["us", "ca"])
  Event detail: { name: "countries", value: ["us", "ca"] }
}

// Handle mix of options and custom values
onValueChange(event) {
  this.value = event.detail.value; // e.g., ["us", "ca", "custom-service"]
}
```

This prop is content/behavioral in nature and is essential for the combo-box's data model. It formats differently for single vs multi-select, handles custom values, and integrates with validation and events.

Usage: `value="approved"` or `value=["approved", "pending"]`

## defaultValue

Provides the initial selected value(s) for the combo-box when the component first loads. Unlike value, which represents the current always-up-to-date selection, defaultValue has special behavior around initialization and history management. This is a content prop that's useful for pre-filling the combo-box, for browser history/caching scenarios, or for providing user-friendly starting points.

**Default value behavior and differences from value**:

- **defaultValue vs value**: The value prop always reflects the current selection, including all user interactions. The defaultValue prop provides an initial selection that can be overridden by user interaction and is also considered during browser history navigation (back/forward buttons), making it more suitable for scenarios where you want history awareness.

- **Interaction override**: When defaultValue is set and users don't interact, the combo-box shows the default selection. Once users select a different option (either from the dropdown or by entering a custom value), value overrides defaultValue and the user's selection persists.

- **Value initialization**: If both defaultValue and value are provided and value is empty/unset, defaultValue is used as the initial selection. This allows you to provide a default that users can override.

**Browser history integration**: The defaultValue prop has special behavior with browser history (back button navigation). When users navigate back to a page where they had previously interacted with the combo-box:
- History-aware forms treat defaultValue as the initial state before user interaction
- The browser may restore the form's previous state based on defaultValue
- This is different from value, which is treated as always-current user state

**Important interaction with custom values**: defaultValue can be set to a custom value (a value that doesn't exist in the options array). When allowCustomValue=true and defaultValue is set to a non-matching value:
- The combo-box initially displays the custom value in the field
- The custom value is treated as if the user had entered it
- If disableEdit=false, users can still filter/select other options
- If disableEdit=true, users cannot change the field except by selecting from the dropdown (assuming the custom value matches an option, shows no selection)

**Single-select default value**:
```typescript
// Pre-selecting "United States" on load
defaultValue="us"

// Pre-selecting with custom value (when allowCustomValue=true)
defaultValue="custom-service-not-in-options"
```

**Multi-select default value**:
```typescript
// Pre-selecting multiple options on load
defaultValue=["us", "ca", "mx"]

// Mix of options and custom values
defaultValue=["us", "custom-option-1", "ca"]
```

**Important relationship with required validation**: If defaultValue is set to a valid selection and the combo-box is required=true, then validation initially passes because the field is not empty. This is useful for forms where you want a required field to start with a valid selection (possibly a default like "Select one" or the most common option).

**Important interaction with filtering and disableEdit**:
- **disableEdit=false (allows typing)**: defaultValue appears initially. Users can type to filter and either select options OR enter custom values that override the default
- **disableEdit=true (cannot type)**: defaultValue appears initially but users cannot type custom values. They can only select from the dropdown options

**Important relationship with value and user interaction patterns**:
```typescript
// Correct pattern - don't update defaultValue after interaction
onValueChange(event) {
  this.value = event.detail.value; // Updates current selection
  // Don't do this: this.defaultValue = event.detail.value
}

// defaultValue stays constant as the initial state
// value always reflects the current, possibly-override state
```

**Common use cases**:
- **Form pre-population**: Set defaultValue when you want the combo-box to start with a reasonable selection for user convenience (e.g., most common country, default status)
- **Profile loading**: Load user's previously saved selection as defaultValue so it's their starting point (though value is typically used for this pattern)
- **Survey/templates**: Set default selections for templates that users can customize - defaultValue represents the template default
- **History preservation**: Use defaultValue instead of value when you want browser history awareness and better back/forward navigation behavior
- **User-friendly starting point**: When most users will select the same option, save them time by pre-selecting it but allow them to change if needed
- **A/B testing**: Set different defaultValues for different user segments and measure which leads to better completion rates

**Code example - using defaultValue properly**:
```typescript
// Combobox component
defaultValue: string = "proposal"; // Initial default value
value: string = ""; // Current value (empty by default)

// When component loads:
// - defaultValue="proposal" sets initial state
// - value="" means user hasn't interacted yet
// - Field shows "Proposal" as selection

// After user selects "Approved":
// - value becomes "approved"
// - defaultValue remains "proposal"
// - Back button would restore to defaultValue context
```

**Important behavior difference from value**:
- **value**: Always reflects current user state, overrides defaultValue after interaction, not used for browser history
- **defaultValue**: Initial state before interaction, preserved for browser history navigation, not updated after user changes selection

**Code example - correct usage**:
```typescript
// Don't update defaultValue after user interaction
// Instead update value when valueChange fires
onValueChange(event) {
  this.value = event.detail.value; // Updates current selection
  // Don't update: this.defaultValue = ... (this defeats the purpose)
}
```

This prop is content-focused and provides initial state vs the current state represented by value. It has special behavior with browser history and is most useful for initialization scenarios and providing user-friendly starting points.

Usage: `defaultValue="approved"`

## options

The available options that users can select from in the combo-box. This is a content prop that defines the combo-box's option list, which can include simple options, grouped options, options with icons/descriptions, disabled options, and more. The options prop is central to the combo-box's data model, filtering behavior, and user interface. For combo-box specifically, options also support dynamic loading based on user input.

**Options structure types**:

The options prop accepts multiple different structures to accommodate different data models and loading strategies:

1. **Basic IDropdownOption array** (static):
```typescript
[
  { value: "us", label: "United States" },
  { value: "ca", label: "Canada" },
  { value: "mx", label: "Mexico" }
]
```

2. **Mixed options and groups (IDropdownItem array)** (static):
```typescript
[
  { label: "North America", items: [
    { value: "us", label: "United States" },
    { value: "ca", label: "Canada" }
  ]},
  { value: "uk", label: "United Kingdom (ungrouped)" },
  { value: "mx", label: "Mexico" }
]
```

3. **Function returning options** (dynamic):
```typescript
() => [
  { value: "us", label: "United States" },
  { value: "ca", label: "Canada" }
]
```

4. **Synchronous function with query parameter** (filtering):
```typescript
(query: string) => {
  if (!query) return allOptions;
  return allOptions.filter(opt => opt.label.toLowerCase().includes(query.toLowerCase()));
}
```

5. **Async function returning Promise with options** (remote):
```typescript
async (query: string) => {
  const response = await fetch(`/api/countries?q=${query}`);
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
- **Options with descriptions**: Option label with secondary description below, provides additional context for selection decisions
- **Options with enhancers**: Text prefix or icon before the option label, visually differentiates grouped or categorized options
- **Disabled options**: Options appear grayed/unclickable and cannot be selected, useful for unavailable but relevant options (e.g., "Out of stock" items)
- **Grouped options**: Options organized under headers with optional group icons, useful for large option sets (50+ items)
- **Mixed listing**: Combination of grouped and ungrouped options (grouped items appear first, then ungrouped items)

**Virtual scrolling behavior**: Large option lists (≥15 items, as defined by Static_Options_Virtualization_Threshold) automatically enable virtual scrolling for performance. This applies to both static arrays and function-returned options. Virtual scrolling efficiently renders only visible options regardless of total count, which is especially important for combo-box where options may be filtered dynamically.

**Important for combo-box - dynamic options with filtering**: Unlike dropdown, combo-box supports query-based dynamic options where the options function receives the user's search query:
```typescript
// Query-based dynamic options for combo-box
options = async (query: string): Promise<IDropdownOption[]> => {
  // query is what user typed for filtering
  const response = await fetch(`/api/countries?q=${encodeURIComponent(query)}`);
  return response.json();
}
```

In this pattern, the combo-box calls the options function each time the user types (with loadThrottle debouncing), passing the current input as the query parameter. This allows server-side filtering where the remote API returns filtered results rather than the combo-box filtering locally.

**Important interaction with filterMode**: When options are provided as a function with query parameter, the combo-box's built-in filtering (controlled by filterMode, filterKeys, caseSensitiveFilter) typically doesn't apply. Instead, the combo-box assumes the options function handles filtering based on the query parameter. When options are provided as static arrays, the combo-box applies its built-in filtering.

**Important interaction with loadThrottle**: For async options functions, loadThrottle controls the debounce timing. The combo-box waits `loadThrottle` milliseconds after each character typed before calling the options function. This prevents excessive API calls while users are typing. The default is 300ms.

**Important interaction with loading prop**: When options are loaded asynchronously, the loading prop should be set appropriately to show loading state while the async operation completes. The combo-box may automatically set loading based on the async function state, but manual loading state management can ensure better UX.

**Updating options dynamically**: The options prop can be reactive - when the source data changes, the combo-box updates its option list. For arrays, this means assigning a new array reference. For functions, the function re-executes and returns updated options. In combo-box, when users type, the function is re-called with the updated query.

**Code examples - different option patterns**:

```typescript
// Simple static options (common for combo-box)
options = [
  { value: "us", label: "United States" },
  { value: "ca", label: "Canada" },
  { value: "mx", label: "Mexico" }
]

// Options with descriptions (helpful for selection decisions)
options = [
  { value: "us", label: "United States", description: "USA headquarters" },
  { value: "ca", label: "Canada", description: "Canadian operations" }
]

// Options with icon enhancers (visual differentiation)
options = [
  { value: "us", label: "United States", startEnhancer: { type: "icon", value: "flag_us" } },
  { value: "ca", label: "Canada", startEnhancer: { type: "icon", value: "flag_ca" } }
]

// Grouped static options (useful for 50+ items)
options = [
  { label: "Americas", items: [
    { value: "us", label: "United States" },
    { value: "ca", label: "Canada" }
  ]},
  { label: "Europe", items: [
    { value: "uk", label: "United Kingdom" },
    { value: "fr", label: "France" }
  ]}
]

// Dynamic options without query (refresh-on-open pattern)
options = async () => {
  const response = await fetch('https://api.example.com/countries');
  return response.json();
}

// Dynamic options with query (combo-box filtering pattern)
options = async (query: string): Promise<IDropdownOption[]> => {
  const response = await fetch(`https://api.example.com/countries?q=${encodeURIComponent(query)}`);
  return response.json();
}

// Dynamic options with query and custom filtering parameters
options = async (query: string): Promise<IDropdownOption[]> => {
  const response = await fetch(`https://api.example.com/countries?q=${encodeURIComponent(query)}&limit=50&active=true`);
  return response.json();
}

// Mixed static + dynamic pattern (show recent + dynamic results)
options = (query: string): IDropdownOption[] | Promise<IDropdownOption[]> => {
  if (!query) {
    // Return recent selections when no query
    return this.recentSelections;
  }
  // Fetch remote results when user types
  return this.fetchRemoteOptions(query);
}
```

**Important behavior with allowCustomValue**: When allowCustomValue=true, users can enter values that don't exist in options. The options array still controls what appears in the dropdown, but custom values entered by users can also be selected and stored. This is useful when you want to provide suggested options but allow flexibility.

**Important interaction with refreshOptions method**: The combo-box provides a refreshOptions() method that can be called programmatically to reload options. For static arrays, this re-processes the array. For function options, it re-calls the function to get updated options. This is useful when you need to trigger an options refresh from outside the combo-box.

**Important consideration for large datasets**: For very large datasets (thousands of options):
1. Use function-based dynamic options with query parameter for server-side filtering
2. Enable virtual scrolling (automatically enabled for 15+ items if disableVirtualScroll=false)
3. Consider groupMaxSelection limits when using grouped options
4. Test performance with your actual data size

**Virtual scroll and virtual scrolling control**: Virtual scrolling is automatically enabled for:
- Dynamic options (provided as a function)
- Static options with ≥15 items

You can override this with disableVirtualScroll true to prevent virtual scrolling even when it would normally be auto-enabled.

This prop is content-focused and central to the combo-box's functionality. It can be structured in various ways to accommodate different data models, display patterns, and data loading strategies - with combo-box supporting query-based dynamic options for remote filtering scenarios.

Usage: `options="statusOptions"` or `options="loadStatusOptions"`

## loadThrottle

Debounce timing in milliseconds for dynamic option loading. Controls how long the combo-box waits after the user types before calling the async options function. This prevents excessive API calls while users are still typing their search query. This is a behavioral prop specifically relevant for combo-boxes with dynamic options (function-based options).

**Load throttle behavior**:

- **loadThrottle not set (defaults to 300ms)**: The combo-box waits 300 milliseconds after the last keystroke before calling the options function. As the user types, each keystroke resets the 300ms timer. The options function is only called once the user pauses typing for 300ms. This is a balance between responsiveness and efficiency.

- **loadThrottle set to custom value (e.g., loadThrottle=500)**: The combo-box waits the specified number of milliseconds after the last keystroke before calling the options function. Higher values reduce API calls but make the combo-box feel less responsive. Lower values make the combo-box feel more responsive but may trigger excessive API calls.

- **loadThrottle set to 0 or very low**: The combo-box calls the options function immediately on each keystroke, effectively debouncing is disabled. This can result in one API call per character typed, which is very inefficient and can overwhelm servers and cause poor UX.

**How debounce works with loadThrottle**:
1. User types first character "u" → Timer starts (300ms by default)
2. User types second character "s" (23ms later) → Timer resets (now 300ms from "us")
3. User types third character "a" (89ms later) → Timer resets (now 300ms from "usa")
4. User stops typing → Timer expires after 300ms → Options function called with query="usa"

**Important relationship with options function type**: The loadThrottle prop only applies when options are provided as a function (dynamic options). For static array options, loadThrottle has no effect since there's no async loading - the combo-box filters locally using filterMode and related props.

**Important for remote vs local filtering**:

**Remote filtering** (options function with query parameter):
```typescript
// Remote filtering - server filters results
options = async (query: string) => {
  // Server receives query and returns filtered results
  const response = await fetch(`/api/countries?q=${encodeURIComponent(query)}`);
  return response.json();
}

loadThrottle = 300; // Controls how often API is called
```

**Local filtering** (static array + built-in filtering):
```typescript
// Local filtering - combo-box filters client-side
options = [
  { value: "us", label: "United States" },
  { value: "ca", label: "Canada" }
];

filterMode = "StartsWith"; // Controls HOW filtering happens
loadThrottle = 300; // Has no effect - filtering is local and immediate
```

**Important interaction with loading prop**: When options are loaded asynchronously and loadThrottle is active, the loading prop should be managed appropriately:
- Set loading=true to show loading state while waiting for options function to complete
- Set loading=false when options are returned
- The combo-box may handle loading automatically, but manual management gives better UX control

**Visual feedback during debounce**: Users typically see:
- While typing: No loading indicator (debounce hasn't expired yet)
- After debounce expires: Loading indicator appears while options function runs
- When results return: Options display in dropdown

This creates a subtle "thinking" pause that is more UX-friendly than showing/hiding loading on every keystroke.

**Performance considerations**:
- **300ms (default)**: Good balance for most use cases - responsive enough without overwhelming servers
- **500-700ms**: Better for slower servers or limited API quotas, but may feel sluggish to users
- **100-200ms**: More responsive for fast servers, but increases API call count
- **Avoid 0 or very low**: Immediate API calls on each keystroke create inefficient patterns

**Important interaction with network timing**: The loadThrottle controls WHEN the API call is made, but not HOW LONG the network request takes. Even with a short loadThrottle (e.g., 100ms), if the API takes 500ms to respond, users will still wait ~600ms total (100ms debounce + 500ms network). Conversely, even with a long loadThrottle (e.g., 700ms), if the API responds in 50ms, users only wait 750ms total.

**Use cases**:
- **Most remote APIs**: Use default 300ms for good balance
- **Rate-limited APIs**: Use higher value (500-700ms) to reduce API call frequency
- **Fast internal services**: Use lower value (100-200ms) for snappier response
- **Expensive operations**: Use higher value (500-1000ms) when each API call is computationally expensive or charges per call

**Code example - configuring for expensive API**:
```typescript
// API is expensive and has rate limiting - use higher throttle
loadThrottle = 700;

options = async (query: string) => {
  const response = await fetch(`/api/expensive-search?q=${query}`);
  return response.json(); // Each call costs money or time
}
```

**Code example - debouncing example**:
```typescript
// User types: "u n i t e d   s t a t e s" over 2 seconds
// With loadThrottle=300:

// Types "u" -> timer starts at 300ms
// Types "n" at 50ms -> timer resets to 300ms
// Types "i" at 150ms -> timer resets to 300ms
// ... continues ...
// Types last character -> timer resets one final time
// User stops typing -> timer expires at 300ms
// Options function called once with full query="united states"

// Result: Only 1 API call for entire typing sequence
```

This prop is behavioral and affects async option loading timing. It only applies to function-based dynamic options and doesn't affect static arrays or local filtering scenarios.

Usage: `loadThrottle="500"`

## dropdownWidth

Controls the width of the dropdown panel/menu that appears when the combo-box opens. This is a visual prop that determines how wide the options list is displayed, independent of the field's width. For combo-box, this is particularly important because the dropdown may show options with labels that are longer than the field's text area.

**Dropdown width behavior**:

- **dropdownWidth="auto" (default)**: The dropdown panel inherits the width of the combo-box field itself. The panel appears with the same width as the field, creating visual alignment. This is the most common behavior and creates a cohesive appearance where the options list matches the field width.

- **dropdownWidth="none"**: The dropdown panel uses its content-based width rather than inheriting the field's width. The panel expands or contracts to fit the widest option's content, potentially wider or narrower than the field. This can be useful when options are very long or very short and you want them displayed without truncation or excessive whitespace.

- **dropdownWidth="custom CSS width" (e.g., "300px", "80%", "20rem")**: The dropdown panel has the specified custom width, regardless of the field's width. This allows you to:
  - Make the panel wider than the field (e.g., dropdownWidth="600px") when options are very long and need more horizontal space
  - Make the panel narrower than the field (e.g., dropdownWidth="200px") for compact display
  - Use percentage-based widths (e.g., dropdownWidth="80%") relative to viewport or container
  - Use responsive units (e.g., dropdownWidth="clamp(200px, 50vw, 400px)") for adaptive width

**Important relationship with field width**: The dropdownWidth specifically controls the panel/menu width, not the field width. The field's width is controlled by the containing layout and any width constraints on the combo-box component. The dropdownWidth applies to the floating/popover content that appears when the combo-box is opened.

**Important consideration for combo-box filtering**: In combo-box, when users type to filter options:
- filtered options may be shorter/longer than the field's current value
- The dropdownWidth determines how much horizontal space is available for displaying those filtered option labels
- Wider dropdownWidth allows more space for long option labels to be displayed without truncation

**Visual positioning and alignment**: Regardless of the dropdownWidth, the panel is typically aligned with the field. When dropdownWidth="auto", the panel aligns with the field edges because they match in width. With custom widths, the panel may extend beyond (wider) or be contained within (narrower) the field's horizontal space.

**Interaction with long options**: If options are very long and dropdownWidth is narrow:
- Auto width (="auto"): Field must be wide enough to accommodate longest option, or truncation may occur in both field and dropdown
- None width (="none"): Panel expands to fit content, possibly wider than field
- Custom width: Set a width that accommodates your content needs

**Important interaction with multi-select and tags**: In multi-select combo-boxes, filtered options appear alongside already-selected items (tags may or may not be visible depending on disableTags). The dropdownWidth affects how much horizontal space is available for both the filtered options list and any tag display within the dropdown panel.

**Important interaction with optionTemplate**: If you're using custom optionTemplate that renders complex UI, the dropdownWidth needs to be wide enough to accommodate your custom layout without horizontal scrolling or squished content.

**Use cases**:
- **Aligned appearance (="auto")**: Most common, creates cohesive field+panel alignment
- **Content-driven width (="none")**: Let content determine panel width to avoid truncation, especially for combo-box where option labels may be longer than field content
- **Wider than field**: When field is narrow but options are long and need horizontal space - common in combo-box where field shows short selected text but available options have longer descriptions
- **Narrower than field**: When you want compact panel display even in wide fields
- **Responsive width**: Use percentage or viewport units for adaptive sizing based on screen size

**Code examples for combo-box**:
```typescript
// Common combo-box use case - field shows short value but options have long labels
dropdownWidth = "400px"; // Wider than field for full option labels
// Example: Field shows "US", but dropdown shows "United States of America (North America)"

// Auto width matches field - if field is wide enough for long options
dropdownWidth = "auto";

// Let content determine width - best for maximum label visibility
dropdownWidth = "none";

// Responsive combo-box for different screen sizes
dropdownWidth = "clamp(300px, 60vw, 600px)"; // Responsive width
```

**Important consideration for mobile**: On mobile where combo-box may open as full-screen drawer, dropdownWidth typically has less effect since the drawer takes full viewport width. The drawer's internal layout handles width automatically.

This prop is visual and controls the dropdown menu/panel width independently of the field width. It affects the appearance and layout of the options list when the combo-box is opened.

Usage: `dropdownWidth="300px"`

## dropdownHeight

Controls the height behavior of the dropdown panel/menu. This is a visual prop that determines how the dropdown panel's height is calculated and displayed, particularly relevant for scrolling behavior with many options and for combo-box filtering scenarios where users may type to find specific options.

**Dropdown height behavior**:

- **dropdownHeight="default" (default)**: The dropdown panel has a calculated height based on typical dropdown behavior. This usually means:
  - Fixed or maximum height is set based on design system tokens (typically around 300px or similar)
  - Content beyond the calculated height scrolls vertically
  - Height is appropriate for the number of options but constrained to reasonable limits
  - For filtered results, height accommodates the number of matching options (up to the maximum)
  - Example maximum height might be 300px or similar design system value

- **dropdownHeight="full"**: The dropdown panel takes up more vertical space, often extending to a larger portion of the viewport. This is particularly useful for:
  - Displays where you want maximum visibility of options
  - Scenarios where users are expected to review many options during filtering
  - Desktop interfaces where more vertical space is available than mobile
  - Used in conjunction with virtual scrolling for very large option lists
  - For combo-box filtering, allows more filtered options to be visible at once

**Important relationship with virtual scrolling**: When virtualScroll=true (enabled automatically for option lists with ≥15 items), dropdownHeight="full" becomes especially relevant. The full height allows the dropdown panel to use more viewport height, which means:
- More options are visible without scrolling
- Virtual scrolling has more space to render options before they're out of viewport
- Performance benefits of virtual scrolling are maximized
- User can see more items at once when deciding what to select
- For combo-box filtering, more filtered options are visible per screen, reducing scrolling needed to find desired option

**Important relationship with combo-box filtering**: In combo-box, as users type to filter options:
- The number of visible options in the dropdown changes based on matching results
- dropdownHeight="default" shows up to its maximum height even if only 5 options match (may show empty space below)
- dropdownHeight="full" allows more vertical space for showing many matching options at once
- For large filtered result sets, "full" height significantly improves UX by showing more results per screen

**Important relationship with mobile presentation**: On mobile devices where the combo-box opens as a full-screen drawer, dropdownHeight="full" maximizes the available vertical space within the drawer (typically 75% of viewport height). This provides the best mobile experience for browsing and filtering options. On desktop native select fallback mode (if configured), this prop may have different behavior due to browser-controlled presentation.

**Scrolling behavior**: With dropdownHeight="default", the dropdown panel has a fixed/max height and scrolls internally when content exceeds that height. With dropdownHeight="full", the panel uses more vertical space and therefore:
- Less internal scrolling is needed for the same number of options
- Initial view shows more options at once
- Better visibility reduces the need to scroll through long lists
- For filtered results, more options are visible at once

**Visual presentation**: Height settings primarily affect the dropdown panel size, not the options themselves. Options are rendered at the same size regardless of dropdownHeight - just more or fewer are visible at once within the visible scroll area.

**Responsive consideration**: In some implementations, dropdownHeight may have different effects at different viewport sizes. For example, "full" height on mobile might use all available drawer space, while on desktop it might use a larger percentage of viewport.

**Important interaction with multi-select confirm footer**: In multi-select combo-boxes with confirmOnApply=true, the dropdown footer contains Apply/Clear buttons. dropdownHeight affects whether this footer is visible without scrolling:
- dropdownHeight="default": Footer may be below the fold (visible only after scrolling options)
- dropdownHeight="full": Footer typically visible near bottom without scrolling options first

**Use cases**:
- **Standard behavior (="default")**: Most combo-boxes use default height, which provides good balance of visibility and space efficiency
- **Maximum visibility (="full")**: When you want users to see as many options as possible, especially for very large option lists or when users filter frequently
- **Virtual scrolling synergy**: When virtual scrolling is enabled (≥15 items or dynamic options), "full" height provides the best performance and user experience
- **Filtering optimization**: For combo-box filtering, "full" height lets users see more filtered results at once, making filtering feel more responsive
- **Mobile optimization**: Full height in mobile drawer mode provides best mobile option browsing and filtering experience

**Code example for combo-box filtering**:
```typescript
// Combo-box with many options and frequent filtering
options = async (query: string) => {
  // Returns up to 1000 options when empty, fewer when filtered
  return await api.getCountries(query);
}

// Use full height so users can see more filtered results at once
dropdownHeight = "full";

// This makes filtering feel more responsive because users can
// see 15+ filtered options on one screen rather than scrolling
```

This prop is visual and affects the dropdown panel's height behavior and scrolling characteristics. It's particularly relevant for large option lists and works well with virtual scrolling, especially in combo-box filtering scenarios.

Values:
- `default`: Standard dropdown height (default)
- `full`: Full viewport height

Usage: `dropdownHeight="full"`

## loading

When true, indicates that the combo-box's options are currently loading or the component is in a loading state. This is a visual prop that typically displays a loading indicator/spinner to communicate to users that the dropdown is not yet ready for interaction. For combo-box, this is particularly relevant when using dynamic options (function-based) with async loading or when filtering triggers remote API calls.

**Loading behavior**:

- **loading=false (default)**: The combo-box displays normally and is fully interactive. Users can type to filter (if disableEdit=false), see the options, make selections, and interact with all combo-box functionality.

- **loading=true**: The combo-box appears in a loading state, typically with a spinner or loading indicator. The exact visual pattern depends on the design system implementation, but users should understand that the combo-box is not yet ready. This commonly appears when:
  - Options are being fetched asynchronously from an API
  - The combo-box is initializing and calculating options
  - The options data is being processed/calculated
  - A filtering operation is in progress and results are being fetched from a remote server

**Important relationship with dynamic options (function-based)**: The loading prop is most commonly used in conjunction with async options. When options are provided via a function that returns a Promise, the combo-box needs to show the loading state while the async operation completes. This is especially important in combo-box because each filtering operation may trigger a new async call.

**Important interaction with loadThrottle**: In combo-box, when users type to filter:
1. loadThrottle controls the debounce timer (e.g., 300ms waiting for typing to pause)
2. User types → timer starts/resets
3. Timer expires → options function is called
4. loading=true should be set while waiting for the Promise to resolve
5. Promise resolves/destroys → loading=false, results display

This sequence creates smooth UX where users see loading indicator after they stop typing, not on every keystroke.

**Impact on interaction**: When loading=true, the combo-box should be non-interactive or limited in interaction - users cannot see full options or select from them until loading completes. The visual loading state communicates this temporary unavailability. However:
- Users may still be able to type additional characters (updating the query)
- Typing while loading typically resets the debounce timer and cancels the previous pending request
- The combo-box may show the loading state in the dropdown panel area

**Implementation pattern for async combo-box loading**:
```typescript
// State management for loading
loading = false;

// Initialize async options with loading state
async loadInitialOptions() {
  this.loading = true;
  try {
    this.options = await this.fetchCountryOptions();
  } finally {
    this.loading = false;
  }
}

// Dynamic filtering with debouncing
options = async (query: string) => {
  // Called after loadThrottle (e.g., 300ms) expires
  this.loading = true;
  try {
    const data = await this.fetchCountryOptions(query);
    return data;
  } finally {
    // Ensure loading false regardless of success/failure
    this.loading = false;
  }
}
```

**Visual representation**: The exact appearance of the loading state depends on the design system, but typically includes:
- Visual loading indicator (spinner or loader icon) in the dropdown area
- Possibly placeholder text like "Loading..." or "Searching..." in the dropdown
- Non-interactive appearance in the dropdown panel
- Loading indicator may appear below the field or within the dropdown panel itself

**Important interaction with multi-select dropdown**: In multi-select combo-boxes, loading state affects the dropdown panel where users make selections. Already-selected values remain visible in the field, but the dropdown panel shows loading instead of available/filtered options until loading completes.

**Important interaction with disableEdit**: When disableEdit=true (users cannot type), loading primarily affects the dropdown panel showing available options. The field remains non-interactive for typing regardless of loading state. When disableEdit=false, loading affects both the input area and dropdown panel.

**Accessibility considerations**: When loading=true, the combo-box should have appropriate ARIA attributes to indicate loading state to screen readers. This helps users understand why the dropdown is temporarily unavailable. For example, aria-busy="true" or similar attributes may be used.

**Important best practice - debounce pattern**: For combo-box with async filtering, always manage loading state in try/finally:
```typescript
options = async (query: string) => {
  this.loading = true; // Show loading
  try {
    const results = await this.fetchOptions(query);
    return results;
  } finally {
    this.loading = false; // ALWAYS hide loading, even on error
  }
}
```

This prevents loading state from getting stuck if errors occur.

**Use cases**:
- **API-driven options**: Show loading state while fetching initial options from server
- **Filtering async operations**: Show loading during combobox filtering when options function makes remote API calls
- **Async data processing**: Show loading state while calculating large/complex option lists
- **Initialization delay**: Show loading state during component setup when options aren't immediately available
- **Data refreshing**: Show loading state when refreshing options after user action or external event
- **Error handling**: Show loading state while retrying failed API calls

**Code example - complete async combo-box**:
```typescript
@Component({
  template: `
    <ion-combo-box
      label="Country"
      placeholder="Type to search countries"
      [options]="loadCountries"
      [loadThrottle]="300"
      [loading]="loading"
      [disableEdit]="false"
      (filteredOptionsLengthChanged)="onFilteredOptionsChange($event)">
    </ion-combo-box>
  `
})
export class AsyncComboBoxComponent {
  loading = false;

  // Dynamic options with query (for filtering)
  loadCountries = async (query: string): Promise<IDropdownOption[]> => {
    this.loading = true;
    try {
      const response = await fetch(
        `https://api.countries.com/search?q=${encodeURIComponent(query)}&limit=50`
      );
      const data = await response.json();
      return data.map(country => ({
        value: country.code,
        label: country.name,
        description: country.region
      }));
    } finally {
      this.loading = false;
    }
  };

  onFilteredOptionsChange(event) {
    console.log(`Found ${event.detail} matching countries`);
  }
}
```

This prop is visual and behavioral (affects interaction capabilities). It is most useful in async loading scenarios, especially in combo-box filtering where frequent async calls occur, and communicates temporary unavailability to users.

Usage: `loading="true"`

## headerElement

Allows injection of custom header content at the top of the dropdown panel, above the option list. This is a content prop that accepts either an IonElement function that returns an HTMLElement, or a raw string. This prop provides the ability to add custom content to the dropdown header for branding, instructions, or other UI elements. For combo-box, this is particularly useful for providing guidance about filtering behaviors or showing search context.

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

**Important relationship with combo-box filtering**: For combo-box where users type to filter options, the headerElement has special considerations:
- The header appears above all filtered results, providing context for the search
- Header content can guide users about how to filter or what they can type
- Header is visible even when no matching options are found (shows helpful "No results" or similar guidance)
- Header is a good place to show the current search query being used

**Important relationship with mobile presentation**: On mobile devices where the combo-box opens as a full-screen drawer, the headerElement appears at the top of the drawer, maintaining consistent positioning relative to the content.

**Content types and use cases for combo-box**:

**Text header (string format)**:
- Provides instructional text at the top of the dropdown
- Useful for context like "Type to search countries" or "Popular countries shown first"
- Serves similar purpose to helperMessage but appears inside the dropdown panel
- In combo-box filtering, can show guidance like "Type country name to filter" or "Search results for: {{query}}"

**Custom HTML header (IonElement function)**:
- Provides complete control over header content and styling
- Can include icons, buttons, links, or any HTML content
- Useful for advanced scenarios like custom search controls, filter buttons at panel top
- In combo-box, useful for showing search summary, filters, or advanced search UI with icons

**Important behavior with confirmOnApply and multi-select**: When confirmOnApply=true in multi-select mode and Apply/Clear buttons are shown, the headerElement positioning is adjusted to appear with proper spacing from these buttons (typically buttons appear at bottom, header at top), ensuring visual hierarchy is maintained.

**Specific combo-box use cases for headerElement**:

1. **Filtering guidance** for type-to-filter:
```typescript
headerElement = "Type to search countries (e.g., 'uni' for 'United States')";
```

2. **Search summary**:
```typescript
headerElement = () => {
  const query = this.currentSearchQuery;
  return query ? `Search results for "${query}"` : "All countries available";
}
```

3. **Custom search controls**:
```typescript
headerElement = () => {
  return this.advancedSearchHeader.nativeElement;
}
```

**Common header use cases**:

- **Instructions**: Add guidance like "Type name to filter" or "Select up to 5 regions"
- **Search indicator**: Show when search is affecting the displayed options in combo-box
- **Filters/controls**: Add sorting buttons, filter controls at panel top
- **Context**: Explain business rules or constraints relevant to the dropdown
- **Branding**: Include logos or branding elements in the dropdown
- **Search status**: Show "Searching..." when async filtering is in progress

**Code examples for combo-box**:

```typescript
// Simple text header
headerElement = "Type to search countries";

// Dynamic header based on search query
headerElement = () => {
  const query = this.currentFilterText;
  const count = this.filteredOptionsCount;
  if (query) {
    return `${count} results for "${query}"`;
  } else {
    return "All countries available";
  }
}

// Custom HTML header with filter controls
headerElement = () => {
  return this.customHeaderTemplate.nativeElement;
}

// Header with clear filter button
headerElement = () => {
  return `<div class="dropdown-header">
    <span>Search: ${this.currentQuery}</span>
    <button (click)="clearFilter()">Clear</button>
  </div>`;
}
```

**Important interaction with empty results**: In combo-box filtering, when no options match the search query, the headerElement remains visible while the options list shows "No results" or similar. This makes the header a good place to show helpful guidance about why no results were found and what users can do next (e.g., "No countries match - try a different search").

**Important behavior with dynamic options**: When options are loaded asynchronously (function-based options), the headerElement appears immediately while options are loading. You can use this to show "Loading..." or similar status text in the header area.

**Accessibility**: If headerElement contains interactive elements (buttons, links), ensure they have proper keyboard accessibility and ARIA attributes. The header content should be properly integrated into the dropdown's accessibility tree.

This prop is content-focused and allows custom header injection at the top of the dropdown panel. It works with the combo-box's filtering capabilities and provides flexible customization for header content.

Usage: `headerElement="headerTemplate"`

## footerElement

Allows injection of custom footer content at the bottom of the dropdown panel, below the option list. This is a content prop that accepts either an IonElement function, an HTMLElement, or a raw string. This prop provides the ability to add custom content to the dropdown footer for additional controls, information, or UI elements. For combo-box, this is particularly useful for providing additional search controls or showing filter summary information.

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

**Important relationship with combo-box filtering**: For combo-box where users type to filter options, footerElement is valuable for:
- Showing summary information about filtered results
- Providing additional search controls (e.g., "Advanced search" button)
- Displaying filter status or search parameters
- Showing tips for better filtering
- Providing actions like "Clear filters" when filtering is active

**Important relationship with mobile presentation**: On mobile devices where the combo-box opens as a full-screen drawer, the footerElement appears at the bottom of the drawer, providing a consistent footer position across desktop and mobile.

**Important relationship with confirmOnApply**: When confirmOnApply=true, Apply and Clear buttons appear in the dropdown footer area. If footerElement is also provided, the content is arranged to integrate properly with these buttons - typically the custom footerElement appears above the confirmation buttons, maintaining logical user interaction flow (footer content → Apply/Clear buttons).

**Content types and use cases for combo-box**:

**Text footer (string format)**:
- Provides instructional text or shortcuts at the bottom
- Useful for keyboard shortcut hints like "Press Enter to select"
- Can show context-specific guidance like "3 of 10 matching options shown"
- In combo-box filtering, can show search tips like "Type country name or code"

**Custom HTML footer (IonElement/HTMLElement)**:
- Provides complete control over footer content and styling
- Can include buttons, links, status indicators, charts, or any HTML content
- Useful for complex footers like additional search actions, filter controls, or summary displays
- In combo-box, useful for advanced search UI, filter chips, or search summary with visual indicators

**Specific combo-box use cases for footerElement**:

1. **Search summary** showing match count:
```typescript
footerElement = () => {
  const query = this.currentSearchQuery;
  const total = this.totalOptionsCount;
  const visible = this.filteredOptionsCount;
  if (query) {
    return `Showing ${visible} of ${total} - search: "${query}"`;
  } else {
    return `All ${total} countries available`;
  }
}
```

2. **Advanced search button**:
```typescript
footerElement = () => {
  return <button (click)="openAdvancedSearch()">Advanced Search</button>;
}
```

3. **Filter summary with clear button**:
```typescript
footerElement = () => {
  return `<div class="filter-summary">
    <span>Filter: ${this.currentFilter}</span>
    <button (click)="clearFilter()">Clear Filter</button>
  </div>`;
}
```

**Common footer use cases in combo-box**:

- **Keyboard shortcuts**: Show hints like "Type to filter, Enter to select" for power users
- **Additional actions**: Add search refinement buttons like "Search in more fields"
- **Status indicators**: Display search status, filter state, or search progress
- **Context information**: Provide details about filtering behavior or available options
- **Branding**: Include additional branding elements in the footer area
- **Filter management**: Show active filters with ability to clear them
- **Search summary**: Display "10 results found" or "All 195 countries shown"

**Code examples for combo-box**:

```typescript
// Simple text footer
footerElement = "Type country name to filter options";

// Dynamic footer based on search state
footerElement = () => {
  if (this.isLoadingResults) {
    return "Searching...";
  } else if (this.currentSearchQuery) {
    return `Found ${this.filteredOptionsCount} results for "${this.currentSearchQuery}"`;
  } else {
    return `All ${this.totalOptions} options available`;
  }
}

// Custom HTML footer with advanced search
footerElement = () => {
  return this.advancedSearchFooter.nativeElement;
}

// Footer with search tips
footerElement = () => {
  return `<div class="search-tips">
    <p>💡 Tip: Search by country name or 2-letter code</p>
  </div>`;
}
```

**Important interaction with empty results**: In combo-box filtering, when no options match the search query, the footerElement remains visible while the options list shows "No results". This makes the footer an excellent place for guidance like "No results found - try a different search term or clear filters."

**Important interaction with multi-select**: In multi-select combo-boxes, footerElement can display additional selection information like "3 selected" or selection summary, especially useful when used with confirmOnApply=true workflow.

**Important interaction with desktop vs mobile**: On mobile drawers, footerElement appears at the bottom of the drawer area. The same footer content appears consistently across both desktop popover and mobile drawer modes, which is valuable for search-related content that users need regardless of device.

**Accessibility**: If footerElement contains interactive elements (buttons, links), ensure they have proper keyboard accessibility. Users should be able to tab to footer elements and activate them with Enter/Space keys. The footer content should be properly integrated into the dropdown's accessibility tree.

**Performance consideration**: For dynamic footerElement functions that depend on filtered results or search state:
- The function may be called frequently in combo-box (on each keystroke)
- Avoid expensive calculations or API calls in footerElement function
- Cache expensive computations and update them separately
- Ensure footer rendering is fast and doesn't cause UI lag during typing

**Code example - efficient pattern**:
```typescript
// Efficient - calculate separately, footer just displays
effectiveFooterText: string = "";

updateFilteredResults(results: IDropdownOption[], query: string) {
  this.filteredOptions = results;
  this.currentQuery = query;
  // Calc once, reuse in footer
  this.effectiveFooterText = query
    ? `${results.length} results found for "${query}"`
    : `All ${this.totalOptions} options available`;
}

footerElement = () => this.effectiveFooterText;
```

This prop is content-focused and allows custom footer injection at the bottom of the dropdown panel. It's particularly valuable for combo-box search/filter scenarios and provides flexible customization for footer content.

Usage: `footerElement="footerTemplate"`

## multiSelect

When true, enables multiple option selection where users can select more than one option from the combo-box. This is a behavioral prop that fundamentally changes the combo-box's interaction model from single selection to multiple selection. For combo-box, this also affects how typed values (custom values) and selections are displayed and managed.

**Multi-select behavior and single-select differences**:

**Single-select (multiSelect=false, default)**:
- Only one option can be selected at a time
- Selecting one option automatically deselects the previously selected option
- Value is a single value (e.g., "us") not an array
- No selection limit by default (can select any one option)
- No multi-select-specific UI elements (checkboxes, apply/clear buttons)
- Custom values work with allowCustomValue=true, but only one custom value can be committed at a time

**Multi-select (multiSelect=true)**:
- Multiple options can be selected simultaneously
- Users can select or deselect options independently
- Value is always an array (e.g., ["us", "ca", "mx"]) even if only one or no items selected
- Selection limits can be controlled via maxSelection (total) and groupMaxSelection (per group)
- Multi-select UI elements appear: checkboxes within options, apply/clear buttons (if confirmOnApply=true)
- Custom values can be added alongside selected options when allowCustomValue=true
- Display behavior changes significantly based on disableTags, tagDisplay, totalSelected, separator

**Visual differences in multi-select**:

- **Checkboxes**: Each option displays a checkbox to indicate its selected state in the dropdown
- **Selection indication**: Selected options maintain visual highlighting and checked state  
- **Multi-select controls**: When enabled, additional UI elements appear:
  - Show Select All checkbox at top (if showSelectAll=true)
  - Clear and Apply buttons in footer (if confirmOnApply=true)
  - Selection display in field based on disableTags, tagDisplay, totalSelected settings

**Multi-select value handling**:
```typescript
// Initial state - no selections
value = []

// After selecting "US" and "CA"
value = ["us", "ca"]

// After deselecting "CA" but adding "MX"
value = ["us", "mx"]

// With custom values alongside selected options (allowCustomValue=true)
value = ["us", "custom-service-1", "ca"]
```

**Important interaction with disableEdit**: In multi-select combo-box:
- **disableEdit=false**: Users can type to filter/select options AND can type custom values (if allowCustomValue=true). Typing filters both existing options and allows entering new custom values
- **disableEdit=true**: Users cannot type to filter or enter custom values, but can select from dropdown options only. Useful when you want multi-select but no custom value entry

**Important interaction with disableTags in multi-select**:
- **disableTags=true**: Selected values appear as comma-separated text in the field (e.g., "United States, Canada" based on separator)
- **disableTags=false**: Selected values appear as removable chips/tags in the field. Each tag can be individually removed by clicking its X button. The field itself is still typeable for filtering additional options

**Important relationship with separator prop**: In multi-select mode, the separator prop controls how multiple selected value labels are joined when disableTags=true. For example, if separator=", " and value=["us", "ca"], the field displays: "United States, Canada"

**Important relationship with totalSelected**: When totalSelected=true, the field displays "X selected" count instead of individual labels (e.g., "3 selected" instead of listing three country names). This changes the display mode entirely.

**Important relationship with tagDisplay**:
- **tagDisplay="collapsed"** (default): Shows single row of tags with +N overflow indicator that expands to maxVisibleRows when clicked
- **tagDisplay="wrap"**: Allows tags to wrap to multiple rows within maxVisibleRows limit

**Important relationship with multi-select specific props**: Several props only have function when multiSelect=true:
- separator: Controls display string between selected option labels (when disableTags=true)
- totalSelected: Shows "X selected" count instead of listing labels
- showSelectAll: Displays Select All checkbox at top of dropdown
- confirmOnApply: Adds Apply/Clear buttons for confirmation workflow
- maxSelection: Limits total number of selections across all options
- groupMaxSelection: Limits number of selections per option group
- allSelectionValue: Custom text to show when all options selected
- disableTags: Controls whether selections show as tags or comma-separated text
- tagDisplay: Controls tag wrapping behavior (only relevant when disableTags=false)

**Important interaction with allowCustomValue**: When both multiSelect=true and allowCustomValue=true:
- Users can select multiple predefined options AND enter custom values
- Custom values go into the value array alongside selected options
- Custom values appear as tags (when disableTags=false) alongside selected option tags
- Custom values can be removed individually along with selected options

**Mobile experience changes**:
- **Without confirmOnApply**: Mobile multi-select works similarly to desktop - selections update immediately
- **With confirmOnApply**: Mobile shows full-screen drawer with Apply/Clear actions, requiring explicit confirmation (Apply) or cancellation (Clear)

**Desktop vs Native Mode**: On mobile where combo-box may render as native select (if configured), multi-select behavior may differ. Native HTML selects have limited multi-select UX - some browsers show a scrollable list with checkboxes, others use platform-specific multi-select patterns.

**Accessibility in multi-select**:
- Each option checkbox should be properly labeled and keyboard accessible
- Screen readers announce selection state for each option
- Total count announcements when selections change in "X selected" display mode
- Proper ARIA attributes for the multi-select state

**Code pattern - multi-select with typing disabled**:
```typescript
// Multi-select but users can only select from dropdown (no typing)
multiSelect = true;
disableEdit = true; // Only dropdown selection
disableTags = false; // Show tags for selected items
separator = ", "; // Not used since disableTags=false
maxSelection = 5; // Limit total selections
```

**Code pattern - multi-select with custom values**:
```typescript
// Multi-select allowing both option selection and custom value entry
multiSelect = true;
allowCustomValue = true;
disableEdit = false; // Allow typing
disableTags = false; // Show tags
// User can select "us" from dropdown AND type "custom-service" to add it
// Both go into value array: ["us", "custom-service"]
```

**Code pattern - multi-select with full controls**:
```typescript
// Full-featured multi-select
multiSelect = true;

// Selection management
maxSelection = 10;
groupMaxSelection = 3;
showSelectAll = true;

// Display control
disableTags = false;
tagDisplay = "wrap";
totalSelected = false; // Show individual tags
separator = ", "; // Used when disableTags=true or if structure changes

// Confirmation workflow
confirmOnApply = true;

// Custom display when all selected
allSelectionValue = "All countries selected";
```

This prop is behavioral and fundamentally changes the combo-box's interaction model. It activates and enables numerous multi-select-specific features that are not available in single-select mode, especially customizing how selections are displayed and managed within the combo-box field.

Usage: `multiSelect="true"`

## separator

Controls the text string used to join multiple selected option labels when displaying them in the combo-box field. This is a visual/content prop that only applies in multi-select mode (multiSelect=true) and particularly when disableTags=true, affecting how multiple selected values are formatted for display in the field.

**Separator behavior and usage**:

- **separator not set (defaults to ", ")**: Multiple selected option labels are joined with a comma and space, creating a readable list. For example, if options ["United States", "Canada", "Mexico"] are selected, the field displays: "United States, Canada, Mexico"

- **separator set to custom string**: Multiple selected option labels are joined with the provided string. This allows customization for different formatting preferences:
  - comma separator (", " - default): "United States, Canada, Mexico"
  - vertical bar separator (" | "): "United States | Canada | Mexico"
  - semicolon separator ("; "): "United States; Canada; Mexico"
  - dash separator (" - "): "United States - Canada - Mexico"
  - custom separator (" ◦ " or " // "): "United States ◦ Canada ◦ Mexico"

**Important relationship with multiSelect**: The separator prop only has an effect when multiSelect=true. In single-select mode, there's only one selected option, so no joining is needed and separator is ignored.

**Important interaction with disableTags**: The separator prop primarily applies in multi-select mode when disableTags=true. When disableTags=false, selected values appear as removable chips/tags instead of text with separator. The separator may still be used internally or for accessibility (screen reader announcements) but isn't visually displayed as text.

**Important relationship with totalSelected**: When totalSelected=true, the separator prop has no visual effect because instead of listing individual option labels, the field displays something like "3 selected" (the count instead of the values). The separator only applies when the field displays the actual option labels.

**Important interaction with custom values**: For combo-boxes with allowCustomValue=true and multiSelect=true, custom values are treated identically to selected options for grouping and display. Custom values appear in the same sequence as selected options and are joined using the same separator when disableTags=true.

**Visual presentation**: The separator is inserted between each option label when multiple selections are displayed in the field as text. The separator text itself appears in the same color/weight as the option labels, creating a cohesive visual appearance. The separator does NOT appear after the last item.

**Important role in accessibility**: Even when disableTags=false (using chips/tags), the separator may be used for screen reader announcements. Screen readers may announce selections as "United States, comma, Canada, comma, Mexico selected" or similar pattern, using the separator (or punctuation equivalent) to separate items in the announcement. This helps screen reader users understand individual selections vs. a mass selection.

**Mobile vs desktop behavior**: In mobile multi-select combo-boxes where the presentation may differ (full-screen drawer vs dropdown), the separator typically affects the field display consistently across devices - the field shows text with separator regardless of mobile presentation mode.

**Important guidance on separator choice**:
- **Clarity**: Choose separators that clearly distinguish individual items (", " is most universally understood)
- **Space considerations**: Include trailing space after separator for readability ("; " vs ";")
- **Avoid confusion**: Don't use characters that might appear in option labels themselves (e.g., if options contain commas, use different separator)

**Common issues when separator may not work as expected**:
- Option labels contain the separator character (creates ambiguity in parsing)
- Very long option names that make text display unwieldy regardless of separator
- Internationalization: Some languages expect different separator conventions

**Use cases**:
- **Standard comma separator (default)**: Most readable for general multi-select, follows standard English comma-separated list format
- **Vertical bar separator**: Visually creates distinct separation between options, useful for options where comma separation might be confusing (e.g., when option labels themselves contain commas)
- **Semicolon separator**: Alternative to comma when you want visual distinction from typical list formatting
- **Custom separators**: When your application has specific formatting requirement or brand guidelines
- **No separator ("")**: Creates concatenated appearance (not recommended as it's hard to parse visually)

**Code examples**:
```typescript
// Default behavior - comma separated
separator = ", "; 
// Field displays: "US, Canada, Mexico"

// Vertical bar separation  
separator = " | "; 
// Field displays: "US | Canada | Mexico"

// No separator (concatenates)
separator = ""; 
// Field displays: "USCanadaMexico" (hard to read!)

// Bullet appearance
separator = " ◦ "; 
// Field displays: "US ◦ Canada ◦ Mexico"

// Custom for technical data
separator = " + "; 
// Field displays: "US + CA + MX"
```

**Important troubleshooting**:
- If selections appear concatenated: Check separator is set correctly and has space
- If custom values cause display issues: Ensure separator doesn't conflict with custom value patterns
- If screen reader announcements sound unnatural: Separator choice affects announcements too

**Code pattern - debugging separator issues**:
```typescript
// If display looks wrong, check:
console.log('Separator:', this.separator);
console.log('Value array:', this.value);
console.log('Expected display:', this.value.map(v => labelMap[v]).join(this.separator));
```

**Important trick for long labels**:
When option labels are very long, the separator may not help readability much. In these cases, consider:
- Using totalSelected=true instead (shows count rather than listing all labels)
- Using disableTags=false with shortened tag display (may truncate long labels)
- Reducing maxVisibleRows with scroll overflow

This prop is visual/content-focused and only applies in multi-select mode. It affects how multiple selected values are formatted for display in the combo-box field, particularly when disableTags=true.

Usage: `separator=";"`

## totalSelected

When true and multiSelect=true, displays the count of selected options (e.g., "3 selected") in the combo-box field instead of listing all selected option labels. This is a visual prop that provides a condensed display for multi-select, especially useful when many options are selected and listing all labels would be unwieldy. For combo-box, this is particularly important given the ability to type custom values in addition to selecting options.

**Total selected behavior**:

- **totalSelected=false (default)**: The combo-box field displays the labels of all selected options, separated by the separator string (when disableTags=true) or as tags (when disableTags=false). For example, if options ["United States", "Canada", "Mexico"] are selected and separator=", ", the field displays: "United States, Canada, Mexico"

- **totalSelected=true**: The combo-box field displays a count of how many options are selected instead of listing the labels. For example, if 3 options are selected, the field displays "3 selected" or "3 selected" (localized). The exact text format follows the design system's localized strings.

**Important relationship with multiSelect**: The totalSelected prop only has an effect when multiSelect=true. In single-select mode, there's only ever 0 or 1 selected options, so a count display would be redundant ("0 selected" or "1 selected" simply conveys the same information as the blank field or single selection).

**Important interaction with disableTags**: When totalSelected=true, the disableTags prop becomes irrelevant for field display because labels are not being listed at all. The field shows "X selected" regardless of whether it would show tags or comma-separated text. However, when the dropdown is open, tags may still be displayed within the dropdown panel depending on disableTags setting.

**Important interaction with separator**: When totalSelected=true, the separator prop is ignored because no option labels are being joined. The field displays a single count string instead of formatted option labels.

**Important interaction with allSelectionValue**: When both totalSelected=true and allSelectionValue is set, the behavior varies based on whether all options are selected:
- **Not all options selected**: Shows "X selected" count (e.g., "3 selected")
- **All options selected**: Shows the custom allSelectionValue text instead of the count (e.g., "All countries selected" instead of "10 selected")

**Important behavior with custom values**: For combo-boxes with allowCustomValue=true and multiSelect=true, totalSelected counts both selected options AND custom values together as one total. If users selected "US" and "CA" from dropdown and entered "custom-service" as a custom value, totalSelected=true would show "3 selected" (not differentiating between options and custom values).

**Important role in combo-box filtering**: During combo-box filtering where users type to search options:
- totalSelected=true displays "X selected" count even when filtering is active
- The count remains accurate regardless of what filtering is currently showing
- Users see total number of selected items while they type to filter additional options
- This provides helpful context - they know how many items are already selected while searching for more

**Accessibility impact**: Screen readers will announce the count string instead of reading all individual labels when totalSelected=true. This may be more efficient for users with many selections but may reduce specific knowledge of what is selected. Consider the balance between efficiency and specificity when choosing between these display modes.

**Mobile experience**: On mobile devices where multi-select combo-boxes show full-screen drawer:
- totalSelected=true displays "X selected" in the collapsed field (same as desktop)
- The full-screen drawer typically shows all selected items (either as checked items or in a summary section) regardless of totalSelected setting
- This maintains consistency - users can see details in the dropdown/drawer while keeping the field compact

**Use cases**:
- **Many selections selected**: When dozens of options are selected, listing all labels is overwhelming - totalSelected=true provides cleaner display ("25 selected" instead of listing 25 country names or custom values)
- **Count-based summary**: When you need a count of selections for display purposes (e.g., "Selected 5 of 10 filters active")
- **Clean appearance**: When you want a more minimalist, less cluttered user interface
- **Filtering workflows**: When users need to see how many items are selected while still being able to search for/add more selections
- **Scalability**: When the number of potential selections is large but you display relatively few at a time

**Code pattern - counting for totalSelected**:
```typescript
// Without totalSelected (labels displayed)
value = ["us", "ca", "mx", "custom-service-1"];
// Field shows: "United States, Canada, Mexico, Custom Service 1"

// With totalSelected=true (count displayed)
totalSelected = true; 
value = ["us", "ca", "mx", "custom-service-1"];
// Field shows: "4 selected"
```

**Important pattern - combo-box with custom values**:
```typescript
// Custom values counted alongside options
multiSelect = true;
allowCustomValue = true;
totalSelected = true;

// User selects: "US" from dropdown + enters "custom-service" 
value = ["us", "custom-service"];
// Field shows: "2 selected" (doesn't distinguish option vs custom value)
```

**Code pattern - with allSelectionValue**:
```typescript
multiSelect = true;
totalSelected = true;
allSelectionValue = "All regions selected";

// When 3 of 10 selected:
value = ["us", "ca", "mx"];
// Field shows: "3 selected"

// When all 10 selected:
value = /* all 10 options */;
// Field shows: "All regions selected" (custom text)
```

**Important troubleshooting**:
- If count appears wrong: Check value array length (includes both options AND custom values)
- If dropdown shows different count: Dropdown may show all options selected vs. what's actually in value array
- If custom values aren't counted: Ensure allowCustomValue=true (custom values with false may not be committed to array)

**Code pattern - debugging totalSelected**:
```typescript
get totalDisplay(): string {
  if (!this.totalSelected || !this.value || !this.value.length) {
    return "Multi-select ready"; // empty state message
  }
  
  if (this.allOptionsSelected && this.allSelectionValue) {
    return this.allSelectionValue;
  }
  
  return `${this.value.length} selected`;
}
```

**Important guidance - when to use totalSelected**:
- **Use for**: Many selections (>5), fast workflow where individual labels matter less, filtering-heavy interactions
- **Avoid for**: Small number of selections where users need to see what's selected, cases where individual label identity is critical

**Best practice for combo-box with filtering**:
```typescript
// Recommended setup for filterable multi-select combo-box
multiSelect = true;
disableEdit = false; // Allow typing for filtering
totalSelected = true; // Show count instead of listing labels
tagDisplay = "wrap"; // Configure tags in dropdown (override count display)
// This provides clean field while allowing detailed tag interaction in dropdown
```

This prop is visual and only applies in multi-select mode. It dramatically affects how multiple selections are displayed in the combo-box field, providing a condensed display that scales well with many selections (including both options and custom values).

Usage: `totalSelected="true"`

## showSelectAll

When true and multiSelect=true, displays a Select All checkbox at the top of the dropdown menu above the option list. This checkbox allows users to select or deselect all options with a single click. This is a behavioral/visual prop that provides a convenient way to manipulate all selections. For combo-box this is particularly valuable given filtering capabilities - the Select All behavior adapts based on currently filtered options.

**Show Select All behavior**:

- **showSelectAll=false (default)**: No Select All checkbox is displayed. Users must select or deselect options individually.

- **showSelectAll=true**: A Select All checkbox appears at the top of the dropdown menu, above the first option group or option. The checkbox has three states:
  - **Unchecked**: All options are deselected (no options selected)
  - **Checked**: All selectable options are selected (every option that can be selected is selected)
  - **Indeterminate**: Some (but not all) selectable options are selected

**Important relationship with multiSelect**: The showSelectAll prop only has an effect when multiSelect=true. In single-select mode, "select all" is meaningless since only one option can be selected.

**Select All state logic**:
- When all selectable options (excluding disabled options) are selected → checkbox is checked
- When no selectable options are selected → checkbox is unchecked
- When some but not all selectable options are selected → checkbox is indeterminate (displayed as a dash/minus)
- Disabled options do not affect the Select All state - they are excluded from "all" calculations

**Important interaction with combo-box filtering**: In combo-box where users type to filter options, showSelectAll adapts its behavior:

**When no filter is active** (all options visible):
- Select All affects all options in the entire option list
- Clicking Select All selects every available option (up to maxSelection limit)
- Behaves identically to dropdown's showSelectAll

**When filter is active** (subset of options visible):
- Select All only affects the currently FILTERED (visible) options
- Clicking Select All selects only matching options shown in the dropdown
- This allows users to "select all matching items" rather than all options overall
- After clearing filter, the dropdown shows bothselected items from previous selections + can filter to different subsets

**Select All checkbox interaction**:
- **Clicking when unchecked**: Selects all selectable options currently visible (respecting maxSelection limit). In filtered state, selects all matching options. If maxSelection limits apply, Select All selects up to that limit from currently visible options.
- **Clicking when checked**: Deselects all options in the dropdown (no options selected)
- **Indeterminate state typically resolves to checked when clicked** (selects the remaining unselected options)

**Positioning**: The Select All checkbox appears at the very top of the dropdown menu, before any option groups or individual options. It's visually distinct from regular options (typically has a different background and contains text like "Select All" or localized equivalent).

**Important interaction with maxSelection**: When maxSelection is set, clicking Select All only selects the first N options up to the limit, not necessarily all visible options:
- If there are 20 visible options and maxSelection=5, clicking Select All selects the first 5 selectable options
- The checkbox may then be in indeterminate state (not all selected, some selected)
- This provides useful UX: Select All respects limits while still providing bulk selection

**Important interaction with groupMaxSelection**: When grouped options have per-group limits via groupMaxSelection:
- Select All respects both total limit (maxSelection) AND per-group limit (groupMaxSelection)
- Select All will select up to groupMaxSelection from each individual group
- The final selection respects both constraints simultaneously
- This may result in fewer than maxSelection items being selected if groupMaxSelection constraints are tighter

**Accessibility**: The Select All checkbox should have proper ARIA labeling so screen readers recognize it as a special control that affects all options. The component should announce changes like "Select All, checked, 5 options selected" or "Select All, indeterminate, 3 of 10 selected" depending on state.

**Important interaction with disabled options**: Select All only affects selectable (enabled) options. Disabled options remain disabled regardless of Select All state. If there are 10 options but 2 are disabled, Select All would only select the 8 enabled options (subject to selection limits). The Select All state is calculated based on selectable options only.

**Important behavior with custom values**: For combo-boxes with allowCustomValue=true, Select All does NOT automatically select or affect custom values. Custom values are separate from predefined options. However:
- Users can select all predefined options via Select All
- Then separately type/enter custom values as needed
- Custom values add to the selected count but aren't controlled by Select All

**Important role in combo-box workflows**:
```typescript
// Workflow example: Select all then filter to refine
1. User types "united" → shows "United States", "United Kingdom"
2. User clicks Select All → selects both matching items
3. User clears filter → now sees all options, with 2 already selected
4. User types "asia" → shows Asian countries
5. User clicks Select All → selects all Asian countries (adds to existing selections)
```

**Use cases**:
- **Large option sets**: When there are many options and users frequently need to select most or all of them
- **Bulk selection**: When the workflow involves selecting most options then deselecting a few exceptions
- **Filter-based bulk selection**: When users want to select all items matching a filter criteria in combo-box
- **Start-point for refinement**: When users want to get started with everything selected, then remove items
- **Baseline creation**: When establishing a baseline selection that gets fine-tuned later

**Code pattern - Select All with limits**:
```typescript
// Select all respects multiple limits simultaneously
multiSelect = true;
showSelectAll = true;
maxSelection = 5; // Total limit
groupMaxSelection = 2; // Per-group limit

// Options: 3 groups with 5 items each = 15 total items
// Clicking Select All selects: 2 from group1 + 2 from group2 + 1 from group3 = 5 total
// Respects all limits (5 total, 2 per-group)

// Filter to see only 3 items, 1 from each group
// Clicking Select All selects those 3 (doesn't try to select 5 since only 3 visible)
```

**Code pattern - combo-box filtering with Select All**:
```typescript
// Filter-able combo-box with Select All
multiSelect = true;
showSelectAll = true;
disableEdit = false; // Allow typing to filter
filterMode = "StartsWith"; // Filtering behavior
maxSelection = 10; // Respect limits

// User interaction flow:
// 1. User types "uni" → shows 3 matching options
// 2. User clicks Select All → selects those 3 matching items
// 3. User types "as" → shows different 4 matching options  
// 4. User clicks Select All → adds those 4 (now 7 total)
// 5. Total respects maxSelection=10 limit
```

**Important difference from dropdown**: In dropdown, Select All always selects all options in the entire dataset. In combo-box, Select All adapts to current filter state and selects from currently visible (filtered) options. This is intentional behavior for combo-box's filtering capability.

**Code pattern - handling Select All state programmatically**:
```typescript
// Programmatically determining Select All state
const getSelectAllState = (): 'checked' | 'unchecked' | 'indeterminate' => {
  const selectableOptions = this.options.filter(opt => !opt.disabled);
  const selectedCount = this.value ? this.value.length : 0;

  if (selectedCount === 0) return 'unchecked';
  if (selectedCount === selectableOptions.length) return 'checked';
  return 'indeterminate';
};
```

This prop is behavioral/visual and only applies in multi-select mode. It adds a convenient bulk selection feature that adapts to combo-box filtering, respecting selection limits and disabled options.

Usage: `showSelectAll="true"`

## confirmOnApply

When true and multiSelect=true, adds Apply and Clear buttons to the dropdown footer and requires explicit confirmation before committing selections. This is a behavioral prop that changes multi-select from immediate-updating to a confirmation workflow. For combo-box, this is particularly valuable when users might type custom values or filter extensively before finalizing selections.

**Confirm on Apply behavior**:

- **confirmOnApply=false (default)**: Multi-select works with immediate updates - when users select or deselect options, the value updates immediately. No confirmation buttons are displayed. In combo-box, typing and filtering change selections immediately as users interact.

- **confirmOnApply=true**: Multi-select works with confirmation workflow - users can select/deselect multiple options in the dropdown, including typing custom values, but changes are not committed until they click the Apply button. The dropdown displays two buttons at the bottom:

**Apply button**:
- Only enabled when at least one option is selected and selections differ from initial state
- Clicking commits the selections (fires valueChange with committed=true)
- After clicking, the dropdown closes and selected options appear in the field
- Button text is "Apply" or localized equivalent

**Clear button**:
- Always enabled when any options are selected
- Clicking deselects all options (fires valueChange with committed=false)
- After clicking, selections are cleared but dropdown remains open for new selections
- Button text is "Clear" or localized equivalent

**Important relationship with multiSelect**: The confirmOnApply prop only has an effect when multiSelect=true. In single-select mode, selections are always updated immediately (there's nothing to "confirm" since each selection replaces the previous one).

**Important interaction with clearButton**: When confirmOnApply=true, the clearButton prop is ignored/not displayed. The confirmation workflow provides its own Clear button in the footer, which serves the purpose of clearing selections. You would use either:
- clearButton=true for immediate clearing in single-select or multi-select without confirmation
- confirmOnApply=true for confirmation workflow with own Clear button

**Important interaction with combo-box filtering**: In combo-box filtering scenarios, confirmOnApply=true changes the interaction meaningfully:

**Without confirmOnApply** (immediate updates):
- User types to filter → each character shows filtered options immediately
- User clicks option → selection updates immediately
- User can continuously filter + select without ever committing
- Each selection changes the field value immediately

**With confirmOnApply** (confirmation workflow):
- User types to filter → each character shows filtered options immediately  
- User selects options → selections tracked but NOT committed yet
- User can type different filters → shows different option subsets
- User can select/deselect freely across different filter views
- Only when clicking Apply are ALL selections committed together
- This allows exploring across different filter criteria before final selections

**Important behavior valueChange events**:
When confirmOnApply=true, valueChange fires differently:

**Preview mode** (committed=false):
- Fires when selections change within dropdown
- Shows current selection state without committing
- Allows tracking preview state separately from final state

**Confirmed mode** (committed=true):  
- Fires only when Apply is clicked
- Shows final committed selections
- This is the state your application should use as the authoritative selection

**Code pattern - handling confirmation state**:
```typescript
onValueChange(event: CustomEvent<{name: string, value: string[], committed: boolean}>) {
  const { value, committed } = event.detail;
  
  if (committed) {
    // User clicked Apply - use this as actual selection
    this.finalSelections = [...value];
  } else {
    // Preview state - selections pending confirmation
    this.previewSelections = [...value];
  }
}
```

**Confirmation workflow state**:
1. **Dropdown opens**: Empty selections (or previous selections if maintaining state)
2. **User types to filter**: Filters visible options without committing selections
3. **User selects/deselects options**: Selections tracked but not committed yet
4. **User types different filter**: Can select from different subsets, all tracked together
5. **Apply click**: All tracked selections committed (fires valueChange with committed=true), dropdown closes, field reflects new selections
6. **Clear click**: All selections deselected (fires valueChange with committed=false), dropdown remains open
7. **Close without Apply**: If dropdown is closed without Apply, changes are abandoned (unless you've maintained preview state for later re-opening)

**Important role in combo-box custom values**: When allowCustomValue=true and confirmOnApply=true:
- Users can type custom values during their exploration
- Custom values are tracked like selections, pending confirmation
- Only committed on Apply, just like selected options
- This allows users to experiment with custom values before committing them

**Code pattern - combo-box with filtering + confirmation**:
```typescript
// Combo-box allowing exploration before commitment
multiSelect = true;
confirmOnApply = true;
allowCustomValue = true;
disableEdit = false; // Allow typing and filtering
filterMode = "StartsWith";
maxSelection = 10;

// User can:
// 1. Type "uni" → filter to find specific items
// 2. Select filtered items → tracked but not committed
// 3. Type "asia" → show different subset
// 4. Select more items → added to tracked selections
// 5. Type custom value → tracked like selection
// 6. Click Apply → everything committed at once
```

**Mobile experience**: When confirmOnApply=true and the dropdown opens as a full-screen drawer on mobile, the Apply/Clear buttons appear at the top (or bottom) of the drawer for easy access. This provides a mobile-optimized confirmation experience where users can:
- Scroll through many options
- Type to filter or select
- See current selection state
- Confirm with Apply when done

**Accessibility**: The Apply and Clear buttons should have proper ARIA attributes. Focus management should ensure keyboard users can navigate to and operate these buttons. The confirmation state should be clearly communicated to screen readers. The workflow should support:
- Keyboard navigation to Apply/Clear buttons
- Enter/Space to activate buttons
- Clear announcements about confirmation state changes

**Important interaction with totalSelected**: When confirmOnApply=true with totalSelected=true:
- Preview state may show draft count: "3 selected (uncommitted)"
- Confirmed state shows final count: "3 selected"
- The count updates in real-time during preview but reflects different state until Apply

**Code example - complete confirmation workflow**:
```typescript
@ زندگی(arr[Keyboard驳回) {/*component=visible*/})
export class FilterableComboBoxComponent {
  previewValues: string[] = [];
  finalValues: string[] = [];
  
  onValueChange(event) {
    const { value, committed } = event.detail;
    
    if (committed) {
      // Apply clicked - commit selections
      console.log('Committing selections:', value);
      this.finalValues = [...value];
      this.previewValues = [];
    } else {
      // Preview state - track changes
      console.log('Preview selections:', value);
      this.previewValues = [...value];
    }
  }
  
  // Optional: maintain preview when reopening dropdown
  openDropdown() {
    if (this.previewValues.length > 0) {
      // Restore preview state so user continues where left off
      // You would set this.value to this.previewValues
      // But maintain it's still preview until Apply clicked
    }
  }
}
```

**Important use case - complex selection workflows**:
- **Exploratory selection**: Users need to filter through many options and experiment before finalizing
- **Batch operations**: One confirmation for multiple selection operations is more efficient
- **User control**: Users want explicit control over when their selections are finalized, especially in data-heavy applications
- **Performance optimization**: When option selection triggers expensive operations, defer until explicit confirmation
- **Complex filters**: Users filter through different criteria and want to select from each subset before committing

**Code pattern - avoiding double-processing**:
```typescript
// Important: Only process committed selections for business logic
onValueChange(event) {
  if (event.detail.committed) {
    this.processSelections(event.detail.value); // Actually process
    // Don't preview processing - wait for Apply
  }
}
```

**Important troubleshooting**:
- If selections disappear on blur: Ensure you're not clearing preview state inappropriately
- If Clear button doesn't work: Check both clearButton=false and confirmOnApply=true are set
- If Apply doesn't fire: Ensure at least one selection exists (button may be disabled)

This prop is behavioral and only applies in multi-select mode. It changes multi-select from immediate-updating to a confirmation workflow with explicit Apply/Clear buttons, particularly valuable in combo-box for filtering-heavy multi-select scenarios.

Usage: `confirmOnApply="true"`

## allSelectionValue

Provides custom text to display in the combo-box field when all options are selected and totalSelected=true. This is a content prop that allows customization of the display text when every selectable option is chosen. For combo-box, this is particularly valuable when dealing with extensive filtering or when you want to provide clear, meaningful text when users have selected everything available.

**All selection value behavior**:

- **allSelectionValue not set**: When all options are selected and totalSelected=true, the combo-box displays the count pattern "{N} selected" where N is the number of options. For example, "10 selected" for 10 options (the default localized format).

- **allSelectionValue set (e.g., allSelectionValue="All countries selected")**: When all options are selected and totalSelected=true, the combo-box displays your custom text instead of the count. For example, "All countries selected" instead of "10 selected".

**Important relationship with totalSelected**: The allSelectionValue prop only has an effect when totalSelected=true. When totalSelected=false, the combo-box displays the actual option labels separated by the separator, so there's no special "all selected" display to customize.

**Important relationship with multiSelect**: The allSelectionValue prop only has an effect when multiSelect=true. In single-select mode, there's no concept of "all options selected" since only one is ever selected.

**Important behavior with combo-box filtering**: In combo-box filtering scenarios:
- "All options selected" means all options in the entire dataset (not just filtered subset)
- When filtering is active and totalSelected=true, the display depends on selection state:
  - If user has selected ALL options → shows allSelectionValue
  - If user has selected SOME options → shows count like "3 selected"
  - If user has selected ALL currently visible filtered options but NOT all overall options → shows count
- This distinction is important: allSelectionValue only triggers when every single selectable option in the entire dataset is selected

**Important behavior with custom values**: For combo-boxes with allowCustomValue=true:
- Custom values are not included in "all options selected" calculation
- Even if all predefined options are selected, custom values don't trigger allSelectionValue
- allSelectionValue specifically means all predefined/options-list options are selected
- This is intentional design because custom values theoretically infinite

**All options detection**: The component determines "all options selected" based on the count of selectable options (excluding disabled options). If there are 10 total options but 2 are disabled, then selecting the 8 selectable options triggers the "all selected" state and displays the custom allSelectionValue text.

**Code examples - behavior variations**:
```typescript
// Setup
multiSelect = true;
totalSelected = true;
allSelectionValue = "All countries selected";
options = [
  { value: "us", label: "United States" },
  { value: "ca", label: "Canada" },
  { value: "mx", label: "Mexico" }
];

// When 1 of 3 selected:
value = ["us"];
// Field shows: "1 selected" (count, not allSelectionValue)

// When 2 of 3 selected:
value = ["us", "ca"];
// Field shows: "2 selected" (count, not allSelectionValue)

// When 3 of 3 selected:
value = ["us", "ca", "mx"];
// Field shows: "All countries selected" (allSelectionValue!)
```

**Important behavior with disabled options**:
```typescript
// With disabled options
options = [
  { value: "us", label: "United States", disabled: false },
  { value: "ca", label: "Canada", disabled: false },
  { value: "mx", label: "Mexico", disabled: true } // Disabled
];

// Selecting 2 of 2 selectable options:
value = ["us", "ca"];
// Field shows: "All countries selected" (allSelectionValue)
// Even though there are 3 options total, only 2 are selectable
```

**Important interaction with groupMaxSelection**: When grouped options have per-group limits:
- "All options selected" means all options within those limits
- If groupMaxSelection restricts some options from being selected, "all selected" means selecting up to those limits
- This provides logical behavior: "all selected" means all available/allowed selections

**Code example with limits**:
```typescript
multiSelect = true;
totalSelected = true;
maxSelection = 5;
allSelectionValue = "Maximum selections made";

// When 5 of 15 options selected:
value = /* 5 options */;
// Field shows: "Maximum selections made" (allSelectionValue)
// Even though only 5 selected vs 15 total, hitting the limit triggers custom text
```

**Important use cases**:
- **Custom messaging**: When you want the field to say something more descriptive than just the count when all options are selected (e.g., "All countries selected" vs "10 selected")
- **Branding/language**: When the count message is too generic and you want more specific, context-appropriate text (e.g., "All regions active" for regional settings)
- **User experience**: When you want to provide clearer feedback when all options are selected (e.g., "Selected all filters" vs "5 selected")
- **Special states**: When reaching maximum selections is significant (e.g., "Maximum filters applied" rather than just count)

**Code pattern - dynamic allSelectionValue**:
```typescript
allSelectionValue: string = "";

updateAllSelectionValue(totalOptions: number) {
  switch (totalOptions) {
    case 0:
      this.allSelectionValue = "No options available";
      break;
    case 1:
      this.allSelectionValue = "Only option selected";
      break;
    default:
      this.allSelectionValue = `All ${totalOptions} options selected`;
  }
}

// Call this when options load发生变化
loadOptions() {
  this.options = this.fetchOptions();
  this.updateAllSelectionValue(this.selectableOptionsCount);
}
```

**Important role in combo-box filtering**:
- When user types to filter, allSelectionValue doesn't change (always based on total options)
- Field shows custom text permanently once all options are selected, regardless of current filter
- This provides stable messaging even as filtering changes what's visible

**Code pattern - combo-box with filtering**:
```typescript
// Combo-box allowing filtering + everything selected
multiSelect = true;
totalSelected = true;
allowCustomValue = true;
allSelectionValue = "All filters active";
disableEdit = false;
filterMode = "StartsWith";

// User selects: ALL 10 options
value = /* all 10 values */;
// Field shows: "All filters active" (allSelectionValue)

// User types: "uni" → shows 2 filtered options
// Field still shows: "All filters active" (because ALL options are selected, not just visible ones)
// Important: allSelectionValue is based on total dataset, not filtered view
```

**Best practices for allSelectionValue**:
- **Concise but descriptive**: Keep text short but meaningful (e.g., "All regions selected" vs "You have selected all of the available regions from the list")
- **Context-specific**: Make text relevant to what options represent (e.g., "All currencies" for currency selector, "All statuses" for status filter)
- **Action-oriented**: If relevant, indicate what happens next (e.g., "All countries included - ready to proceed")
- **Avoid confusion**: Don't make custom text ambiguous about what's selected

**Important accessibility**:
- Screen readers announce the custom allSelectionValue text
- Ensure text is clearly understandable without visual context
- Avoid technical jargon that might be confusing
- Consider localization if supporting multiple languages

**Common pitfalls to avoid**:
- Using allSelectionValue when totalSelected=false (has no effect)
- Forgetting to account for disabled options (allSelectionValue may trigger earlier than expected)
- Confusing filtered view with total dataset (allSelectionValue is for total dataset)
- Not updating allSelectionValue when options list changes

**Code pattern - handling dynamic options**:
```typescript
// When options reload, update allSelectionValue appropriately
async reloadOptions() {
  this.loading = true;
  try {
    const newOptions = await this.fetchUpdatedOptions();
    this.options = newOptions;
    
    // Update allSelectionValue if needed
    const selectableCount = newOptions.filter(o => !o.disabled).length;
    this.allSelectionValue = `All ${selectableCount} options selected`;
    
    // Check if we need to adjust value (some previously-selected options may no longer exist)
    this.validateSelectionsAgainstNewOptions(newOptions);
  } finally {
    this.loading = false;
  }
}
```

This prop is content-focused and only applies when both multiSelect=true and totalSelected=true. It allows customization of the display message when every selectable option is selected, providing clearer, more context-appropriate messaging than the default count format.

Usage: `allSelectionValue="All Statuses Selected"`

## maxSelection

Limits the maximum number of options that can be selected in multi-select mode. This is a behavioral prop that enforces selection limits and prevents users from selecting more options than allowed. For combo-box, this is particularly valuable when managing resources, preventing performance issues, or enforcing business rules around selection limits.

**Max selection behavior**:

- **maxSelection not set (or undefined)**: No limit on the number of selected options in multi-select. Users can select as many options as exist in the dropdown, up to all options. This applies to both predefined options and custom values (when allowCustomValue=true).

- **maxSelection set to number (e.g., maxSelection=5)**: Users can only select up to the specified number of options. When the limit is reached:
  - Additional options become disabled/unclickable in the dropdown
  - Users must deselect existing selections before selecting additional options
  - Visual indication shows when at the limit (typically disabled appearance on remaining options)
  - Selections are prevented beyond the limit, enforced by the component
  - Custom value entry (when allowCustomValue=true) is also blocked at this limit

**Important relationship with multiSelect**: The maxSelection prop only has an effect when multiSelect=true. In single-select mode, the limit of 1 is inherent, and specifying maxSelection doesn't change behavior.

**Important interaction with groupMaxSelection**:
- **maxSelection**: Limits total selections across ALL options and ALL groups combined
- **groupMaxSelection**: Limits selections per individual option group

Both limits can be set simultaneously, and both must be satisfied. For example:
- maxSelection=5 AND groupMaxSelection=2 with 3 groups means:
  - Total selections cannot exceed 5 across all groups
  - Each of the 3 groups cannot have more than 2 selections independently
  - So possible distribution could be: Group1:2 + Group2:2 + Group3:1 = 5 total (valid)
  - But distribution like Group1:2 + Group2:2 + Group3:2 = 6 total (invalid, exceeds total limit)
  - Or distribution like Group1:3 + Group2:1 + Group3:1 = 5 total (invalid, exceeds group limit)

**Important interaction with combo-box filtering**: In combo-box filtering scenarios, maxSelection behavior is particularly relevant:
- The limit applies to total selections overall, not per filter view
- Users can filter, select items from one view, then filter to a different view and select more items
- The same selection limit persists across all filter states
- Visual feedback shows remaining selections available (e.g., "2 of 5 used" or similar)

**Disabled options don't count toward max**: The maxSelection limit only counts selectable (non-disabled) options. If there are 15 total options but 3 are disabled, maxSelection=5 means users can select up to 5 of the 12 selectable options. Disabled options are excluded from the limit calculation.

**Show Select All interaction with maxSelection**: When showSelectAll=true and maxSelection is set:
- Clicking Select All selects up to the max limit, not necessarily all options
- If there are 10 options and maxSelection=5, clicking Select All selects the first 5 selectable options
- The Select All checkbox appears in indeterminate state (not all selected, some selected)
- Users can individually add/remove selections within the limit

**Important behavior with showSelectAll in filtered state**:
- When filtering is active AND maxSelection is set, clicking Select All selects up to maxSelection from visible filtered options
- Example: 50 total options, maxSelection=5, filter shows 10 matching options
- Clicking Select All → selects first 5 of the 10 matching options
- User can clear filter, filter differently, select more options up to remaining limit
- This allows filtered, limited selection workflow

**Important interaction with confirmOnApply**: When confirmOnApply=true, the current selection limit enforcement happens during selection but final commitment happens on Apply. This means:
- During dropdown interaction, component enforces maxSelection during preview state
- All selections must be within maxSelection limit to enable Apply button
- Clear button can reset all selections to 0 within the limit
- Apply only becomes enabled when selections are positive but within limit

**Important behavior with custom values**: For combo-boxes with allowCustomValue=true and maxSelection set:
- Custom values count toward the maxSelection limit
- Users can mix custom values and standard options within the limit
- Example: maxSelection=5, user selects 3 options and creates 2 custom values = 5 total
- Attempting to add sixth custom value or select sixth option blocks with visual feedback
- This maintains consistent limit across all selection types

**Visual feedback at/near limit**: The component provides various visual cues when approaching the limit:
- Remaining selections indicator: "2 of 5 selected" or similar
- Options becoming disabled when limit reached
- Warning indicators or notification when trying to exceed limit
- Color changes or warnings when very close to limit

**Code pattern - tracking selections against limit**:
```typescript
const canSelectMore = (): boolean => {
  const currentCount = this.value ? this.value.length : 0;
  return currentCount < this.maxSelection;
};

const getSelectionStatus = (): string => {
  const currentCount = this.value ? this.value.length : 0;
  return `${currentCount} / ${this.maxSelection} selected`;
};
```

**Use cases**:
- **Resource allocation**: Limiting selections when selecting too many consumes too much resource (e.g., bandwidth, memory, api calls)
- **Data limits**: Preventing selection of too many items for data processing limits, UI performance, or downstream system constraints
- **Business rules**: Enforcing business constraints (e.g., "最多选择5个因素进行对比" - maximum 5 factors for comparison)
- **Performance**: Preventing excessive selections that would impact performance (rendering, network requests, computational cost)
- **User experience**: Avoiding overwhelming users with too many selections to manage
- **UI constraints**: Fitting selections within visible space (e.g., tag display area, mobile constraints)

**Code example with multiple limits**:
```typescript
// Enable multi-select with total and group limits
multiSelect = true;

// Set total limit across all options
maxSelection = 5;

// Set per-group limit  
groupMaxSelection = 2;

// Show Select All while respecting limits
showSelectAll = true;

options = [
  { label: "Americas", items: [US, CA, MX, BR] },  // 4 items
  { label: "Europe", items: [UK, FR, DE, ES, IT] },  // 5 items
  { label: "Asia", items: [JP, CN, IN, KR, SG, MY] }  // 6 items
];

// Valid distributions:
// A: 2 Americas + 2 Europe + 1 Asia = 5 total ✓ (respects both limits)
// B: 1 Americas + 2 Europe + 2 Asia = 5 total ✓

// Invalid distributions:
// C: 3 Americas + 1 Europe + 1 Asia = 5 total ✗ (exceeds Americas group limit)
// D: 2 Americas + 3 Europe + 0 Asia = 5 total ✗ (exceeds Europe group limit)
// E: 6 total selections ✗ (exceeds total maxSelection limit)
```

**Important pattern - combo-box filtering with limits**:
```typescript
// Combo-box with filtering and selection limits
multiSelect = true;
maxSelection = 5;
disableEdit = false; // Allow typing for filtering
filterMode = "MultiToken"; // Multi-word search
allowCustomValue = true; // Allow custom entries too

// User workflow:
// 1. Type "united states" → shows 2 matching options
// 2. Select both: Now 2/5 used
// 3. Type "asia" → shows 8 matching options  
// 4. Select first 3: Now 5/5 used (at limit)
// 5. Try to select 4th option → blocked, shows "Maximum 5 selections reached"
// 6. Can still type custom value → blocked at limit
// 7. Must deselect something to select/add more
```

**Code pattern - real-time limit tracking**:
```typescript
// Track how close to limit
get proximityToLimit(): 'far' | 'near' | 'at' {
  const count = this.value ? this.value.length : 0;
  const remaining = this.maxSelection - count;
  
  if (remaining <= 0) return 'at';
  if (remaining <= 2) return 'near';
  return 'far';
}

// Show appropriate UI based on proximity
get limitDisplay(): string {
  const count = this.value ? this.value.length : 0;
  const proximity = this.proximityToLimit;
  
  switch (proximity) {
    case 'at': 
      return `Maximum ${count} selections reached`;
    case 'near':
      return `${count} selected (${this.maxSelection - count} remaining)`;
    case 'far':
      return `${count} selected`;
  }
}
```

**Important interaction with allSelectionValue**: When maxSelection is set and allSelectableCount equals maxSelection (because disabled options or functional limit), clicking Select All triggers allSelectionValue. Example: 10 total options, 3 disabled, maxSelection=7 - selecting all 7 selectable options triggers allSelectionValue display showing "All available options selected."

**Best practices for maxSelection**:
- **Clear communication**: Always show remaining selections available (e.g., "3 of 5 selected")
- **Reasonable defaults**: For most use cases, 5-10 is reasonable unless specific business needs dictate otherwise
- **Progressive disclosure**: Consider showing visuals or warnings as users approach the limit
- **Non-arbitrary limits**: Set limits based on actual constraints (performance, business rules) not just arbitrary numbers
- **Persisted state**: Note that maxSelection limit only applies to current component instance; persisted selections should respect limit when restoring

This prop is behavioral and only applies in multi-select mode. It enforces selection limits at the total level, working in combination with groupMaxSelection for individual group limits, and applies equally to both standard options and custom values.

Usage: `maxSelection="5"`

## groupMaxSelection

Limits the maximum number of options that can be selected from each individual option group in multi-select mode. This is a behavioral prop that enforces per-group selection limits while the overall multi-select limit (maxSelection) controls the total across all groups. For combo-box, this is particularly valuable when options are organized hierarchically and you need balanced selection across categories.

**Group max selection behavior**:

- **groupMaxSelection not set (or undefined)**: No per-group limit on selections within option groups. Users can select any number of options from each group, subject only to the overall maxSelection limit.

- **groupMaxSelection set to number (e.g., groupMaxSelection=2)**: Users can only select up to the specified number of options within each individual option group. When the group limit is reached:
  - Additional options in that group become disabled/unclickable
  - Users can still select options from other groups (subject to other groups' limits and overall maxSelection)
  - Visual indication shows when group limit is reached (typically disabled appearance on remaining options in that group)
  - Selections per group are prevented beyond the limit
  - Different groups maintain independent limits

**Important relationship with maxSelection**:
- **maxSelection**: Limits total selections across ALL options and ALL groups combined
- **groupMaxSelection**: Limits selections per individual option group

Both limits can be set simultaneously, and both must be satisfied. Example:
- maxSelection=5 AND groupMaxSelection=2 with 3 groups means total selections cannot exceed 5 across all groups, and each of the 3 groups cannot have more than 2 selections independently.

**Ungrouped options with groupMaxSelection**: Ungrouped options (options not wrapped in a group structure) are treated as part of a single "ungrouped" group for the purposes of groupMaxSelection. So if groupMaxSelection=2 and there are ungrouped options, you can select at most 2 from the pool of ungrouped options.

**Show Select All with per-group limits**: When showSelectAll=true and groupMaxSelection is set, clicking Select All respects the per-group limits, selecting up to groupMaxSelection items from each group rather than all items.

**Important interaction with combo-box filtering**: In combo-box filtering scenarios:
- The groupMaxSelection limit applies per group in the FULL dataset, not per filtered view
- Users can filter to see specific items from different groups
- Clicking Select All in filtered view respects group limits for visible items
- The actual group selection limit is based on the full group, not filtered subset

**Independent group limits**: Each group has its own limit. Reaching the limit in one group doesn't affect the limits of other groups. Users can continue selecting from other groups up to their respective groupMaxSelection values.

**Important behavior with custom values**: For combo-boxes with allowCustomValue=true:
- Custom values are NOT assigned to any group for selection limit purposes
- Custom values count toward the overall maxSelection limit but NOT toward groupMaxSelection

**Use cases**:
- **Balanced selections**: Enforcing even distribution across categories (e.g., select at most 2 from each region)
- **Category-specific rules**: Applying different business rules to different groups
- **Fair selections**: Preventing excessive selection from any single category
- **Resource allocation by group**: Managing selections per resource category independently

Usage: `groupMaxSelection="2"`

## allowCustomValue

Enables users to input and select values that don't exist in the predefined options list. This is a behavioral prop that allows the combo-box to function as both a selector from predefined options AND a text input field for custom user-created values. For combo-box, this is one of the key differentiators from dropdown, giving users maximum flexibility.

**Allow custom value behavior**:

- **allowCustomValue=false (default)**: Users can only select from the predefined options list. When typing in the combo-box (if disableEdit=false), the text only serves for filtering options. If users type text that doesn't match any option, that text is not committed as a selection - it's simply ignored or shows "no results" behavior.

- **allowCustomValue=true**: Users can both select from predefined options AND enter custom values that don't exist in the options list. Custom values behave identically to selected options:
  - Custom values become part of the value array (in multi-select) or the single value (in single-select)
  - Custom values commit on blur or selection
  - Custom values appear in the field in the same way as selected options (as tags or text)
  - Custom values are included in form submissions via the name attribute
  - Custom values trigger valueChange events just like standard option selections

**Important interaction with disableEdit**: The allowCustomValue prop only provides value acceptance when disableEdit=false. When disableEdit=true (cannot type), allowCustomValue=true has no effect because users cannot enter custom values - they can only select from predefined options in the dropdown.

**Important interaction with multi-select**: For combo-boxes with multiSelect=true and allowCustomValue=true:
- Users can select multiple predefined options AND add multiple custom values
- Custom values and selected options appear together in the value array
- Example: value = ["us", "ca", "custom-service-1", "custom-service-2"]
- Visual display treats both types identically (tags or comma-separated based on disableTags)
- The total selection count (for maxSelection) includes both types together

**Custom value validation and acceptance flow**:
1. User types text in the combo-box input field
2. As they type, the combo-box filters existing options based on the text
3. When they blur (click away, tab out) the input field:
   - **allowCustomValue=false**: Non-matching text is rejected, field clears or shows selection from filtered options
   - **allowCustomValue=true**: Non-matching text is accepted as a custom value, added to selections

**Visual behavior for custom values**:
- Custom values appear in the field identically to selected options
- In multi-select with disableTags=false: Custom values appear as removable tags like selected options
- In multi-select with disableTags=true: Custom values appear in comma-separated text like selected options
- Visual appearance matches standard options - no differentiation unless custom styling is applied

**Important interaction with filterMode and filtering props**: The filtering props (filterMode, filterKeys, caseSensitiveFilter) control how the combo-box filters PREDEFINED options during typing. Custom values don't affect these filtering behaviors:
- While typing, filtering matches against predefined options using filterMode settings
- Custom value acceptance happens (at blur) regardless of what filtering produced
- Example: User types "xyz" with filterMode="StartsWith" and no options match, but if allowCustomValue=true, "xyz" is still accepted as custom value on blur

**Code pattern - custom value with multi-select**:
```typescript
// Setup: Multi-select with custom values
multiSelect = true;
allowCustomValue = true;
disableEdit = false; // Enable typing
disableTags = false; // Show tags
maxSelection = 10; // Limit total selections (opts + custom)

// User interaction:
// 1. Types and selects "United States" → value = ["us"]
// 2. Types and selects "Canada" → value = ["us", "ca"]  
// 3. Types "custom-api" → no matching options shown
// 4. Blurs field → "custom-api" accepted as custom value
// 5. value = ["us", "ca", "custom-api"]

// Custom value appears like a selection tag
```

**Important behavior with confirmOnApply**: When confirmOnApply=true and allowCustomValue=true:
- Custom values are tracked in the preview state alongside selected options
- Custom values only commit when Apply button is clicked
- Users canmix selecting predefined options AND entering custom values before confirmation
- This allows exploration: select some options, type some custom values, then decide to commit or clear all together

**Code pattern - confirmation with custom values**:
```typescript
multiSelect = true;
confirmOnApply = true;
allowCustomValue = true;

onValueChange(event) {
  const { value, committed } = event.detail;
  
  if (committed) {
    // Both selected options and custom values are committed together
    // e.g., ["us", "ca", "custom-service-1"]
    this.finalSelections = [...value];
  } else {
    // Preview state includes both types
    this.previewSelections = [...value];
  }
}
```

**Important interaction with maxSelection**: When both maxSelection and allowCustomValue=true are set:
- Custom values count toward the maxSelection limit like selected options
- Example: maxSelection=5, user selects 3 options + enters 2 custom values = 5 total limit reached
- Cannot enter 6th custom value or select 4th option when at limit
- Component enforces limit across both selection types

**Use cases**:
- **Open-ended selections**: When you provide suggested options but need flexibility for user-created values (e.g., service names, identifiers)
- **Future-proofing**: When new options may appear over time and users need a way to specify them immediately rather than waiting for updates to the options list
- **Mixed selection workflows**: When users need to select from standard options but occasionally need custom entries (e.g., standard currencies + custom "other" amounts)
- **Dynamic categorization**: When options represent categories but users need to create new categories on the fly
- **API parameters**: Users select from known API parameters or supply custom ones
- **Form flexibility**: Reducing form field count by allowing "other specify" in the same component rather than separate text field

**Code pattern - handling custom values in form submission**:
```typescript
onFormSubmit() {
  const formData = this.form.value;
  
  // Both selected options and custom values arrive in same value prop
  const selectedItems = formData.relatedItems;
  // e.g., ["option-1", "option-2", "custom-value-123"]
  
  // Process both uniformly
  selectedItems.forEach(item => {
    if (this.isStandardOption(item)) {
      // Handle standard option - might look up metadata
      this.processStandardOption(item);
    } else {
      // Handle custom value - might create new record
      this.processCustomValue(item);
    }
  });
}
```

**Important validation for custom values**: Applications should validate custom values separately:
- Format validation: Ensure custom values meet required format (e.g., email address pattern, length limits)
- Business rule validation: Check custom values against business constraints (e.g., no duplicates, allowed characters)
- Security validation: Sanitize user input when custom values are processed server-side

**Code pattern - validating custom values**:
```typescript
validateCustomValue(value: string): boolean {
  // Format validation
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailPattern.test(value)) {
    return false; // Invalid format
  }
  
  // Length validation
  if (value.length > 50) {
    return false; // Too long
  }
  
  // Business rule validation - no duplicates
  if (this.value && this.value.includes(value)) {
    return false; // Already selected
  }
  
  return true; // Valid
}

// Apply validation before accepting custom value
onBlur(event) {
  const inputValue = this.inputValue;
  if (!this.isStandardOption(inputValue) && this.allowCustomValue) {
    if (this.validateCustomValue(inputValue)) {
      this.acceptCustomValue(inputValue);
    } else {
      this.showValidationError("Invalid custom value format");
    }
  }
}
```

**Important behavior with search/filtering**: When users type to search and allowCustomValue=true:
- As they type, the combo-box filters and shows matching standard options
- If no matches exist and they blur, the typed text becomes a custom value
- This creates smooth UX: type to find, if nothing found, just type your own value and blur
- No special action needed to switch from "search" mode to "custom value" mode

**Code pattern - hybrid search/custom workflow**:
```typescript
// Most common use case: search options, if not found, create custom
disableEdit = false;
allowCustomValue = true;
filterMode = "StartsWith";

// User workflow:
// 1. User wants "United States"
// 2. Types "uni" → sees "United States" option
// 3. Selects it → simple selection

// Alternative workflow:
// 1. User wants a new service "api-provider-xyz"
// 2. Types "api" → no matching options
// 3. Types full "api-provider-xyz" → still no matches
// 4. Users accept and blur → "api-provider-xyz" becomes custom value
// No separate "create custom" button needed - just type and accept
```

**Common patterns with allowCustomValue**:

**Legacy data support**: Allow users to select existing options OR enter legacy/custom values:
```typescript
options = this.getCurrentStandardOptions(); // Today's options
allowCustomValue = true; // Support yesterday's custom values too
```

**Import/export workflows**: Support importing data with custom values while offering standard selections:
```typescript
// User imports file with "custom-service-name"
// It auto-populates in combo-box as a custom value
// User can still select from standard options for other selections
```

**Provisioning/registration**: Standard options (known entities) + custom values (new entities):
```typescript
options = this.getKnownServers(); // Known data centers
allowCustomValue = true; // New servers being provisioned
// User can select known OR type new server location
```

**Important accessibility with custom values**:
- Screen readers should distinguish custom values from standard options
- Consider adding visual indicators (like icons) to identify custom values
- Custom values should be properly announced with context (e.g., "Custom value: api-provider-xyz selected")
- Provide clear error messaging when custom values fail validation

**Best practices with allowCustomValue**:
- **Validate thoroughly**: Custom values bypass your controlled options list - validate server-side too
- **Provide guidance**: Use placeholder or helperMessage to indicate custom values are allowed
- **Set expectations**: If custom values will be processed differently, explain that to users
- **Consider limits**: Use maxSelection to prevent unlimited custom values that could overwhelm your system
- **Document management**: Decide whether custom values are ephemeral or should be added back to options list for future users

This prop is behavioral and fundamental to combo-box's flexibility beyond dropdown. It enables users to go beyond predefined selections while still benefiting from filtering and selection workflows.

Usage: `allowCustomValue="true"`

## limit

Controls the maximum number of visible filtered options in the dropdown. This is for display purposes only - use maxSelection and groupMaxSelection to enforce selection limits. Different scoping with limit being for display only.

Usage: `limit="50"`

## disableTags

Controls how selected values are displayed in multi-select mode. When disableTags=true, selected values appear as comma-separated text; when disableTags=false, they appear as removable tags. Only applies when multiSelect=true. This is a visual prop with significant UX implications for how users interact with and manage their selections in the combo-box field.

**Disable tags behavior and display modes**:

- **disableTags=false (default)**: Selected values appear as removable chips/tags in the combo-box field. Each tag shows:
  - The label of the selected option (or custom value)
  - An X/close button that removes that specific selection when clicked
  - Consistent styling and spacing between tags
  - Visual distinction between different selections (separate tags)
  
  This mode provides a more interactive, visually distinct display where users can remove individual selections by clicking their tag's X button. The tags appear inline with the field and users can still type to filter/add more selections.

- **disableTags=true**: Selected values appear as comma-separated text within the combo-box field. For example, if options "United States", "Canada", "Mexico" are selected and separator=", ", the field displays: "United States, Canada, Mexico". This mode:
  - Shows selected values as continuous text using the separator prop
  - Does NOT provide individual X buttons for removing specific selections
  - Users must remove selections via dropdown interaction (deselecting items)
  - Provides a more compact, plain text appearance
  - Useful when the field needs to look like traditional multi-select display

**Important relationship with multiSelect**: The disableTags prop only has an effect when multiSelect=true. In single-select mode, there's only ever one selected value, so the distinction between tags and comma-separated text is irrelevant.

**Important interaction with separator prop**: When disableTags=true, the separator prop controls how multiple selected value labels are joined in the text display. When disableTags=false, the separator prop may still be used internally (for screen readers, accessibility, or value serialization) but it's not visually displayed since tags are shown individually.

**Visual comparison of display modes**:

**disableTags=false (tags)**:
```
┌─────────────────────────────────────┐
│ [United States X] [Canada X] [Mexi...]│
└─────────────────────────────────────┘
```
- Individual tags with X buttons
- Can click X to remove specific selection
- Tags appear inline with field
- Each tag distinct and removable

**disableTags=true (comma-separated)**:
```
┌─────────────────────────────────────┐
│ United States, Canada, Mexico,      │
└─────────────────────────────────────┘
```
- Continuous text separated by ", " (or other separator)
- No individual removal buttons
- Cannot remove specific selections by clicking
- Must use dropdown to deselect items

**Important interaction with tagDisplay and overflowMode**: When disableTags=false, these props become relevant for how tags are arranged when there are many selections:
- **tagDisplay="collapsed"** (default): Shows single row of tags with +N overflow indicator that expands to maxVisibleRows when clicked
- **tagDisplay="wrap"**: Allows tags to wrap to multiple rows within maxVisibleRows limit
- **overflowMode="clip"**: Excess tags hidden and shown as +N counter
- **overflowMode="scroll"**: Makes the tag container scrollable

When disableTags=true, tagDisplay and overflowMode have minimal effect since individual tag positioning isn't available.

**Important role in combo-box editing**: When disableEdit=false (users can type), the interaction varies by display mode:

**With disableTags=false (tags)**:
- Tags appear inline with field
- Users can type to filter/add more selections
- Clicking within field positions cursor appropriately around tags
- Visual separation between existing tags and user input area

**With disableTags=true (text)**:
- Selected values appear as continuous text
- Users can type to filter/add more selections
- Text input area appears adjacent to displayed selections
- Less visual differentiation between existing selections and new typing

**Use cases for each mode**:

**disableTags=false (tags) - Recommended for most use cases**:
- **Interactive management**: Users need to remove individual selections frequently (e.g., filter chips, tag management)
- **Visual clarity**: When individual selections should be visually distinct for UX (e.g., team member selector, filter chips)
- **Touch-friendly**: Better for mobile where individual tap-to-remove is easier than navigating dropdown
- **Freq
### pattern**: Users quickly add and remove selections (add → remove → add again loop)
- **Variety of selections**: When types of selections differ significantly (tags provide visual recognition)

**disableTags=true (text) - Use for specific scenarios**:
- **Compact display**: When space is limited and continuous text is more space-efficient (e.g., small form factors)
- **Traditional multi-select**: When emulating traditional form multi-select behavior (familiar to users from other tools)
- **Selection-heavy**: When there are many selections and tags would be overwhelming (e.g., 10+ items)
- **Edit-disabled scenarios**: When disableEdit=true and users won't be adding/removing individually (just display existing selections)
- **Exported data display**: When field is primarily for showing existing selected items rather than active selection management

**Code pattern - interactive tags (recommended)**:
```typescript
multiSelect = true;
disableTags = false; // Show tags for easy removal
maxSelection = 5;
tagDisplay = "wrap"; // Allow tags to wrap

// Users get:
// - Individual tags they can click to remove
// - Can still type to add more
// - Visual clarity about what's selected
// Easy to refine selections (remove unwanted, click to filter for more)
```

**Code pattern - compact text display**:
```typescript
multiSelect = true;
disableTags = true; // Show comma-separated text
separator = "; "; // Custom separator

// Users get:
// - Compact display: "United States; Canada; Mexico"
// - More space for filtering text
// - Traditional multi-select appearance
// - Space savings in small forms

// To remove selections, users must:
// - Open dropdown
// - Deselect items from the list
```

**Important accessibility differences**:
**disableTags=false (tags)**:
- Each tag has proper ARIA markup for screen readers
- Screen readers announce each tag individually
- Tag's X button is keyboard accessible (tab to tag, enter to remove)
- Clear indication that individual items can be removed

**disableTags=true (text)**:
- Screen readers may read entire text string (e.g., "United States, Canada, Mexico, selected")
- Individual item removal less clear to screen reader users
- Keyboard users navigate to field, not individual items
- Less accessible for individual item management

**Code example - accessibility enhancement for tags**:
```typescript
// When disableTags=false, ensure proper keyboard navigation
// Users can tab to individual tags and press enter/space to remove
// Screen readers announce: "United States selected, press enter to remove"
```

**Important interaction with maxSelection**: Regardless of disableTags setting, maxSelection still limits total selections:
- With tags: Visual indication when at limit (disabled appearance for add actions, limit counter)
- With text: Limit enforces but display may not clearly show limit status until trying to add more

**Important behavior with custom values**: For combo-boxes with allowCustomValue=true and disableTags=false:
- Custom values appear as tags just like selected options
- Custom value tags are visually indistinguishable from standard option tags (unless custom styling applied)
- Custom value tags can be removed individually by clicking their X button
- This provides uniform UX whether user selects predefined option or enters custom value

**Code pattern - mixed display types**:
```typescript
// Show tags for visual distinction, but consider switching for many selections
get disableTags(): boolean {
  // Use tags when reasonable number of selections
  if (this.value.length <= 5) {
    return false; // Show tags
  }
  // Switch to text when many selections to avoid overwhelming tags
  return true; // Show comma-separated text
}
```

**Important role in totalSelected display**: When totalSelected=true, disableTags has less visual effect because field shows count instead of individual items. However, when totalSelected=false, disableTags determines whether users see individual tags or comma-separated text.

**Code pattern - combining with totalSelected strategies**:
```typescript
// Strategy: Use totalSelected for many items, tags for few
multiSelect = true;

const displayMode = this.value.length > 5 ? 'count' : 'individual';

switch(displayMode) {
  case 'count':
    this.totalSelected = true; // Show "X selected"
    // disableTags doesn't matter for display
    break;
  
  case 'individual':
    this.totalSelected = false; // Show individual items
    this.disableTags = false; // Show as tags for easy management
    break;
}
```

**Important mobile behavior**: On mobile devices:
- tags (disableTags=false) provide larger touch targets (tap to remove) which is better for touch interaction
- text display (disableTags=true) may be harder to manage without fine motor control for dropdown navigation
- Consider mobile UX when choosing between modes

**Code pattern - mobile-optimized tags**:
```typescript
// Mobile prefers tags for better touch interaction
if (this.isMobile) {
  this.disableTags = false; // Tags have larger touch targets
  this.tagDisplay = "collapsed"; // Single row with expansion
} else {
  // Desktop - can use either mode based on use case
  this.disableTags = this.compactLayout;
}
```

**Important interaction with confirmOnApply**: When confirmOnApply=true:
 disableTags affects the FIELD display of selections (tags or text)
 ConfirmOnApply affects the WORKFLOW for committing selections (immediate vs confirmed on apply)
 These are independent - you can have tags with immediate updates OR comma text with confirmation workflow OR any combination

**Important implications for exported data**: When disableTags=true:
- The comma-separated text may appear directly in exported forms or printed documents
- When disableTags=false, you may need to serialize tags to text format for export:
```typescript
// Export comma-separated regardless of display mode
getExportData(): string {
  const selections = this.value;
  return selections.join(this.separator);
  // Same format whether displayed as tags or text
}
```

**Code pattern - responsive display strategy**:
```typescript
get disableTags(): boolean {
  // Responsive: Use different modes based on viewport width
  if (this.viewportWidth < 768) {
    return true; // Mobile: Text mode for space savings
  } else {
    return false; // Desktop: Tags for interactivity
  }
}
```

**Best practices**:
- **Default to disableTags=false** for most interactive multi-select use cases
- **Consider disableTags=true** for display-only or data-heavy scenarios where interactivity is less important
- **Combine with tagDisplay** (when disableTags=false) for optimal tag layout behavior  
- **Test with actual users** - the choice between interactivity vs compactness is often user-preference driven
- **Consider accessibility** - tags provide better keyboard/screen reader experience for individual item management

**Code pattern - dynamic switching based on user preferences**:
```typescript
// Allow users to choose their preferred display mode
get userDisplayPreference(): string {
  return localStorage.getItem('comboBoxDisplayMode') || 'tags';
}

set disableTags(): boolean {
  return this.userDisplayPreference === 'text';
}

// Provide UI toggle to let users switch between:
// - Tags (individual removal, interactive)
// - Text (compact, cleaner)
```

This prop is visual and significantly affects the UX of multi-select selection management. It provides different interaction models (individual tag removal vs dropdown-only management) and should be chosen based on your specific use case's interactivity needs, space constraints, and accessibility requirements.

Usage: `disableTags="true"`

## filterMode

Controls how the combo-box filters options based on user input when typing. This is a behavioral prop that determines the matching algorithm used to find options that match the user's search query. For combo-box, filterMode is particularly important as it defines the search behavior that makes the type-to-filter experience work effectively.

**Filter mode values and their behavior**:

- **SingleToken (default)**: Matches individual tokens/words in option labels. The user's query is split into tokens (words separated by spaces), and each option is checked if it contains ANY of the individual tokens. This provides the most permissive matching - options match if they contain any word from the query.

- **MultiToken**: Matches multiple tokens simultaneously. The user's query is split into tokens, and options must contain ALL the tokens to be considered a match. More restrictive than SingleToken - requires options to contain all words from the query (though not necessarily in order).

- **StartsWith**: Matches beginning of strings. Options match if they start with the user's query (or start with the query at the start of any word in multi-word options). Most restrictive - requires exact prefix match.

**Important relationship with disableEdit**: The filterMode prop only applies when disableEdit=false (users can type to filter). When disableEdit=true, typing is disabled so filtering doesn't occur and filterMode has no effect.

**Filter mode behavior examples**:

Assume options: ["United States", "Canada", "United Kingdom", "Mexico"]

**SingleToken examples**:
- User types "uni" → matches: United States, United Kingdom (both contain "uni")
- User types "us uk" → matches: United States (has "us"), United Kingdom (has "uk"), United States (also has "uk"?), both match because they containANY tokens
- User types "can m" → matches: Canada (has "can"), Mexico (has "m")

**MultiToken examples**:
- User types "uni" → matches: United States, United Kingdom (same as SingleToken)
- User types "us king" → matches: United Kingdom (has both "us" and "king" tokens)
- User types "uni can" → NO matches (no option contains both "uni" AND "can" tokens)

**StartsWith examples**:
- User types "uni" → matches: United States, United Kingdom (both start with "uni")
- User types "u" → matches: United States, United Kingdom (both start with "u")
- User types "king" → may match: United Kingdom (if checking starts-with-word boundary) OR no matches

**Important interaction with filterKeys**: The filterKeys prop controls WHICH properties of option objects are used for filtering. filterMode controls HOW the matching works within those properties. For example, with filterKeys=["label", "description"] and filterMode="MultiToken":
- Options match if BOTH the label AND description contain the query tokens
- Useful for comprehensive search across multiple properties

**Important interaction with caseSensitiveFilter**: The caseSensitiveFilter prop controls whether matching is case-sensitive or case-insensitive. This applies to all filterMode values uniformly, but the sensitivity of different modes may vary:
- For StartsWith mode: "US" vs "us" may behave differently based on caseSensitiveFilter
- For SingleToken/MultiToken: token-based matching may be more or less sensitive to case depending on implementation

**Visual behavior during filtering**:
- As users type, the combo-box dropdown shows only matching options
- When no options match, the dropdown may show "No results" or similar message
- The filtering is real-time (happens as characters are typed, so typing is responsive)

**Important behavior with custom values**: For combo-boxes with allowCustomValue=true, filterMode affects howOPTIONSnarrow but doesn't affect when custom values are accepted. Custom values accept any text typed by the user, regardless of what filtering produced for standard options.

**Code pattern - choosing right filterMode**:

**Use SingleToken when**:
```typescript
filterMode = "SingleToken"; // Default - flexible matching
// Good for: Users may not type full words, want suggestions based on any part
// Example: User types "states" → matches "United States" (contains "states")
```

**Use MultiToken when**:
```typescript
filterMode = "MultiToken"; // Stricter - requires all tokens
// Good for: Users typing multiple terms, want exact all-term matching
// Example: User types "america north" → matches "North America" (contains both)
```

**Use StartsWith when**:
```typescript
filterMode = "StartsWith"; // Most strict - prefix matching
// Good for: Users want predictive typing, autocomplete-like behavior
// Example: User types "unit" → matches "United States", "United Kingdom"
```

**Supporting filter optimization**: The source code notes that exact fuzzy search algorithms couldn't be fully traced, but the basic behavior patterns are:
- SingleToken: Token-based matching, ANY token matches
- MultiToken: Token-based matching, ALL tokens must match  
- StartsWith: Prefix-based matching, starts-with or starts-word matches
- Actual scoring/sorting algorithms not fully documented in available source

**Important behavior with grouped options**: When options are grouped and filtering is active:
- FilterMode applies to option labels within groups
- If a group contains some matching and some non-matching options, the group is shown with only its matching options visible
- Non-matching options are hidden during filtering
- If a group has NO matching options at all, the entire group (including header) is typically hidden

**Code example - filtering with groups**:
```typescript
options = [
  { label: "Americas", items: [
    { value: "us", label: "United States" },
    { value: "ca", label: "Canada" },
    { value: "mx", label: "Mexico" }
  ]},
  { label: "Europe", items: [
    { value: "uk", label: "United Kingdom" },
    { value: "fr", label: "France" }
  ]}
];

filterMode = "SingleToken";

// User types "uni":
// Shows:
// Americas (group): United States (matches)
// Europe (group): United Kingdom (matches)
// Canada, Mexico, France hidden (don't contain "uni")
```

**Important role in combo-box performance**: Different filterMode values may have different performance characteristics:
- **SingleToken**: Generally fastest as it can exit early on first token match
- **MultiToken**: Slower as it must check all tokens against each option
- **StartsWith**: Performance depends on implementation (stringstartsWith is typically very fast)

For very large option lists (1000+ items), filterMode choice can impact typing responsiveness.

**Code pattern - performance considerations**:
```typescript
// For large option sets
options = this.getLargeDataset(5000); // Many options

// Choose simpler filterMode for better performance
filterMode = "StartsWith"; // Faster than MultiToken
caseSensitiveFilter = false; // Case-insensitive more performant than case-sensitive usually
```

**Dynamic filterMode switching**: You can change filterMode based on user preferences or context:
```typescript
this.filterMode = this.advancedSearch ? "MultiToken" : "SingleToken";

// Users choose search precision:
// Simple mode: flexible, matches any word
// Advanced mode: strict, matches all words
```

**Use cases for each filterMode**:

**SingleToken**:
- **General purpose**: Most users prefer flexible matching; suggestions based on any part of what they type
- **Fuzzy matching**: Useful when users don't know exact spellings or type partial words
- **Broad search**: Good for discovery where you want maximum suggestions back

**MultiToken**:
- **Multi-word queries**: Users typing multiple terms want all terms to be present (like "america north" vs "north america")
- **Narrowed search**: Good for filtering down from large option lists with multiple criteria
- **Precise selection**: When users want exact multi-term matching

**StartsWith**:
- **Autocomplete behavior**: Useful when users benefit from predictive, ordered suggestions
- **Code-like values**: Good for structured values where prefix matching makes sense (e.g., country codes, categories)
- **Performance-critical**: When you need fastest filtering behavior for large datasets

**Code example - filtering with multi-select**:
```typescript
multiSelect = true;
filterMode = "MultiToken";
allowCustomValue = false; // Only select from options

// User workflow:
// 1. Types "america north" → shows "North America"
// 2. Selects it → multiSelect adds it to selections
// 3. Types "asia" → shows Asian countries 
// 4. User continues building multi-option selection
```

**Code pattern - custom filtering augmentation**:
```typescript
// Can combine filterMode with custom additional filtering
options = this.baseOptions.filter(option => {
  // Apply business rules in addition to filterMode matching
  return this.isOptionAvailableForUser(option);
});

// filterMode handles text matching
// Custom filter handles business logic
```

**Interaction text search**: FilterMode applies to the label text (and other filterKeys properties). It doesn't affect:
- Filtered options show their full label display, even though only matched portion triggered the matching
- Disabled options: FilterMode respects disabled state - disabled options are filtered normally but shown as disabled
- Custom value entry: filterMode only affects standard options, not custom value acceptance

**Best practices for filterMode**:
- **Default to SingleToken**: Most flexible and generally preferred by users
- **Consider MultiToken for power users**: More exact matches for precision-focused workflows
- **Use StartsWith for predictable ordering**: When you want simple, ordered suggestions
- **Combine with filterKeys**: For comprehensive matching across multiple properties
- **Test with actual users**: The "best" filterMode varies significantly by user mental model and use case

**Code pattern - adaptive filterMode**:
```typescript
// Adapt based on query complexity
onInputTextChange(text) {
  if (text.includes(' ')) {
    // Contains space has multiple potential tokens
    this.filterMode = 'MultiToken';
  } else {
    // Single word or partial word
    this.filterMode = 'SingleToken';
  }
}
```

This prop is behavioral and fundamental to combo-box's filtering capabilities. It controls the matching algorithm that makes type-to-filter effective, and works in combination with filterKeys and caseSensitiveFilter for comprehensive search behavior.

Values:
- `SingleToken`: Matches individual tokens/words (default)
- `MultiToken`: Matches multiple tokens
- `StartsWith`: Matches beginning of strings

Usage: `filterMode="MultiToken"`

## filterKeys

Specifies which properties of option objects are used for filtering. Default is ['label'], but can be extended to other properties like description or custom fields. Only applies when disableEdit=false. This is a configuration prop that controls WHERE the filtering happens within each option object's data structure.

**Filter keys behavior and usage**:

- **filterKeys not set (defaults to ["label"])**: Filtering only occurs within the `label` property of each option object. User queries are matched against the label text only, and other option properties (description, custom fields) are not considered for matching.

- **filterKeys set to array of properties (e.g., filterKeys=["label", "description"])**: Filtering occurs within ALL specified properties. An option matches if the user's query finds a match in ANY of the specified properties (based on filterMode). This enables multi-property searching, useful when options need to be searchable by multiple attributes.

**Important relationship with disableEdit**: The filterKeys prop only applies when disableEdit=false (users can type to filter options). When disableEdit=true, typing is disabled so filtering doesn't occur and filterKeys has no effect.

**Filter keys matching behavior**:

**Single property (default) - ["label"]:**
```typescript
options = [
  { value: "us", label: "United States", description: "North America" }
];

filterKeys = ["label"]; // Default

User types "america" → NO match (only searches in "label")
User types "united" → Match (finds "united" in "United States")
```

**Multiple properties - ["label", "description"]:**
```typescript
options = [
  { value: "us", label: "United States", description: "North America" }
];

filterKeys = ["label", "description"];

User types "america" → MATCH (finds "america" in "description: North America")
User types "united" → MATCH (finds "united" in "label: United States")
User types "north" → MATCH (finds "north" in "description: North America")
```

**Important interaction with filterMode**: The filterKeys prop specifically controls WHERE matching occurs (which property), while filterMode controls HOW matching works (what kind of matching). Together they enable comprehensive multi-property search:

```typescript
options = [
  { value: "us", label: "United States - USA", code: "US", region: "Americas" }
];

filterKeys = ["label", "code", "region"];
filterMode = "MultiToken";

User types "uni americas" → MATCH (both terms found in label and region)
User types "us us code" → MATCH ("us" in label and region, "code" in label)
User types "us" → MATCH (found in label, code, and region - just needs one for SingleToken)
```

**Important interaction with caseSensitiveFilter**: The caseSensitiveFilter prop applies uniformly across all filterKeys properties - either all properties are case-sensitive or all are case-insensitive. You cannot have case-sensitive matching on some properties but case-insensitive on others within the same filterKeys array.

**Code pattern - comprehensive multi-property search**:
```typescript
// Setup options with multiple searchable properties
options = [
  { value: "us", label: "United States", code: "US", codeNum: 840, description: "USA" },
  { value: "ca", label: "Canada", code: "CA", codeNum: 124, description: "Canada North America" },
  { value: "mx", label: "Mexico", code: "MX", codeNum: 484, description: "Mexico" }
];

// Configure multiple filter keys
filterKeys = ["label", "code", "codeNum", "description"];

// Users can search by any property:
// - "united" → matches (label)
// - "US" → matches (code)
// - "840" → matches (codeNum)
// - "america" → matches (description)
```

**Important behavior missing properties**: If filterKeys references properties that don't exist on some options:
- Properties that don't exist are simply ignored (don't cause errors)
- Only properties that actually exist on each option contribute to matching
- This allows flexible schema where different options might have different properties

**Code pattern - flexible schema matching**:
```typescript
options = [
  // Option with full schema
  { value: "us", label: "United States", code: "US", region: "Americas" },
  
  // Option with partial schema
  { value: "ca", label: "Canada" }, // Missing code, region
  
  // Option with different fields
  { value: "custom", label: "Custom Service", sku: "CS-12345" } // Has sku instead of code, region
];

filterKeys = ["label", "code", "region", "sku"];

// All options match against properties they actually have:
// - "us" matches in label, code, region
// - "ca" matches only in label (other properties don't exist)
// - "custom" matches in label and sku
```

**Important behavior with grouped options**: When options are organized into groups (IDropdownOptionGroup), filterKeys applies to the options within groups, not to group labels themselves:
```typescript
options = [
  { label: "Americas", items: [
    { value: "us", label: "United States", code: "US", description: "USA" }
  ]}
];

filterKeys = ["label", "description"];

User types "america" → NO match ("Americas" group label not in filterKeys)
User types "usa" → MATCH (finds "usa" in description within the group)
```

**Use cases for multiple filterKeys**:

**Comprehensive search** - Search across multiple data points:
```typescript
// Users can find countries by name, code, or description
filterKeys = ["label", "code", "description"];
// User types "840" → finds US (numeric code search)
// User types "america" → finds countries with that keyword
// User types "US" → finds United States (code search)
```

**Flexible data matching** - Different users search differently:
```typescript
// Some users prefer names, others prefer codes
filterKeys = ["label", "code", "sku", "productID"];
// Power users: know the codes exactly (fast search)
// New users: prefer descriptive labels (search by name)
```

**Attribute-specific search** - Target specific types of data:
```typescript
// Server selection: search by hostname, IP, or description
filterKeys = ["hostname", "ipAddress", "description"];
// Network admin: knows IPs (search "192.168.1.1")
// Service team: knows descriptions (search "payment gateway")
```

**Internationalization** - Support multiple naming conventions:
```typescript
// Products with names in multiple languages
filterKeys = ["nameEN", "nameES", "nameFR", "productCode"];
// Spanish user: searches "estados unidos" (nameES: "Estados Unidos")
// French user: searches "états-unis" (nameFR: "États-Unis")
```

**Important performance considerations**: More filterKeys = more properties to check = potentially slower filtering, especially for large option lists:
- Fewer filterKeys = faster filtering, but limited search functionality
- More filterKeys = more comprehensive search, but potentially slower
- Balance search comprehensiveness with performance for your use case

**Code pattern - performance vs. search depth**:
```typescript
// Fast but limited search (fewer properties)
filterKeys = ["label"]; // Default - fastest
// Good for: 10,000 options, need responsive typing

// Comprehensive search (all properties)
filterKeys = ["label", "code", "description", "category", "tags"]; 
// Good for: 200 options, need comprehensive search between many attributes

// Smart filtering (conditional)
get smartFilterKeys(): string[] {
  if (this.options.length > 500) {
    return ["label"]; // Fast but limited
  } else {
    return ["label", "code", "description"]; // Comprehensive
  }
}
```

**Important behavior with custom values**: For combo-boxes with allowCustomValue=true, filterKeys only affects PREDEFINED options. Custom values are always accepted based on user input, not based on filtering against properties.

**Code example - real-world filterKeys configuration**:
```typescript
// Customer service ticket categorization
options = [
  { 
    id: 101, 
    name: "Billing Issue", 
    category: "Finance", 
    keywords: ["invoice", "payment", "bill"],
    description: "Problems with billing or payment"
  },
  {
    id: 102,
    name: "Technical Support",
    category: "IT", 
    keywords: ["broken", "crash", "error"],
    description: "Service technical problems"
  }
];

filterKeys = ["name", "category", "keywords", "description"];

// Comprehensive search across all properties
filterMode = "MultiToken";

// User examples:
// - types "billing" → matches (name, description, keywords)
// - types "finance" → matches (category: Finance)
// - types "crash error" → matches (MultiToken: both in keywords)
```

**Code pattern - dynamic filterKeys**:
```typescript
// Change filterKeys based on user role or context
this.filterKeys = this.adminUser 
  ? ["label", "code", "description", "internalID", "notes"] // Comprehensive for admins
  : ["label", "description"]; // User-friendly for regular users
```

**Important best practices for filterKeys**:
- **Start with label**: Always include "label" in filterKeys as it's the primary user-facing text
- **Add common identifiers**: Include code, id, or similar fields users might know
- **Consider performance**: More properties = slower filtering for large datasets
- **Test with actual users**: Users search in surprising ways - watch what they actually need
- **Document searchable properties**: Help users understand they can search by name, code, etc.

**Code pattern - valid property checking**:
```typescript
// Ensure filterKeys only reference existing properties to avoid warnings
get safeFilterKeys(): string[] {
  const existingProps = this.options.reduce((props, option) => {
    return new Set([...props, ...Object.keys(option)]);
  }, new Set<string>());
  
  return this.filterKeys.filter(key => 
    existingProps.has(key)
  );
}
```

This prop is configuration-specific and works in close combination with filterMode to control WHERE and HOW filtering matches user queries against option data. It enables comprehensive multi-property search while maintaining performance characteristics appropriate for your dataset size.

Usage: `filterKeys="['label', 'description']"`

## caseSensitiveFilter

Determines whether filtering considers case matching (caseSensitiveFilter=true) or performs case-insensitive matching (caseSensitiveFilter=false). Only applies when disableEdit=false.

**Case sensitive filter behavior**:

- **caseSensitiveFilter=false (default)**: Filtering is case-insensitive. User queries match options regardless of letter case. For example, "US" matches both "United States" and "united states" regardless of how the user types it. This is more user-friendly as users don't need to be exact about capitalization.

- **caseSensitiveFilter=true**: Filtering requires exact case matching. User queries must match the option text exactly, including capitalization. For example, "us" only matches if the option contains "us" (lowercase) but not "US" (uppercase). This is more restrictive and typically used when case matters for matches.

**Important relationship with disableEdit**: Only applies when disableEdit=false (users can type to filter). When disableEdit=true, typing is disabled so filtering doesn't occur.

**Code examples**:
```typescript
options = [
  { value: "us", label: "United States" },
  { value: "ca", label: "Canada" }
];

caseSensitiveFilter = false; // Default
User types "us" → matches "United States" (case-insensitive)

caseSensitiveFilter = true;
User types "us" → no match (exact case needed)
User types "US" → may match if option contains "US"
```

**Use cases**:
- **false (default)**: Most user-friendly, typical web behavior
- **true**: Technical scenarios where case distinction matters (e.g., codes, identifiers)

**Performance note**: Case-insensitive filtering may be slightly slower than case-sensitive matching but typically the difference is negligible for most dataset sizes. The implementation typically converts both query and options to common case for comparison.

**Important interaction with filterMode**: Applies uniformly across all filterMode values (SingleToken, MultiToken, StartsWith). All filtering modes follow the same case sensitivity setting.

Usage: `caseSensitiveFilter="true"`

## disableDefaultSorting

Controls whether options are automatically sorted based on matching scores (disableDefaultSorting=false) or maintain their original order (disableDefaultSorting=true). Only affects filtering behavior when disableEdit=false.

**Default sorting behavior and use cases**:

- **disableDefaultSorting=false (default)**: Options are automatically sorted/reordered based on their matching quality to the current search query. Best matches appear first in the results list. This provides a better user experience by showing the most relevant options at the top. Sorting considers factors like match position, match exactness, and other scoring factors.

- **disableDefaultSorting=true**: Options maintain their original ordering from the options array prop, regardless of how well they match the search query. This is useful when you want maintain a specific order (alphabetical, geographic, user-defined ordering, etc.) and don't want filtering to rearrange results.

**Important relationship with filtering disableEdit**: Only applies when disableEdit=false. If disableEdit=true (no typing/filtering), disableDefaultSorting has no effect since options don't get reordered.

**Code examples**:
```typescript
options = [
  { value: "ca", label: "Canada" },
  { value: "us", label: "United States" },
  { value: "uk", label: "United Kingdom" }
];

disableDefaultSorting = false; // Default
User types "uni" → Results reordered to: "United States", "United Kingdom", "Canada"
                                                    (best matches first)

disableDefaultSorting = true;
User types "uni" → Results maintain: "Canada", "United States", "United Kingdom"
                                      (original order preserved)
```

**Important behavior with grouped options**: When options are grouped:
- disableDefaultSorting typically applies within each group (options within a group are ordered by match quality)
- The group headers themselves typically maintain their defined order
- Optional: Some implementations may reorder groups themselves based on best-matching options within groups

**Use cases**:
- **disableDefaultSorting=false (default)**: Most use cases where you want best matches first for better UX, common scenario for search boxes
- **disableDefaultSorting=true**: Geographic arrangement where countries should stay in region order, alphabetical lists where exact ordering matters, user-defined prioritization

**Interaction with multi-select**: In multi-select scenarios, disableDefaultSorting only affects the visual order in the dropdown. It doesn't change how selections are stored, displayed, or processed in value change events.

**Performance note**: Sorting based on match quality adds computational overhead to filtering operations. For very large datasets with heavy user typing, disabling sorting can improve typing responsiveness. For most typical dataset sizes, the performance difference is negligible.

**Important nuance with custom values**: When allowCustomValue=true and disableDefaultSorting=true:
- Standard options maintain their original order in filtering results
- Custom values (if displayed in dropdown) may appear at designated position (often beginning or end) regardless of sorting
- Original order preservation applies primarily to the predefined options list

**Code patterns**:
```typescript
// Geographic arrangement - maintain region order
options = [
  { label: "Americas", items: [US, CA, MX] },
  { label: "Europe", items: [UK, FR, DE] }
];
disableDefaultSorting = true; // Maintain region order

// Alphabetical - maintain alphabetical consistency
options = [
  { value: "ar", label: "Argentina" },
  { value: "au", label: "Australia" },
  { value: "at", label: "Austria" }
];
disableDefaultSorting = true; // Keep alphabetical order

// Smart search with best matches first (default)
options = /* large dataset */;
disableDefaultSorting = false; // Best matches at top
```

**Important difference from sorting by basic properties**: disableDefaultSorting controls sorting based on MATCHING RELEVANCE to the current search query, not based on basic properties like alphabetical order or data values. To maintain a fixed order based on fundamental sorting (alphabetical, priority), set disableDefaultSorting=true.

**Important role in combo-box vs dropdown**: For combo-box, the filtering experience matters more because users continuously type and see rapidly updating results. Provided that sorting adds minimal overhead but should show the best matches first (disableDefaultSorting=false). The design system has defaults that balance UX and performance.

**Code pattern - context-aware sorting**:
```typescript
useRelevanceBasedSorting() {
  // Use default sorting when searching for best matches
  this.disableDefaultSorting = false;
  
  // Maintain fixed order when users know what they want
  this.disableDefaultSorting = true;
}
```

**Best practices**:
- **Default to false for search interfaces**: Users generally prefer best matches at top
- **Set true for structured data**: When the order itself conveys information (regional, alphabetical grouping)
- **Consider dataset size**: For large datasets, sorting overhead may be noticeable
- **Test with actual users**: Some users prefer consistent order to dynamic ordering

Usage: `disableDefaultSorting="true"`

## disableSpellCheck

Disables browser spell checking in the combo-box input field. This is a behavioral prop that controls the browser's built-in spell checking functionality. This is particularly important for combo-box because the input field serves dual purpose: text entry for custom values AND filtering of options, where spell checking could be disruptive.

**Disable spell check behavior**:

- **disableSpellCheck=false (default)**: The combo-box input field has browser spell checking enabled. As users type, the browser underlines potential spelling errors (typically with red squiggles). This can be distracting in a combo-box because:
  - Users are often typing partial words, codes, or identifiers for filtering purposes
  - Spell checking underlines interfere with the filtering experience
  - Users typing code snippets, APIs, or technical terms get false-positivespell errors
  - The visual clutter of spell checking underlines makes the combo-boxfield look error-prone when users are simply searching

- **disableSpellCheck=true**: The combo-box input field has browser spell checking disabled. When users type, there are no spell check underlines. This provides:
  - Cleaner visual appearance during typing and filtering
  - Better user experience for technical terms, codes, and identifiers
  - Reduced visual distraction during the search/selection process
  - Only affects the input field's appearance; filtering functionality remains unchanged

**Important relationship with disableEdit**: Only applies when disableEdit=false (users can type). When disableEdit=true (no typing), disableSpellCheck has no effect since the input field is read-only and spell checking wouldn't be relevant.

**Important relationship with custom values**: For combo-boxes with allowCustomValue=true, the input field serves both filtering AND custom value entry:
- During filtering: Users type partial matches (spell checking would be distracting)
- During custom value entry: Users type complete values (spell checking might be wanted)
- The prop applies uniformly to both use cases - can't have different spell settings for filtering vs. custom value entry

**Use cases for each mode**:

**disableSpellCheck=true (recommended for most combo-box)**:
- **Technical content**: Users type codes, identifiers, or technical terms that trigger false spell errors
- **APIparametersearching**: Complex values like API endpoints, query strings, or structured identifiers
- **Short-form search**: Users type partial words for filtering purposes (not full sentences)
- **Language-agnostic**: Multi-language contexts where spell checking can't handle all languages properly
- **Database IDs**: Numeric codes, database IDs, or machine identifiers that don't follow natural language rules

**disableSpellCheck=false**: 
- **Natural language entry**: When users primarily enter natural language text (names, descriptions) where spell checking could be helpful
- **Form completion**: When combo-box field is primarily for typing natural language descriptions rather than filtering options
- **User documentation**: Thewhen users are entering free-form text where spell checking would genuinely help them catch typos
- **Email or URL entry**: When the combo-box accepts custom emails, URLs, or other natural language values where spell checking might be useful

**Important performance and behavior considerations**:
- disablespellcheck affects only the visual underline appearance during typing browser-side
- One might think this impacts performance;: Actually, the browser仍 processes all typing events identically - only the visual red squiggle underline is removed
- Filtering happens identically in both cases - this is purely visual

**Code pattern - technical content combo-box**:
```typescript
// Server/API selection combo-box with technical content
disableEdit = false; // Allow typing
allowCustomValue = true; // Allow API endpoints as custom values
disableSpellCheck = true; // Disable spell checking for technical terms

// Users can type: "https://api.myservice.com/v2/users"
// Without red underlines for "https://api.myservice.com" being flagged
```

**Important interaction with popular UI patterns**: Most web interface design guidelines recommend disabling spell checking for:
- Search inputs (like combo-box filtering behavior)
- Password fields
- URL entry
- Technical identifiers
- Email addresses

The combo-box fits primarily in the search/technical category, explaining why disableSpellCheck=false is often disruptive UX.

**Code pattern - behavior by form context**:
```typescript
// Example 1: Standard form field that looks combo-boxish
// Maybe for entering company names where spell checking could help
disableSpellCheck = false; // Help catch typos in company names

// Example 2: Technical parameter selector
// Where users type codes and identifiers that don't follow natural language rules
disableSpellCheck = true; // Don't flag "api-v2-endpoint-123" as spelling error
```

**User experience difference**:

**disableSpellCheck=false (enabled)**:
```
Some partial typed text shows squiggly underlines for "errors" that are actually just partial words used for filtering:
[My serv___]
```

**disableSpellCheck=true (disabled)**:
```
Same typing appears clean without underlines:
[My serv___]
```

**Important distinguishing factor**: The difference isn't in validation or filtering behavior - it's purely in the browser's visual indication of potential spelling errors. For combo-box where users are primarily filtering options, these "errors" are typically false positives and create visual distraction.

**Code pattern - convenience setting**:
```typescript
// In component configuration
disableSpellCheck: boolean = true; // Default to true for combo-box

// For specific use cases where natural language entry isprimary
get effectiveDisableSpellCheck(): boolean {
  // When custom values are natural language texts, spell checking helpful
  if (this.allowsNaturalLanguage && this.allowCustomValue) {
    return false;
  }
  // Default case: technical content, search focused
  return true;
}
```

**Important collaboration with validation**: The disableSpellCheck prop only affects the browser's visual spell checking underline. It doesn't affect:
- Validation logic (validationState, validationMode, required validation)
- Field validation feedback
- Custom validation you implement
- Actual data validation - typos can still be committed or rejected based on your validation logic

**Code pattern - separate concerns**:
```typescript
// Visual spell checking disabled
disableSpellCheck = true; // Cleaner appearance during typing

// Actual validation still works
validationMode = "onBlur";
required = true;
// These validate when user commits, regardless of spell checking
```

**Mobile behavior**: On mobile devices (especially iOS), spell checking behavior may differ:
- Some mobile browsers handle spell checking differently
- iOS may not show squiggly underlines in the way desktop does
- The prop still sets the HTML spellcheck attribute appropriately
- Cross-platform testing recommended if mobile UX is priority

**RTL (Right-to-Left) language considerations**: Spell checking behavior may vary for RTL languages:
- Some spell checker implementations have better/worse support for RTL
- Consider user language context when deciding whether to override browser defaults
- RTL users might have different expectations about when spell checking is appropriate

**Code pattern - language-aware configuration**:
```typescript
get disableSpellCheck(): boolean {
  // For languages where spell checking might be less accurate or helpful
  if (this.userLanguage.startsWith('ar') || this.userLanguage.startsWith('he')) {
    return true; // RTL languages - automatic disable
  }
  // For content-heavy definitions over strict technical
  if (this.isTechnicalContent) {
    return true; // Override for technical content regardless of language
  }
  // Default: browser spell checking disabled (combo-box typical behavior)
  return true;
}
```

**Common patterns**:
- **Default to true*** for most use cases where combo-box behavior is primarily filtering/selection
- **Consider false** for free-form natural language entry rather than pre-defined option selection
- **Consider false** when allowCustomValue=true and custom values are primarily natural language (descriptions, comments)
- **Consider performance** (though impact is minimal) - only affects visual underline rendering

**Important distinction from validation**: DisableSpell focuses purely on browser-side visual spell checking while validation focuses on business rules and data integrity. Both are independent and serve complementary purposes:
-DisableSpell check: Visual appearance, crime candidate identification
- Validation: Business logic enforcement, data integrity, required field checking

**Code pattern - handling both**:
```typescript
// Visual: Disable browser spell checking for cleaner appearance
disableSpellCheck = true;

// Actual validation: Apply custom validation logic
this.validateCustomValue = (value: string) => {
  if (value.length > 100) return false; // Length validation
  if (!/^[\w\s-]+$/.test(value)) return false; // Character validation
  if (this.existsInBlacklist(value)) return false; // Business rule validation
  return true;
};
```

**Important accessibility implications**:
- Spell checking underlines can create visual noise for screen reader users
- Some screen readers announce spell checking errors which could be distracting for combo-box filtering
- DisableSpellCheck=true generally improves accessibility for screen reader users in combo-box contexts
- Consider accessibility impact when deciding whether to override browser defaults

**Code pattern - accessibility‑focused**:
```typescript
// Accessibility: Disable spell checking for cleaner screen reader experience
disableSpellCheck = true;

// Provide any validation feedback through dedicated UX instead of browser squiggles
this.validationState = this.hasErrors ? "invalid" : "valid";
this.helperMessage = this.hasErrors ? "Please enter a valid value" : "";
```

**Best practices**:
- **Default to true** for most combo-box configurations where filtering/searching is primary use case
- **Be explicit** about why you're overriding browser spell check defaults if setting to false
- **Document behavior** in UX guidelines or component documentation
- **Test with actual users** to determine whether the visual indicating helps or hinders their workflow
- **Consider form context** - Some forms benefit from spell checking on similar fields

**Code pattern - documentation**:
```typescript
// In component documentation:
/**
 * @property disableSpellCheck - Disable browser spell checking
 * @description 
 *   Recommended: true (default) - cleaner appearance during filtered searching
 *   Set to false: when combo-box primarily accepts natural language 
 *                 descriptions where spell checking could help catch typos
 * @example Technical content (API endpoints, codes)
 *   disableSpellCheck = true; // Don't flag "https://api..." as spelling error
 * @example Natural language entry (descriptions, notes)
 *   disableSpellCheck = false; // Help catch typos in plain text descriptions
 */
```

This prop is behavioral and affects only the browser's visual spell check rendering. It's particularly important for combo-box because the input field serves dual purpose (filtering and potential custom value entry) where spell checking can be more disruptive than helpful.

Usage: `disableSpellCheck="true"`

## hideArrowButton

Hides the dropdown arrow button, useful for creating custom dropdown triggers. When true, removes the arrow icon indicator that shows users they can open the dropdown. This is a visual prop that affects the component's appearance while maintaining the dropdown opening functionality. For combo-box, this is often used when you want cleaner appearance or when you provide alternative ways to indicate dropdown availability.

**Hide arrow button behavior**:

- **hideArrowButton=false (default)**: The standard arrow icon (typically a downward triangle or chevron) appears at the end of the combo-box field, providing a clear visual affordance that clicking will open the dropdown menu. The arrow icon:
  - Appears when the combo-box is enabled (disabled=false, readOnly=false)
  - Changes appearance when dropdown is open/closed (rotation, color change)
  - Provides visual feedback for dropdown state
  - Standardized UI pattern familiar to most users

- **hideArrowButton=true**: The arrow icon is removed from the combo-box field. The dropdown still opens when users click on the field, but there's no visible arrow indicator. This creates:
  - Cleaner, more minimal appearance
  - Potentially less obvious dropdown affordance
  - May require other visual cues to indicate dropdown capability

**Important relationship with disableEdit and interaction**: The dropdown functionality remains available regardless of hideArrowButton:
- Users can still click anywhere on the field to open dropdown
- Keyboard users can still use arrow keys or space/enter to open
- The field focus and blur behaviors work identically
- Only the visual arrow indicator is removed, not the interaction capability

**Use cases for hiding arrow button**:

**Minimal design aesthetic**: When you want a cleaner, more minimal appearance that doesn't show the arrow icon for space or design reasons.

**Custom triggers**: When you provide alternative ways to indicate and trigger dropdown:
```typescript
hideArrowButton = true;
// Field shows clean text without arrow
// Dropdown still opens on field click
// May combine with custom UI elements elsewhere
```

**Custom dropdown controls**: When implementing completely custom dropdown interaction patterns:
```typescript
hideArrowButton = true;
// Field looks like a text input rather than dropdown
// You provide custom buttons elsewhere to open
// Example: "Browse" button next to field opens dropdown
```

**Space optimization**: When the arrow consumes too much space and you want to maximize field width for displayed text.

**Mobile optimization**: When arrow indicators may be confusing or unnecessary in mobile contexts where tap patterns differ.

**Important accessibility considerations**: The arrow icon provides an important affordance for users to understand that the field is interactive and contains dropdown options. When hiding the arrow, ensure users still have other clear indicators:
- Clear label and placeholder that suggest selection capability
- Focus states that show interactivity  
- Cursor changes that indicate clickability
- Consistent spacing and layout that follows typical dropdown patterns

**Code pattern - custom dropdown triggers**:
```typescript
hideArrowButton = true;
multiSelect = false;

// Provide custom "Browse" button that opens dropdown
this.comboBox.openDropdown();

// Or use button that shows custom modal/panel with selection UI
```

**Important interaction with endEnhancer**: When both hideArrowButton=true and endEnhancer is set:
- The end enhancer (if any) becomes the primary end-of-field interactive element
- Users interact with the end enhancer rather than the arrow for dropdown indication
- This is common pattern for custom dropdown triggers (e.g., calendar icon for date dropdown)

**Code示例 - hide arrow, custom trigger**:
```typescript
hideArrowButton = true;

// Replace with custom end enhancer
endEnhancer = {
  type: "icon",
  value: "calendar"  // Calendar icon indicates date picker dropdown
};

// Field shows: [Date input] [calendar icon]
// Calendar icon clicked → opens date dropdown

// Traditional dropdown would show: [Date input] [calendar icon] [⬇]
```

**Important behavior with showSelectAll**: When showSelectAll=true and hideArrowButton=true, the Select All checkbox is still shown in the dropdown menu when it's open, but the field itself lacks the arrow indicator.

**Code pattern - mobile-friendly custom triggers**:
```typescript
// Mobile: Hide arrow, add custom "Select" button
hideArrowButton = true;

// Desktop: Show standard arrow (default)
hideArrowButton = false; 

// Responsive approach for different platforms
get hideArrowButton(): boolean {
  return this.isMobile; // Custom trigger preferred on mobile
}
```

**Important role in combo-box vs dropdown**: For combo-box, the arrow indicator is particularly important because the component serves dual purpose as text input AND dropdown. Users might expect:
- Text input behavior (type to filter) vs dropdown behavior (click to expand)
- Arrow helps clarify the dropdown aspect of the component
- When hiding arrow, ensure other UI elements make the dropdown functionality clear

**Code pattern - indicating dropdown without arrow**:
```typescript
hideArrowButton = true;

// Provide clear indicators through other means:
this.placeholder = "Click to select or type to search";
this.helperMessage = "Type to filter options or click dropdown icon to see all";
// Custom styling that hints at dropdown capability on hover/focus
```

**Common patterns with hideArrowButton**:

**Clean minimal design**:
```typescript
hideArrowButton = true;
// Field appears like standard text input
// Dropdown still opens on click
// Minimal appearance with full functionality
```

**Custom dropdown with complex interaction**:
```typescript
hideArrowButton = true;
// Field shows selected value/text as if it's editable
// Clicking doesn't just toggle dropdown - may open complex panel
// You provide custom interaction button(s)
```

**Paired with custom end enhancer**:
```typescript
hideArrowButton = true;
endEnhancer = {
  type: "icon-button",
  value: "search"
};
// Field shows: [Value] [Search icon]
// Search icon click triggers dropdown with search UI
// Arrow hidden because search icon serves as affordance
```

**IMPORTANT NOTE**: When hideArrowButton=true, ensure:
- Users have clear way to know dropdown exists (labels, instructions, custom affordances)
- Keyboard navigation still works (arrow keys, space/enter) - arrow is visual only
- Focus states clearly show interactivity (border color, background changes)
- Don't hide arrow AND prevent alternative dropdown triggers (users won't know how to access dropdown)

**Code pattern - maintaining interactivity without arrow**:
```typescript
hideArrowButton = true;

// Ensure these stay functional:
disableEdit = false; // Users can still type
// Focus indicator: Border changes on focus
// Hover context: Field changes appearance on hover
// User instructions: HelperMessage explains dropdown capability
```

**Accessibility considerations with hidden arrow**:
- The arrow icon provides an important affordance for screen reader users
- When hideArrowButton=true, ensure:
  - Component has proper ARIA roles (haspopup="listbox", etc.)
  - aria-label provides clear description of dropdown functionality
  - Focus management signals interactivity clearly
  - Alternative affordances provide same information visually

**Code pattern - accessible custom trigger**:
```typescript
hideArrowButton = true;

// Ensure accessibility with proper ARIA
this.ariaLabel = "Selectable options, click to open dropdown or type to search";
// plus proper haspopup attributes and keyboard interaction
```

**Best practices** when hiding arrow:
- **Provide alternative trigger/button** for opening dropdown
- **Use clear labels** that indicate dropdown capability
- **Maintain standard visual feedback** for focus/hover
- **Test with users** to ensure dropdown discoverability
- **Consider custom affordances** like icons, buttons that replace arrow
- **Document behavior** if interaction differs from standard dropdown pattern

**Code示例 - complete custom trigger implementation**:
```typescript
@Piece-friend(arrow replacement)
export class CustomComboBox {
  hideArrowButton = true;
  
  // Custom "Browse" button next to field
  openBrowser() {
    this.comboBox.openDropdown();
  }
}

// Template:
// <ion-combo-box [hideArrowButton]="true"></ion-combo-box>
// <button (click)="openBrowser()">Browse</button>

// User experience:
// Field shows selected value with clean input appearance
// "Browse" button provides clear affordance for dropdown access
// Clicking either works (field click or button click)
```

This prop is visual and affects only the appearance of the dropdown affordance indicator. It removes the standard arrow icon while maintaining the dropdown opening functionality, requiring you to provide alternative visual indicators and cues for users to understand the dropdown capability.

Usage: `hideArrowButton="true"`

## selectOptionsOnPaste

Enables automatic option selection when users paste text containing the separator character into the input field. When selectOptionsOnPaste=true, pasted text is split by separator and matching options are auto-selected. Only applies when multiSelect=true. Interacts with disableEdit - requires disableEdit=false for typing and paste functionality.

Usage: `selectOptionsOnPaste="true"`

## disableVirtualScroll

Explicitly disables virtual scrolling for the dropdown options. Virtual scroll is automatically enabled for dynamic options (when options is a function) or static options with 15+ items. disableVirtualScroll explicitly disables virtual scrolling even when it would normally be auto-enabled.

Usage: `disableVirtualScroll="true"`

## groupSelectedOptions

Controls how selected options are organized in the dropdown when multiSelect=true. When groupSelectedOptions=true, selected options are grouped together at the top of their respective groups; when false, selections stay in their original positions.

Usage: `groupSelectedOptions="false"`

## maxVisibleRows

Controls the number of rows used for displaying selected options. In collapsed mode, initially shows 1 row with +N overflow indicator that expands to maxVisibleRows. In wrap mode, constrains to maxVisibleRows with scroll overflow. Interacts with tagDisplay and overflowMode for final handling. Interacts with overflowMode - when overflowMode=scroll, all selected options are visible and scrollable; when overflowMode=clip, excess options are hidden and shown as +N counter.

Usage: `maxVisibleRows="3"`

## tagDisplay

Controls the layout behavior for tags vs non-tags display. Works with both disableTags=true and disableTags=false. Interacts with overflowMode - when tagDisplay=wrap and maxVisibleRows >= 3, scroll mode is used automatically; when tagDisplay=collapsed, clip mode shows +N counter.

**Tag display values and their behavior**:

- **tagDisplay="collapsed" (default)**: Shows single row of tags with +N overflow indicator that expands on click. This is the most common pattern for multi-select combo-box where users don't need to see all tags simultaneously. Collapsed mode:
  - Shows single row of tags (up to what fits in one line)
  - Displays "+X more" indicator showing how many additional tags exist
  - User clicks "+X more" or clicks within tag area to expand and see all tags
  - After expansion, shows up to maxVisibleRows of tags
  - Provides compact display while allowing view when needed
  - Important for space efficiency in forms

- **tagDisplay="wrap"**: Allows tags to wrap to multiple rows. This mode:
  - Tags flow to multiple lines as needed within the maxVisibleRows limit
  - No "+X more" overflow indicator needed (all visible tags shown directly)
  - Users can see more selections at once without expansion
  - Takes more vertical space in the field
  - Better when space allows and users need to see multiple selections simultaneously

**Important relationship with disableTags**: The tagDisplay prop affects layout behavior whether disableTags is true or false:

- **With disableTags=false (tags)**: tagDisplay controls how tags are arranged (collapsed vs wrapped)
- **With disableTags=true (text)**: tagDisplay controls how comma-separated text is arranged (collapsed vs wrapped within maxVisibleRows)

In both cases, tagDisplay provides consistent layout behavior for multiple items, though the visual appearance differs between tags and text.

**Important interaction with maxVisibleRows**: The maxVisibleRows prop limits how many rows of tags/text are displayed:
- **tagDisplay="collapsed"**: Initially shows 1 row with +N indicator, expands to maxVisibleRows on click
- **tagDisplay="wrap"**: Shows up to maxVisibleRows of tags wrapping naturally

**Important interaction with overflowMode**: The overflowMode prop controls how items beyond maxVisibleRows are handled:
- **overflowMode="clip"**: Excess items hidden and shown as +N counter
- **overflowMode="scroll"**: Makes the tag container scrollable

**Code examples and visual behavior**:

**Example 1: tagDisplay="collapsed" with maxVisibleRows=3**:
```
┌─────────────────────────────────┐
│ [US X] [CA X] [MX X] +5 more  │ ← 1 row + overflow indicator
└─────────────────────────────────┘

After clicking +5 more:
┌─────────────────────────────────┐
│ [US X] [CA X] [MX X]           │ ← Row 1
│ [UK X] [FR X] [DE X]           │ ← Row 2  
│ [ES X] [IT X] +2 more          │ ← Row 3 (at maxVisibleRows=3)
└─────────────────────────────────┘
```

**Example 2: tagDisplay="wrap" with maxVisibleRows=3**:
```
┌─────────────────────────────────┐
│ [US X] [CA X] [MX X] [UK X]   │ ← Row 1 (wrapping naturally)
│ [FR X] [DE X] [ES X] [IT X]   │ ← Row 2
│ [JP X] [CN X]                  │ ← Row 3 (at maxVisibleRows)
└─────────────────────────────────┘
```

**Important behavior withCustom values**: For combo-boxes with allowCustomValue=true:
- Custom values appear as tags just like selected options when disableTags=false
- Custom values follow the same tagDisplay layout rules (they're just tags like any others)
- No visual distinction between standard option tags and custom value tags unless custom styling applied

**Code pattern - choosing appropriate tagDisplay**:
```typescript
// Scenario 1: Many selections, limited space (collapsed preferred)
multiSelect = true;
disableTags = false;
tagDisplay = "collapsed"; // Single row + overflow

// Scenario 2: Fewer selections, more space (wrap preferred)  
multiSelect = true;
disableTags = false;
tagDisplay = "wrap"; // Show all selections visible

// Scenario 3: Dynamic based on selection count
get tagDisplay(): "collapsed" | "wrap" {
  return this.value.length > 5 ? "collapsed" : "wrap";
}
```

**Important interaction with mobile vs desktop**:
- **Mobile**: Collapsed mode is often preferred for touch interfaces and space constraints
- **Desktop**: Wrap mode may be preferred when screen space allows and users benefit from seeing more selections at once
- Consider form layout patterns when choosing

**Code pattern - responsive tagDisplay**:
```typescript
get tagDisplay(): "collapsed" | "wrap" {
  if (this.isMobile) {
    return "collapsed"; // Mobile: Single row + overflow
  } else {
    return "wrap"; // Desktop: Show more visible selections
  }
}
```

**Use cases for each mode**:

**tagDisplay="collapsed" (default)**:
- **Space-constrained forms**: When vertical space is limited and compact display needed
- **Mobile interfaces**: Better for touch UX and limited screen space
- **Many selections**: When 5-10+ selections and listing all would overwhelm the field
- **Clean aesthetic**: When you want minimal field appearance
- **Browse-then-select workflows**: Users primarily see completed selections, not managing individual items

**tagDisplay="wrap"**:
- **Visible selection management**: When users need to see and manage selections simultaneously
- **Fewer selections**: When typically 2-5 selections and space allows showing all
- **Status monitoring**: When field shows what's selected as part of status display
- **Desktop layouts**: When vertical space available and seeing all selections helpful
- **Interactive refinement**: When users frequently add/remove items and seeing all selections speeds decisions

**Important behavior for form layout**: The choice of tagDisplay affects how the field interacts with surrounding form elements:

**Collapsed:**
- Field height is more predictable (single row primarily)
- Fits better in tight form layouts
- Less reflow of surrounding content when selections vary
- Consistent field height regardless of selection count

**Wrap:**
- Field height varies based on selection count (within maxVisibleRows)
- May cause more layout reflow if selection count changes frequently
- Better for showing complete selection state at a glance
- Height more dynamic but bounded by maxVisibleRows

**Code pattern - form layout integration**:
```typescript
@Comp市场的ar{}
export class FormComponent {
  // Choose tagDisplay based on form layout constraints
  multiSelect = true;
  
  get tagDisplay(): "collapsed" | "wrap" {
    if (this.isCompactForm) {
      return "collapsed"; // Save space in tight layout
    } else {
      return "wrap"; // Use available space in standard layout
    }
  }
}
```

**Important role in accessibility**:
- **Collapsed mode**: Screen readers may announce "5 selected, click arrow to see details" rather than listing all items - requires users to expand inventory
- **Wrap mode**: Screen readers can announce all selections without requiring expansion - better accessibility for visibility
- Consider your accessibility requirements when choosing between modes

**Code pattern - accessibility enhancement**:
```typescript
// Ensure collapsed mode provides clear cues
tagDisplay = "collapsed";

// Provide aria-label or helperText to indicate expandable behavior
helperMessage = "Click to see all selected items (+X more collapsed)";

// Or make aria-live announcements clear about selection state
```

**Important interaction with totalSelected**: When totalSelected=true:
- Shows count instead of individual items, making tagDisplay less relevant for primary display
- However, tagDisplay may still affect behavior when dropdown is open or in other contexts
- Consider combining: totalSelected=true for field, but configure how selections appear in dropdown

**Code pattern - smart tagDisplay with totalSelected**:
```typescript
multiSelect = true;

// Strカ:
const displayMode = this.value.length > 5 ? 'count' : 'individual';

switch(displayMode) {
  case 'count':
    this.totalSelected = true; // "X selected"
    break;
  
  case 'individual':
    this.totalSelected = false; // Show individual tags
    this.tagDisplay = this.value.length > 3 ? 'collapsed' : 'wrap';
    break;
}
```

**Important CSS considerations**: The tagDisplay mode may affect:
- Field height and scrollbar behavior
- Tag positioning and spacing
- Cursor placement for typing (in combo-box where disableEdit=false)
- Right-to-left (RTL) layout considerations

**Code example - reactive layout with overflow**:
```typescript
// Pattern: Start with collapsed, auto-expand when user interacts
@Complexport{}
export class SmartComboBox {
  initiallyCollapsed = true;
  userInteracted = false;
  
  get tagDisplay(): "collapsed" | "wrap" {
    // Collapse initially
    if (!this.userInteracted && this.initiallyCollapsed) {
      return "collapsed";
    }
    // Expand after first user interaction
    return "wrap";
  }
  
  onUserInteraction() {
    this.userInteracted = true;
    // Tag display updates based on new state
  }
}
```

**Performance implications**:
- **Collapsed**: Generally more performant - fewer DOM elements rendered initially
- **Wrap**: More DOM elements visible simultaneously, but bounded by maxVisibleRows
- Difference is negligible for typical selection counts (10-20 tags)
- Consider performance only for very large selection counts (50+ tags)

**Code example - performance-optimized for large selections**:
```typescript
// Many selections scenario (100+ items)
multiSelect = true;
disableTags = false; // Show tags
tagDisplay = "collapsed"; // Start collapsed for performance
maxVisibleRows = 3; // Limit visible tags
// Render only minimal tags initially, expand on click
```

**Common patterns and best practices**:
- **Default to collapsed** for most use cases (space-efficient, common UX pattern)
- **Use wrap** when seeing all selections provides value (status displays, dashboard widgets)
- **Consider totalSelected** as alternative for showing count instead of individual tags
- **Combine with maxVisibleRows** to control vertical space usage
- **Test with realistic data** - use actual selection counts and lengths to evaluate layout

**Important troubleshooting**:
- If tags don't wrap as expected: Check maxVisibleRows setting and current field width
- If overflow counter doesn't appear: Ensure tagDisplay="collapsed" and maxVisibleRows limits are being reached
- If field height varies unexpectedly: Check tagDisplay and maxVisibleRows bounds

**Code pattern - debugging tag display**:
```typescript
logTagDisplayState() {
  console.log('tagDisplay:', this.tagDisplay);
  console.log('maxVisibleRows:', this.maxVisibleRows);
  console.log('selectionCount:', this.value.length);
  console.log('expectedOverflow:', Math.max(0, this.value.length - (this.tagDisplay === 'collapsed' ? 3 : this.maxVisibleRows * 3)));
}
```

This prop is visual and affects the layout behavior for multiple selections. It provides control over whether selections are shown in compact collapsed mode or expanded wrap mode, and works in combination with maxVisibleRows and overflowMode for complete control of multi-selection display.

Values:
- `collapsed`: Shows single row with +N overflow indicator that expands on click (default)
- `wrap`: Allows tags to wrap to multiple rows

Usage: `tagDisplay="wrap"`

## overflowMode

Controls how selected options overflow beyond maxVisibleRows. Only applies when maxVisibleRows > 1 and tagDisplay=wrap or when overflowCountClick is true. Interacts with maxVisibleRows and tagDisplay - when tagDisplay=wrap and maxVisibleRows >= 3, scroll mode is used automatically; when tagDisplay=collapsed, clip mode shows +N counter.

Values:
- `clip`: Hides excess options and shows +N counter (default)
- `scroll`: Makes the container scrollable

Usage: `overflowMode="scroll"`

## disableFullScreenMode

Controls mobile behavior: when disableFullScreenMode=true on mobile devices, uses popover instead of full-screen drawer; when disableFullScreenMode=false (default), uses drawer for better mobile UX. On desktop, this prop has no effect. Mobile drawer mode vs popover mode decision logic based on disableFullScreenMode and device detection is implemented but the exact breakpoints and responsive behavior could not be fully traced.

Usage: `disableFullScreenMode="true"`

## mobileDrawerHeight

Controls the height of the mobile drawer in pixels when disableFullScreenMode=false. This prop only applies on mobile devices using drawer mode, no desktop impact.

Usage: `mobileDrawerHeight="400"`

## focus

Programmatically focuses the combo-box input field.

Usage: `this.comboBox.focus()`

## blur

Programmatically blurs (removes focus from) the combo-box input field.

Usage: `this.comboBox.blur()`

## closeDropdown

Programmatically close the dropdown panel.

Usage: `this.comboBox.closeDropdown()`

## openDropdown

Programmatically open the dropdown panel.

Usage: `this.comboBox.openDropdown()`

## setSearchText

Programmatically set the text input value. Accepts a string value and filters options accordingly.

Usage: `this.comboBox.setSearchText("approved")`

## refreshOptions

Programmatically refresh the dropdown options by re-invoking the options function or reloading source data. Returns a Promise<void>.

Usage: `await this.comboBox.refreshOptions()`

## maxLength

Maximum number of characters allowed in the combo-box input field. Default is -1 (no limit).

Usage: `maxLength="50"`

## optionTemplate

Custom template function for rendering individual dropdown options. Accepts IonElement<IDropdownOption>. The componentService.asIonElement() usage for optionTemplate is referenced but the template function signature and IonElement contract were not fully documented from the public API.

Usage: `optionTemplate="customOptionTemplate"`

## textTransform

Text transformation for the combo-box input field value. Could not trace effect on styling through available CSS/LESS files.

Usage: `textTransform="uppercase"`

## disableWhiteSpaceTrimming

Disables automatic whitespace trimming of input values.

Usage: `disableWhiteSpaceTrimming="true"`

## Events

### valueChange

Emitted whenever the selected option(s) changes - on every selection change in single-select mode, on confirmation in multi-select with confirmOnApply=true, and when custom values are entered and validated with allowCustomValue=true.

```typescript
// Angular component
@Component({
  template: `<ion-combo-box (valueChange)="onValueChange($event)"></ion-combo-box>`
})
export class MyComponent {
  onValueChange(event: CustomEvent<{ name: string, value: any }>) {
    const { name, value } = event.detail;
    console.log('Field:', name, 'Value:', value);
  }
}

// Vanilla JS
document.querySelector('ion-combo-box').addEventListener('valueChange', (event) => {
  console.log('Field:', event.detail.name, 'Value:', event.detail.value);
});
```

### dropdownStateChanged

Emitted when the combo-box panel opens or closes - fires with true when opening, false when closing.

```typescript
// Angular component
@Component({
  template: `<ion-combo-box (dropdownStateChanged)="onDropdownStateChanged($event)"></ion-combo-box>`
})
export class MyComponent {
  onDropdownStateChanged(event: CustomEvent<boolean>) {
    console.log('Dropdown:', event.detail ? 'opening' : 'closing');
  }
}

// Vanilla JS
document.querySelector('ion-combo-box').addEventListener('dropdownStateChanged', (event) => {
  console.log('Dropdown:', event.detail ? 'opening' : 'closing');
});
```

### focusIn

Emitted when the combo-box field receives focus - when users click or tab into the field, or when focus is set programmatically.

```typescript
// Angular component
@Component({
  template: `<ion-combo-box (focusIn)="onFocusIn()"></ion-combo-box>`
})
export class MyComponent {
  onFocusIn() {
    console.log('Combo box focused');
  }
}

// Vanilla JS
document.querySelector('ion-combo-box').addEventListener('focusIn', (event) => {
  console.log('Combo box focused');
});
```

### focusOut

Emitted when the combo-box field loses focus - when users click away, tab out, or when focus is removed programmatically.

```typescript
// Angular component
@Component({
  template: `<ion-combo-box (focusOut)="onFocusOut()"></ion-combo-box>`
})
export class MyComponent {
  onFocusOut() {
    console.log('Combo box lost focus');
  }
}

// Vanilla JS
document.querySelector('ion-combo-box').addEventListener('focusOut', (event) => {
  console.log('Combo box lost focus');
});
```

### endEnhancerButtonClick

Emitted when the end enhancer button (if type=icon-button) is clicked - provides hook for custom button action handling.

```typescript
// Angular component
@Component({
  template: `<ion-combo-box (endEnhancerButtonClick)="onEndEnhancerButtonClick()"></ion-combo-box>`
})
export class MyComponent {
  onEndEnhancerButtonClick() {
    console.log('End enhancer button clicked');
  }
}

// Vanilla JS
document.querySelector('ion-combo-box').addEventListener('endEnhancerButtonClick', (event) => {
  console.log('End enhancer button clicked');
});
```

### validationStateChange

Emitted when the validation state changes due to validation logic execution - when validationState prop changes from none/valid/warning/invalid to a different state.

```typescript
// Angular component
@Component({
  template: `<ion-combo-box (validationStateChange)="onValidationStateChange($event)"></ion-combo-box>`
})
export class MyComponent {
  onValidationStateChange(event: CustomEvent<ValidationState>) {
    console.log('New validation state:', event.detail);
  }
}

// Vanilla JS
document.querySelector('ion-combo-box').addEventListener('validationStateChange', (event) => {
  console.log('New validation state:', event.detail);
});
```

### keyDown

Emitted when keyboard events occur within the combo-box field - includes special handling for navigation, selection, and editing interactions.

```typescript
// Angular component
@Component({
  template: `<ion-combo-box (keyDown)="onKeyDown($event)"></ion-combo-box>`
})
export class MyComponent {
  onKeyDown(event: CustomEvent<KeyboardEvent>) {
    console.log('Key pressed:', event.detail.key);
  }
}

// Vanilla JS
document.querySelector('ion-combo-box').addEventListener('keyDown', (event) => {
  console.log('Key pressed:', event.detail.key);
});
```

### textChange

Emitted when the text input value changes - on each keystroke (TextInput), when field loses focus (Blur), when an option is selected (SelectionChange), or when a tag is removed (ItemRemove).

```typescript
// Angular component
@Component({
  template: `<ion-combo-box (textChange)="onTextChange($event)"></ion-combo-box>`
})
export class MyComponent {
  onTextChange(event: CustomEvent<{ value: string, reason: string }>) {
    console.log('Text value:', event.detail.value, 'Reason:', event.detail.reason);
  }
}

// Vanilla JS
document.querySelector('ion-combo-box').addEventListener('textChange', (event) => {
  console.log('Text value:', event.detail.value, 'Reason:', event.detail.reason);
});
```

### filteredOptionsLengthChanged

Emitted when the number of filtered options changes due to typing, search, or options loading - useful for showing/hiding 'no results' messages or updating UI based on available options.

```typescript
// Angular component
@Component({
  template: `<ion-combo-box (filteredOptionsLengthChanged)="onFilteredOptionsLengthChanged($event)"></ion-combo-box>`
})
export class MyComponent {
  onFilteredOptionsLengthChanged(event: CustomEvent<number>) {
    console.log('Filtered options count:', event.detail);
  }
}

// Vanilla JS
document.querySelector('ion-combo-box').addEventListener('filteredOptionsLengthChanged', (event) => {
  console.log('Filtered options count:', event.detail);
});
```

## Examples

### Basic Usage

```typescript
export const Basic = {
  args: {
    label: 'Status',
    placeholder: 'Select a status',
    options: [
      { label: 'Approved', value: 'approved' },
      { label: 'Pending', value: 'pending' },
      { label: 'Rejected', value: 'rejected' }
    ]
  },
  render: (args) => ({
    template: `<ion-combo-box [label]="'${args.label}'" [placeholder]="'${args.placeholder}'" [options]="statusOptions"></ion-combo-box>`,
    component: ComboBoxStoryComponent,
    props: {
      statusOptions: args.options
    }
  })
};
```

### Controlled Component

```typescript
export const Controlled = {
  args: {
    label: 'Category',
    value: 'electronics',
    options: [
      { label: 'Electronics', value: 'electronics' },
      { label: 'Clothing', value: 'clothing' },
      { label: 'Books', value: 'books' }
    ]
  },
  render: (args) => ({
    template: `<ion-combo-box [label]="'${args.label}'" [value]="'${args.value}'" [options]="categoryOptions" (valueChange)="onValueChange($event)"></ion-combo-box>`,
    component: ControlledComboBoxComponent,
    props: {
      categoryOptions: args.options,
      onValueChange: (event) => console.log('Selected:', event.detail.value)
    }
  })
};
```

### Multi-Select

```typescript
export const MultiSelect = {
  args: {
    label: 'Tags',
    multiSelect: true,
    separator: ', ',
    disableTags: false,
    options: [
      { label: 'JavaScript', value: 'javascript' },
      { label: 'TypeScript', value: 'typescript' },
      { label: 'Vue', value: 'vue' },
      { label: 'React', value: 'react' }
    ]
  },
  render: (args) => ({
    template: `<ion-combo-box [label]="'${args.label}'" [multiSelect]="${args.multiSelect}" [separator]="'${args.separator}'" [disableTags]="${args.disableTags}" [options]="tagsOptions"></ion-combo-box>`,
    component: MultiSelectComboBoxComponent,
    props: {
      tagsOptions: args.options
    }
  })
};
```

### With Validation

```typescript
export const WithValidation = {
  args: {
    label: 'Email',
    required: true,
    validationMode: 'onBlur',
    validationState: 'none',
    helperMessage: 'Please enter a valid email address'
  },
  render: (args) => ({
    template: `<ion-combo-box [label]="'${args.label}'" [required]="${args.required}" [validationMode]="'${args.validationMode}'" [validationState]="'${args.validationState}'" [helperMessage]="'${args.helperMessage}'" [options]="emailOptions"></ion-combo-box>`,
    component: ValidationComboBoxComponent,
    props: {}
  })
};
```

### Dynamic Options

```typescript
export const DynamicOptions = {
  args: {
    label: 'Country',
    loadThrottle: 300,
    loading: false
  },
  render: (args) => ({
    template: `<ion-combo-box [label]="'${args.label}'" [loadThrottle]="${args.loadThrottle}" [loading]="${args.loading}" [options]="loadCountries" (filteredOptionsLengthChanged)="onFilteredOptionsChanged($event)"></ion-combo-box>`,
    component: DynamicComboBoxComponent,
    props: {
      loadCountries: async (query) => {
        const response = await fetch(`/api/countries?q=${query}`);
        return response.json();
      },
      onFilteredOptionsChanged: (event) => console.log('Options count:', event.detail)
    }
  })
};
```

### Custom Filtering

```typescript
export const CustomFiltering = {
  args: {
    label: 'Search Items',
    filterMode: 'MultiToken',
    filterKeys: ['label', 'description'],
    caseSensitiveFilter: false,
    disableDefaultSorting: false
  },
  render: (args) => ({
    template: `<ion-combo-box [label]="'${args.label}'" [filterMode]="'${args.filterMode}'" [filterKeys]="${JSON.stringify(args.filterKeys)}" [caseSensitiveFilter]="${args.caseSensitiveFilter}" [disableDefaultSorting]="${args.disableDefaultSorting}" [options]="searchItems"></ion-combo-box>`,
    component: CustomFilteringComboBoxComponent,
    props: {
      searchItems: [
        { label: 'Apple', description: 'A red fruit', value: 'apple' },
        { label: 'Banana', description: 'A yellow fruit', value: 'banana' },
        { label: 'Cherry', description: 'A red small fruit', value: 'cherry' }
      ]
    }
  })
};
```