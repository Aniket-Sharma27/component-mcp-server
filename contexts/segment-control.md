---
realComponent: "ion-segmented-control"
description: "A visual form control that allows users to select one or multiple options from a group, providing greater prominence than radio buttons with configurable appearance, content variants, and selection behaviors"
themes:
  - light
  - dark
props:
  - name: "multiSelect"
    type: "boolean"
    category: "behavioral"
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
    designTokens: {}
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
  - name: "orientation"
    type: "orientation"
    category: "visual"
    required: false
    default: "horizontal"
    values:
      - horizontal
      - vertical
    designTokens: {}
  - name: "label"
    type: "string | ILabelOptions"
    category: "content"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "labelAlignment"
    type: "labelAlignment"
    category: "visual"
    required: false
    default: "start"
    values:
      - start
      - end
    designTokens: {}
  - name: "description"
    type: "string"
    category: "content"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "contentOrientation"
    type: "contentOrientation"
    category: "visual"
    required: false
    default: "horizontal"
    values:
      - horizontal
      - vertical
    designTokens: {}
  - name: "disableWrap"
    type: "boolean"
    category: "visual"
    required: false
    default: "false"
    values: []
    designTokens: {}
  - name: "minSelection"
    type: "number"
    category: "behavioral"
    required: false
    default: "1"
    values: []
    designTokens: {}
  - name: "maxSelection"
    type: "number"
    category: "behavioral"
    required: false
    default: "1"
    values: []
    designTokens: {}
  - name: "name"
    type: "string"
    category: "behavioral"
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
  - name: "value"
    type: "any[]"
    category: "content"
    required: true
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
  - name: "variant"
    type: "string"
    category: "visual"
    required: false
    default: "icon-label-description"
    values:
      - icon
      - label
      - icon-label
      - label-description
      - icon-label-description
    designTokens: {}
  - name: "required"
    type: "boolean"
    category: "accessibility"
    required: false
    default: "none found"
    values: []
    designTokens: {}
  - name: "necessityIndicator"
    type: "IndicatorType"
    category: "accessibility"
    required: false
    default: "none found"
    values: []
    designTokens: {}
events:
  - name: "valueChange"
    payloadType: "CustomEvent<{ name: string, value: any[] }>"
    firesWhen: "Fires immediately after user interaction completes and the selection state is validated and accepted"
    detailAccess: "event.detail.name (string) and event.detail.value (any[] of selected item values)"
    bindingSyntax: "(valueChange)='onValueChange($event)'"
  - name: "change"
    payloadType: "CustomEvent<{ name: string, value: any[] }>"
    firesWhen: "Fires immediately after user interaction completes and the selection state is validated and accepted (emitted alongside valueChange for backward compatibility)"
    detailAccess: "event.detail.name (string) and event.detail.value (any[] of selected item values)"
    bindingSyntax: "(change)='onChange($event)'"
jointTokens:
  - combination: "emphasized=true, disabled=false, readOnly=false"
    resolvesTo: "#f5f5f6"
    tokenChain: "var(--ion-comp-segmented-control-group-container-color-bg-enabled-bold)"
    appliesToCssProperty: "background-color"
  - combination: "emphasized=false, disabled=false, readOnly=false"
    resolvesTo: "#f9f9fa"
    tokenChain: "var(--ion-comp-segmented-control-group-container-color-bg-enabled-subtle)"
    appliesToCssProperty: "background-color"
  - combination: "emphasized=true, disabled=true"
    resolvesTo: "#f5f5f6"
    tokenChain: "var(--ion-comp-segmented-control-group-container-color-bg-disabled-bold)"
    appliesToCssProperty: "background-color"
  - combination: "emphasized=false, disabled=true"
    resolvesTo: "#f9f9fa"
    tokenChain: "var(--ion-comp-segmented-control-group-container-color-bg-disabled-subtle)"
    appliesToCssProperty: "background-color"
  - combination: "emphasized=true, readOnly=true"
    resolvesTo: "#f5f5f6"
    tokenChain: "var(--ion-comp-segmented-control-group-container-color-bg-read-only-bold)"
    appliesToCssProperty: "background-color"
  - combination: "emphasized=false, readOnly=true"
    resolvesTo: "#f9f9fa"
    tokenChain: "var(--ion-comp-segmented-control-group-container-color-bg-read-only-subtle)"
    appliesToCssProperty: "background-color"
propInteractions:
  - "multiSelect affects role: when true, component uses checkbox role and allows TAB navigation through all items; when false, uses radio group role with arrow key navigation"
  - "minSelection and maxSelection constrain selection behavior: user cannot select fewer items than minSelection or more than maxSelection, and attempts emit warnings and revert changes"
  - "size affects sizing tokens for container padding, gaps, and minimum heights across sm/md/lg variants"
  - "orientation controls flex-direction of the group container (row for horizontal, column for vertical)"
  - "contentOrientation controls flex-direction of internal content layout (row for horizontal, column for vertical)"
  - "disableWrap applies disable-wrap class that sets min-width: 0 on slotted items to prevent text wrapping"
  - "emphasized affects visual prominence by switching between bold and subtle design token variants"
  - "disabled sets fieldsetState to 'disabled', applies disabled classes, and propagates to all items"
  - "readOnly sets fieldsetState to 'read-only', applies read-only classes, and propagates to all items"
  - "variant determines which elements (icon, label, description) are visible within each segmented control item"
needsReview:
  - "No dark-theme-specific design token values were found in the provided CSS files for exact color resolution"
  - "Design token resolution chain for individual item states (selected-enabled, selected-hover, selected-pressed, etc.) follows complex combinatorial logic that depends on multiple prop combinations (emphasized + disabled + readOnly + selected + hover + pressed)"
  - "Specific hex values for enabled/hover/pressed/disabled/read-only states could not be traced to resolved values without access to the token definition files"
  - "The variant enum values (icon, label, icon-label, label-description, icon-label-description) control visibility of child elements but their exact design token mappings are complex"
  - "validation states (valid, warning, invalid) are supported via fieldsetState but specific token values were not traced"
  - "size-specific design token resolution for sm/md/lg variants across different states could not be fully traced without token definition files"
---

## Usage Notes

Boolean props on this component must always be passed with an explicit string value — e.g. `disabled="true"` or `[disabled]="isDisabled"` — never as bare attribute presence (e.g. `disabled` alone, with no value). Bare attribute presence is a native HTML convention this component does NOT support; it will not be interpreted as true.

## multiSelect

Controls whether users can select multiple options simultaneously or are restricted to a single choice. This is a behavioral prop that fundamentally changes the component's accessibility role and keyboard navigation pattern.

When set to `true`, the component operates as a checkbox group: users can select multiple items, each item is independently reachable via TAB key, and Spacebar toggles the current item's selection. When `false`, it operates as a radio group: users can select only one item at a time, arrow keys navigate between options, and the component as a whole has a single TAB stop.

**Visual cues:** This prop doesn't change visual appearance directly, but affects accessibility behavior and the role attribute (group vs radiogroup, checkbox vs radio for child items).

**When to use:**
- Use `multiSelect="true"` when users need to select multiple independent options
- Use `multiSelect="false"` (default) for mutually exclusive choices
- Combine with `minSelection` and `maxSelection` to enforce valid selection ranges

## emphasized

Controls the visual prominence of the segmented control, switching between two distinct visual weight levels. This is a visual prop that affects color and border styling.

When `true`, uses the "bold" variant with stronger colors and borders for greater emphasis. When `false`, uses the "subtle" variant with lighter styling. The visual effect applies to the group container background, item backgrounds, borders, and text colors.

**Visual cues:** The bold variant shows stronger contrast with more pronounced colors, while the subtle variant uses lighter, more subtle colors. This affects the `background-color` and `border-color` properties.

**When to use:**
- Use `emphasized="true"` when the segmented control needs greater visual prominence in the layout
- Use `emphasized="false"` (default) for standard visual weight
- Consider layout hierarchy - emphasized controls should be used for more important choices

## size

Controls the physical dimensions of the segmented control, affecting padding, gaps, height, and border radius. This is a visual prop that scales the component's size while maintaining proportions.

Accepts three predefined sizes: `sm` (small), `md` (medium, default), `lg` (large). Each size applies a consistent scaling factor to spacing, padding, and sizing tokens.

**Visual cues:** Larger sizes show increased padding, gaps, and minimum heights. The visual effect includes `padding-block`, `padding-inline`, `gap`, `min-height`, and `border-radius` changes across the three size variants.

**When to use:**
- Use `size="sm"` for compact layouts or when space is constrained
- Use `size="md"` (default) for standard use cases
- Use `size="lg"` when greater prominence or touch targets are needed

## orientation

Controls the layout direction of the segmented control group as a whole. This is a visual prop that affects how the container positions its children.

Accepts `horizontal` (default) or `vertical`. Horizontal orients items left-to-right in a row, vertical stacks items top-to-bottom in a column.

**Visual cues:** Changes the flex-direction of the group container. This affects the overall layout but not the internal arrangement of content within each item.

**When to use:**
- Use `orientation="horizontal"` (default) for row-based layouts
- Use `orientation="vertical"` for column-based layouts when space constraints or design patterns call for vertical stacking

## label

Provides the main descriptive label text displayed above the segmented control. This is a content prop that conveys the primary purpose or question the control answers to.

Can accept either a plain string or an `ILabelOptions` object with properties for label text, start icon, and end icon. When provided, it's rendered by the fieldset component that wraps the segmented control.

**Visual cues:** Displayed as a legend/label above the segmented control, positioned according to `labelAlignment` (start or end).

**When to use:**
- Always provide a clear, descriptive label for accessibility and usability
- Use the object form with icons when you need visual context alongside the text
- The label should be concise but descriptive enough that users understand what they're selecting

## labelAlignment

Controls the horizontal alignment of the label relative to the segmented control. This is a visual prop that affects positioning.

Accepts `start` (default) or `end`. Start aligns the label to the left (for LTR languages), end aligns to the right.

**Visual cues:** Changes the text alignment of the legend/label element above the segmented control.

**When to use:**
- Use `labelAlignment="start"` (default) for standard left-aligned labels
- Use `labelAlignment="end"` when design patterns call for right-aligned labels

## description

Provides additional descriptive text displayed below the label and above the segmented control. This is a content prop that offers supplemental context, instructions, or help text.

Displayed as part of the fieldset wrapper around the segmented control.

**Visual cues:** Appears as smaller helper text between the label and the segmented control.

**When to use:**
- Use to provide additional context or instructions beyond the main label
- Keep descriptions concise and focused on helpful supplementary information
- Don't use for critical information that should be in the main label

## contentOrientation

Controls the layout direction of content within each individual segmented control item. This is a visual prop that affects how icon, label, and description are arranged inside each item.

Accepts `horizontal` (default) or `vertical`. Horizontal arranges items left-to-right in a row, vertical stacks them top-to-bottom in a column.

**Visual cues:** Changes the flex-direction of the internal container within each segmented control item.

**When to use:**
- Use `contentOrientation="horizontal"` (default) for standard row-based item layouts
- Use `contentOrientation="vertical"` when you need icon/label/description stacked vertically within items

## disableWrap

Controls whether text content within segmented control items can wrap or is truncated with ellipsis. This is a visual prop that affects text overflow behavior.

When `true`, applies `min-width: 0` to allow text truncation with ellipsis. When `false`, allows normal text wrapping behavior.

**Visual cues:** When enabled, long text will be truncated with ellipsis (...) rather than wrapping to multiple lines.

**When to use:**
- Use `disableWrap="true"` when you have limited horizontal space and want consistent item heights
- Use `disableWrap="false"` (default) when text wrapping is acceptable and you want to preserve all content

## minSelection

Specifies the minimum number of items users must select. This is a behavioral prop that enforces selection constraints.

Accepts a numeric value (default is 1). Cannot be greater than `maxSelection`. Users cannot submit or complete an action (in a form context) until they've selected at least this many items.

**Visual cues:** No direct visual effect, but may affect disabled states of items when combined with `multiSelect` and `maxSelection`.

**When to use:**
- Use to enforce business logic requirements where a certain number of items must be selected
- Default of 1 ensures at least one option is always selected in single-select mode
- Works with `multiSelect` to enforce minimum selections

## maxSelection

Specifies the maximum number of items users can select. This is a behavioral prop that enforces selection constraints and can trigger automatic item disabling.

Accepts a numeric value (default is 1). Cannot be less than `minSelection`. When users reach this maximum, unselected items become automatically disabled.

**Visual cues:** When the maximum selection count is reached, unselected items appear in a disabled state and cannot be selected.

**When to use:**
- Use to enforce limits on the number of selections in multi-select mode
- Default of 1 ensures single-select behavior until `multiSelect` is enabled
- Combines with `multiSelect` for precise selection control

## name

Provides the form field name used when submitting the segmented control as part of an HTML form. This is a behavioral prop that enables form integration.

The name is used as the key when the segmented control is included in form submission, similar to native form controls.

**Visual cues:** No direct visual effect.

**When to use:**
- Use when the segmented control is part of a traditional HTML form that will be submitted
- Most relevant in form-based applications where traditional form submission is used
- Can be omitted in single-page applications that handle state management differently

## defaultValue

Provides an initial value that should be pre-selected when the component first renders. This is a behavioral prop that sets the starting state.

Accepts an array of values that correspond to the `value` attributes of the segmented control items. This is different from `value` - it's for initial state only.

**Visual cues:** Items whose values match the provided array will appear in the selected state when the component first renders.

**When to use:**
- Use to set the default/initial selection when the page first loads
- Different from `value` which represents the current controlled state
- Useful for form initialization or preset configurations

## disabled

Controls whether the entire segmented control is disabled and non-interactive. This is a visual and behavioral prop that affects all children.

When `true`, disables all items within the control, applies disabled styling, and prevents any user interaction. Propagates the disabled state to all child segmented control items.

**Visual cues:** Applies disabled color tokens (lighter colors, reduced contrast), sets appropriate ARIA attributes, and visually indicates non-interactive state. The entire control appears grayed out and unresponsive to mouse or keyboard interaction.

**When to use:**
- Use `disabled="true"` when the control should be temporarily unavailable due to application state
- Use when user permissions or business logic prevent selection changes
- The default of `false` means the control is interactive

## readOnly

Controls whether the segmented control is read-only (readable but not modifiable). This is a visual and behavioral prop that prevents modification while allowing inspection.

When `true`, prevents selection changes but allows keyboard navigation and focus. Unlike `disabled`, read-only controls can be focused and their content can be inspected, but values cannot be changed.

**Visual cues:** Applies read-only color tokens, sets appropriate ARIA attributes, and indicates the control cannot be modified but can be interacted with for inspection.

**When to use:**
- Use `readOnly="true"` when you want to display current selections that cannot be changed
- Different from disabled: read-only controls can still receive focus and keyboard navigation
- Useful for displaying locked or finalized selections

## value

Controls the currently selected items in the segmented control. This is a content prop that represents the component's state.

Accepts an array of values that correspond to the `value` attributes of the segmented control items. This is the controlled state of the component - changes to this value update the selection, and user interactions update this value via events.

**Visual cues:** Items whose values are in the array appear in the selected state with appropriate styling (background color, border, text colors).

**When to use:**
- This is a required prop and must beprovided to establish controlled state
- Use to set the current selection state programmatically
- Update this prop in response to the `valueChange` event to create a fully controlled component

## ariaLabel

Provides an accessible label for screen readers when a visible label is insufficient or unavailable. This is an accessibility prop that assists users of assistive technology.

The aria-label attribute is used by screen readers to announce the purpose of the segmented control when no other label is available or when additional context is needed.

**Visual cues:** No direct visual effect.

**When to use:**
- Use when additional accessibility context is needed beyond the visible label
- Use when a visible label is not present but the control needs an accessible name
- Override default accessibility behavior when needed for complex use cases

## variant

Controls which combination of icon, label, and description elements are visible within each segmented control item. This is a visual prop that determines item content structure.

Accepts five variants: `icon` (icons only), `label` (labels only), `icon-label` (icons and labels), `label-description` (labels and descriptions), `icon-label-description` (all elements, default).

**Visual cues:** Directly controls visibility of `showIcon`, `showLabel`, and `showDescription` properties on child items, changing which DOM elements are rendered and styled.

**When to use:**
- Use `variant="icon-label-description"` (default) for the most informative display with all elements
- Use `variant="icon"` for icon-only selections when space is extremely constrained
- Use `variant="label"` for text-only selections when icons are unnecessary
- Use `variant="icon-label"` for standard icon+text combinations
- Use `variant="label-description"` when you need primary text plus supplemental description without icons

## required

Indicates whether the segmented control requires user input before form submission. This is an accessibility prop that affects form validation and visual indicators.

When `true`, typically triggers visual indicators (like asterisks or different colored labels) and may enable form validation logic.

**Visual cues:** May display required indicators (depending on `necessityIndicator` setting) and can affect validation state styling.

**When to use:**
- Use `required="true"` when at least one selection must be made before form submission
- Combine with `minSelection` to enforce specific selection requirements
- Use to ensure users complete this control before proceeding

## necessityIndicator

Controls how the required/optional status is visually indicated next to the label. This is an accessibility and visual prop that shows whether a field is required.

Accepts values like `requiredMarker`, `requiredLabel`, `optionalLabel`, or `none` to control what indicator is displayed.

**Visual cues:** Shows different visual indicators next to the label: markers (*), text labels ("Required" or "Optional"), or no indicator.

**When to use:**
- Use to explicitly control how required/optional status is communicated
- Combine with `required` prop for clear indication of field requirements
- Choose based on your design system's conventions for field status indication

## Events

### valueChange

Fires when the user completes a selection interaction and the new selection state is validated and accepted. This event is the primary way to track selection changes in the segmented control.

**Emitted args:** `CustomEvent<{ name: string, value: any[] }>`

**When to use:**
- Update your component's state when users make selections
- Trigger application logic that depends on the current selection
- Validate or process the selected values
- Display confirmation or feedback about the selected items

**How to use:**
```typescript
onValueChange(event: CustomEvent<{ name: string, value: any[] }>): void {
    const selectedValues = event.detail.value; // Array of selected item values
    const controlName = event.detail.name;    // The name of the segmented control
    console.log(`${controlName} value changed to:`, selectedValues);
    // Update your component state here
}
```

**Binding syntax:**
```html
<ion-segmented-control (valueChange)="onValueChange($event)" [value]="selectedItems">
    <!-- items -->
</ion-segmented-control>
```

### change

Fires when the user completes a selection interaction and the new selection state is validated and accepted. This event is emitted alongside `valueChange` for backward compatibility with legacy code.

**Emitted args:** `CustomEvent<{ name: string, value: any[] }>`

**When to use:**
- Maintaining compatibility with older code patterns that rely on the `change` event
- Legacy implementations that used `change` instead of `valueChange`
- When both event names are needed for different purposes in your application

**How to use:**
```typescript
onChange(event: CustomEvent<{ name: string, value: any[] }>): void {
    const selectedValues = event.detail.value; // Array of selected item values
    const controlName = event.detail.name;    // The name of the segmented control
    console.log(`${controlName} changed to:`, selectedValues);
    // Legacy compatibility handler
}
```

**Binding syntax:**
```html
<ion-segmented-control (change)="onChange($event)" [value]="selectedItems">
    <!-- items -->
</ion-segmented-control>
```

**Complete event binding example:**
```html
<ion-segmented-control
    (valueChange)="onValueChange($event)"
    (change)="onChange($event)"
    [value]="selectedItems"
    [name]="controlName">
    <ion-segmented-control-item *ngFor="let item of items"
        [value]="item.value">
        {{item.label}}
    </ion-segmented-control-item>
</ion-segmented-control>
```

```typescript
export class MyComponent {
    selectedItems: any[] = [];
    controlName = 'mySegmentedControl';

    onValueChange(event: CustomEvent<{ name: string, value: any[] }>): void {
        this.selectedItems = event.detail.value;
        console.log('Primary handler:', event.detail.name, event.detail.value);
        // Main application logic here
    }

    onChange(event: CustomEvent<{ name: string, value: any[] }>): void {
        console.log('Legacy handler:', event.detail.name, event.detail.value);
        // Legacy compatibility handling here
    }
}
```

## Examples

Basic segmented control with single selection:
```html
<ion-segmented-control
    [value]="['active']"
    (valueChange)="onValueChange($event)">
    <ion-segmented-control-item label="Active" value="active"></ion-segmented-control-item>
    <ion-segmented-control-item label="Inactive" value="inactive"></ion-segmented-control-item>
</ion-segmented-control>
```
*Demonstrates basic single-select pattern with value binding and event handling*

Segmented control with icons and labels:
```html
<ion-segmented-control
    variant="icon-label"
    [value]="['1']"
    (valueChange)="onValueChange($event)">
    <ion-segmented-control-item
        label="ACTIVE"
        icon="lock"
        value="1">
    </ion-segmented-control-item>
    <ion-segmented-control-item
        label="IN-PROGRESS"
        icon="lock_open"
        value="2">
    </ion-segmented-control-item>
    <ion-segmented-control-item
        label="CLOSED"
        icon="lock_filled"
        value="3">
    </ion-segmented-control-item>
</ion-segmented-control>
```
*Demonstrates icon-label variant with icon and label display on each item*

Multi-select segmented control:
```html
<ion-segmented-control
    multiSelect="true"
    minSelection="1"
    maxSelection="3"
    [value]="selectedItems"
    (valueChange)="onValueChange($event)">
    <ion-segmented-control-item *ngFor="let item of options"
        [label]="item.label"
        [value]="item.value">
    </ion-segmented-control-item>
</ion-segmented-control>
```
*Demonstrates multi-select behavior with selection constraints*

Segmented control with label and description:
```html
<ion-segmented-control
    label="Status"
    description="Select the current status"
    variant="label-description"
    [value]="['2']"
    (valueChange)="onValueChange($event)">
    <ion-segmented-control-item
        label="Active"
        description="Currently active"
        value="1">
    </ion-segmented-control-item>
    <ion-segmented-control-item
        label="Pending"
        description="Awaiting approval"
        value="2">
    </ion-segmented-control-item>
    <ion-segmented-control-item
        label="Closed"
        description="No longer active"
        value="3">
    </ion-segmented-control-item>
</ion-segmented-control>
```
*Demonstrates label-description variant with both primary and secondary text*

Emphasized segmented control:
```html
<ion-segmented-control
    emphasized="true"
    [value]="['active']"
    (valueChange)="onValueChange($event)">
    <ion-segmented-control-item label="Active" value="active"></ion-segmented-control-item>
    <ion-segmented-control-item label="Completed" value="completed"></ion-segmented-control-item>
</ion-segmented-control>
```
*Demonstrates emphasized visual style with bold/appearance*

Segmented control with disabled items:
```html
<ion-segmented-control
    [value]="['2']"
    (valueChange)="onValueChange($event)">
    <ion-segmented-control-item label="Option 1" value="1" disabled="true"></ion-segmented-control-item>
    <ion-segmented-control-item label="Option 2" value="2"></ion-segmented-control-item>
    <ion-segmented-control-item label="Option 3" value="3"></ion-segmented-control-item>
</ion-segmented-control>
```
*Demonstrates individual item disabled state*

Icon-only variant:
```html
<ion-segmented-control
    variant="icon"
    [value]="['1']"
    (valueChange)="onValueChange($event)">
    <ion-segmented-control-item icon="pin" value="1"></ion-segmented-control-item>
    <ion-segmented-control-item icon="bar_chart" value="2"></ion-segmented-control-item>
    <ion-segmented-control-item icon="print" value="3"></ion-segmented-control-item>
</ion-segmented-control>
```
*Demonstrates icon-only variant for compact displays*

Vertical orientation:
```html
<ion-segmented-control
    orientation="vertical"
    [value]="['active']"
    (valueChange)="onValueChange($event)">
    <ion-segmented-control-item label="Active" value="active"></ion-segmented-control-item>
    <ion-segmented-control-item label="Inactive" value="inactive"></ion-segmented-control-item>
</ion-segmented-control>
```
*Demonstrates vertical layout orientation*

Disabled segmented control:
```html
<ion-segmented-control
    disabled="true"
    [value]="['active']"
    (valueChange)="onValueChange($event)">
    <ion-segmented-control-item label="Active" value="active"></ion-segmented-control-item>
    <ion-segmented-control-item label="Inactive" value="inactive"></ion-segmented-control-item>
</ion-segmented-control>
```
*Demonstrates disabled state for entire control*