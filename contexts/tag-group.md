---
realComponent: "ion-tag-group"
description: "A container component that groups multiple ion-tag elements together, providing shared selection state, keyboard navigation, and optional overflow handling for tag collections."
themes: ["ion-modern-light-ds", "ion-modern-dark-ds"]
apiTypes: ["element"]
relatedComponents:
  - name: "ion-tag"
    relationship: "child"
    whenToUse: "Use ion-tag-group whenever rendering 2+ ion-tag elements together it manages shared selection state, keyboard navigation between tags, and optional overflow hiding. Use standalone ion-tag elements only when you need a single tag without group-level coordination."
props:
  - name: "name"
    type: "string"
    category: "content"
    required: false
    default: "none found"
    designTokens: {}
  - name: "type"
    type: "TagType"
    category: "visual"
    required: false
    default: "none found"
    values: ["non-interactive", "selectable", "removable"]
    designTokens: {}
  - name: "disabled"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "false"
    designTokens: {}
  - name: "size"
    type: "string"
    category: "visual"
    required: false
    default: '""'
    values: ["sm", "md", "lg", " MQ<string>"]
    designTokens:
      sm:
        resolvesTo: "1px"
        tokenChain: "--ion-lit-sizing-fixed-10"
        appliesToCssProperty: "border-radius"
      md:
        resolvesTo: "2px"
        tokenChain: "--ion-lit-sizing-fixed-25"
        appliesToCssProperty: "border-radius"
      lg:
        resolvesTo: "2px"
        tokenChain: "--ion-lit-sizing-fixed-25"
        appliesToCssProperty: "border-radius"
  - name: "ariaLabel"
    type: "string"
    category: "accessibility"
    required: false
    default: "Strings.DESIGN_SYSTEM_TAG_GROUP_ARIA_LABEL_DEFAULT"
    designTokens: {}
  - name: "hideOverflow"
    type: "boolean"
    category: "visual"
    required: false
    default: "false"
    designTokens: {}
  - name: "multiSelect"
    type: "boolean"
    category: "behavioral"
    required: false
    default: "false"
    designTokens: {}
  - name: "value"
    type: "any[]"
    category: "content"
    required: false
    default: "[]"
    designTokens: {}
events:
  - name: "valueChange"
    payloadType: "CustomEvent<ITagGroupValueChangeEventArgs>"
    firesWhen: "Fires when the selected tags change (only applicable when type is 'selectable'). Emits on both selection and deselection events."
    detailAccess: "event.detail.value (any[]) - array of currently selected tag labels, event.detail.name (string) - the name of the tag group, event.detail.unselected (any[]) - array of tag labels that were just deselected"
    bindingSyntax: "(valueChange)=\"onTagGroupChange($event)\""
jointTokens: []
propInteractions:
  - "The 'type' prop determines whether 'value' and 'multiSelect' props are relevant only 'selectable' type uses value/multiSelect for selection state management."
  - "The 'multiSelect' prop affects selection behavior when 'type' is 'selectable' when false, selecting one tag deselects others; when true, multiple tags can be selected simultaneously."
  - "When 'hideOverflow' is true, the group automatically calculates which tags fit in the container and hides the rest, showing a '+N' overflow label."
  - "The 'size' prop automatically propagates to all child ion-tag elements, ensuring consistent sizing without setting size on each tag individually."
  - "The 'disabled' prop propagates to all child tags, making them unselectable and non-interactive regardless of individual tag disabled states."
  - "The 'name' prop is shared across all child tags for form submission purposes when type is 'selectable'."
needsReview:
  - "No token-mapped visual properties found for the 'type' prop values (non-interactive, selectable, removable) - the visual differences between these types exist but the token mappings could not be traced from the source material."
  - "Only sizing tokens (border-radius) were traceable from the CSS; the actual container spacing, gap, and typography tokens for different size values exist but their full resolution chains could not be traced from the provided token files."
  - "The overflow text (+N label) token chain could not be completely traced from the source material, though the token --ion-comp-tag-group-overflow-text-color-fg-diabled is referenced in tag-ds.css."
  - "No dark-theme-specific token values were found for tag-group specific tokens; the component likely uses the inverse theme tokens automatically but this could not be verified."
---

The `<ion-tag-group>` component is a container for managing collections of `<ion-tag>` elements with shared behavior. It provides coordinated selection state, keyboard navigation between tags, and optional overflow handling when tags exceed available space.

This component is essential when rendering multiple tags together — don't use standalone `ion-tag` elements when you need 2+ tags with coordinated behavior. The tag group handles the complexity of managing selection state (for selectable tags), keyboard navigation, and overflow scenarios automatically.

## Usage Notes

Boolean props on this component must always be passed with an explicit string value — e.g. `disabled="true"` or `[disabled]="isDisabled"` — never as bare attribute presence (e.g. `disabled` alone, with no value). Bare attribute presence is a native HTML convention this component does NOT support; it will not be interpreted as true.

## Related Components

**ion-tag** (child component): The tag-group component requires ion-tag elements as children. Use tag-group instead of multiple standalone ion-tag elements whenever rendering 2+ mutually exclusive options together — it manages shared name/selection state and keyboard navigation automatically. For single tags scenarios, standalone ion-tag may be more appropriate.

## name

This is a content prop that provides an identifier for the tag group, particularly important when `type="selectable"` for form submission purposes. The name is shared across all child tags in the group. This prop is not visually apparent from a design but is important for backend integration and form handling when selected tags need to be submitted as a named form field.

## type

This visual prop determines the interaction mode for all child tags in the group. The type must be set on the tag-group, not on individual tags — the group ensures all contained tags follow the same interaction pattern.

Choose `non-interactive` for static, display-only tag collections (like category labels or status indicators). Choose `selectable` when you want users to choose one or more options from the group (like filter options or category selection). Choose `removable` when you want users to be able to delete items from the collection (like selected filters or items in a list).

**non-interactive**: Tags display static content with no interactive behavior. No selection state or removal actions.

**selectable**: Tags become interactive with click/keyboard selection. When clicked, a toggle selection effect shows/hides. The visual state changes based on selection (color/opacity changes). When `multiSelect="true"`, multiple tags can be selected simultaneously; when `false`, only one tag can be selected at a time.

**removable**: Tags display with a remove button (X icon) that allows users to delete individual tags from the group. Delete can also be triggered via keyboard (Delete key when tag is focused).

The type affects which other props become relevant — value and multiSelect only apply when type="selectable".

## disabled

This behavioral prop disables all interaction within the tag group when set to true. All child tags become non-interactive regardless of their individual disabled states. The visual appearance of disabled tags changes (usually reduced opacity and gray colors).

This prop is not typically determined from a visual design — it's a state you control programmatically based on application logic (e.g., disabling filters while data loads).

## size

This visual prop controls the dimensions of all tags in the group. The size must be set consistently on the group; it automatically propagates to all child tags.

Choose `sm` for compact tag collections where space is limited (like mobile interfaces or dense information displays). Choose `md` (the default) for standard tag sizing suitable for most use cases. Choose `lg` for larger tags that need to be more prominent (like accessibility-focused interfaces or larger touch targets).

The visual cues for size differences include: smaller tags have reduced padding, smaller font sizes, and smaller border-radius; larger tags have increased padding, larger font sizes, and maintain consistent proportions.

## ariaLabel

This accessibility prop provides a screen-reader-friendly description for the entire tag group container. This is particularly important for non-visual users who may not perceive the visual relationship between the grouped tags.

If no `ariaLabel` is provided, the component uses a default label. However, providing a descriptive label is recommended for better accessibility — for example, "Filter options" for a group of selectable filter tags, or "Selected items" for a removable tags group.

## hideOverflow

This visual prop enables automatic overflow handling when the tag group's content exceeds available horizontal space. When set to true, the component calculates which tags fit in the container and hides the remaining tags, showing a "+N" overflow label that expands the list when clicked.

Choose `hideOverflow="true"` when you have dynamic tag collections that may vary in size and need to maintain a consistent visual layout (like user-selected filters that could grow extensively). When the overflow label is clicked, all hidden tags become visible and a "Show Less" option appears to collapse back to the trimmed view.

The overflow behavior is automatic — no additional configuration is needed beyond setting this boolean. The component uses resize observers to recalculate the visible tags when the container size changes.

## multiSelect

This behavioral prop controls whether multiple tags can be selected simultaneously when `type="selectable"`. It only applies to selectable type tag groups.

When set to `false` (the default), the enforces single selection — selecting one tag automatically deselects any previously selected tag. This is radio-button behavior where exactly one option can be chosen.

When set to `true`, multiple tags can be selected independently — users can select or deselect individual tags without affecting others. This is checkbox behavior where multiple options can be chosen.

The selection state is managed through the `value` prop and `valueChange` event, which track the currently selected tag labels.

## value

This content prop tracks the currently selected tag labels when `type="selectable"`. It's an array of strings containing the labels of all selected tags.

For single selection (multiSelect=false), the array contains either 0 or 1 label. For multi-selection (multiSelect=true), the array can contain 0, 1, or many labels.

The `value` prop is bidirectional — you can set it to initialize the selection state (pre-select specific tags), and it updates automatically when users select/deselect tags via the `valueChange` event.

## Events

### valueChange

This event fires whenever the selected tags change in a selectable type tag group. It emits on both selection and deselection events, providing the complete current state and what changed.

**Emitted args:** `CustomEvent<ITagGroupValueChangeEventArgs>` where `ITagGroupValueChangeEventArgs` contains:
- `value: any[]` - array of currently selected tag labels
- `name: string` - the name of the tag group
- `unselected: any[]` - array of tag labels that were just deselected

**When to use:** 
- Filter panels where you need to update data when users select/deselect filter options
- Form submission where selected tags need to be captured
- State management where the selection state needs to synchronize with other components

**How to use:**
```typescript
onTagGroupChange(event: CustomEvent<ITagGroupValueChangeEventArgs>) {
  const selectedTags = event.detail.value; // Array of selected tag labels
  const deselectedTags = event.detail.unselected; // Array of recently deselected tags
  const groupName = event.detail.name; // The tag group's name

  console.log('Selected tags:', selectedTags);
  console.log('Recently deselected:', deselectedTags);
  
  // Update your application state
  this.selectedFilters = selectedTags;
}
```

**Binding syntax:**
```html
<ion-tag-group 
  type="selectable" 
  (valueChange)="onTagGroupChange($event)">
  <ion-tag label="Option 1"></ion-tag>
  <ion-tag label="Option 2"></ion-tag>
</ion-tag-group>
```

**Complete event binding example:**
```html
<ion-tag-group 
  name="filterOptions"
  type="selectable"
  multiSelect="true"
  [value]="selectedFilters"
  (valueChange)="onTagGroupChange($event)">
  <ion-tag label="Category A"></ion-tag>
  <ion-tag label="Category B"></ion-tag>
  <ion-tag label="Category C"></ion-tag>
</ion-tag-group>
```

```typescript
export class FilterComponent {
  selectedFilters: string[] = [];

  onTagGroupChange(event: CustomEvent<ITagGroupValueChangeEventArgs>) {
    // Access the payload via .detail - this is critical for web components
    const { value, unselected } = event.detail;
    
    // Update local state
    this.selectedFilters = value;
    
    // Trigger data refresh based on new selection
    this.refreshData();
    
    // Log what changed
    if (unselected.length > 0) {
      console.log('Deselected:', unselected);
    }
  }

  refreshData() {
    // Your data refresh logic
  }
}
```

## Examples

### Non-interactive tag group

```html
<ion-tag-group 
  type="non-interactive" 
  size="md"
  ariaLabel="Status labels">
  <ion-tag label="Active"></ion-tag>
  <ion-tag label="Pending"></ion-tag>
  <ion-tag label="Completed"></ion-tag>
</ion-tag-group>
```
*Demonstrates a simple non-interactive tag group with manual size setting.*

### Selectable tag group with single selection

```html
<ion-tag-group 
  name="planSelection"
  type="selectable" 
  [value]="selectedPlan"
  (valueChange)="onPlanChange($event)"
  ariaLabel="Plan selection">
  <ion-tag label="Basic"></ion-tag>
  <ion-tag label="Standard"></ion-tag>
  <ion-tag label="Premium"></ion-tag>
</ion-tag-group>
```
*Demonstrates a selectable tag group with single selection (radio behavior) and value change handling.*

### Selectable tag group with multi-selection

```html
<ion-tag-group 
  name="filterCategories"
  type="selectable"
  multiSelect="true"
  [value]="selectedCategories"
  (valueChange)="onCategoryFilterChange($event)"
  hideOverflow="true"
  ariaLabel="Filter by category">
  <ion-tag *ngFor="let category of categories" [label]="category.name"></ion-tag>
</ion-tag-group>
```
*Demonstrates a multi-selectable tag group with overflow handling and dynamic tag content.*

### Removable tag group

```html
<ion-tag-group 
  type="removable" 
  size="sm"
  ariaLabel="Selected items">
  <ion-tag 
    *ngFor="let item of selectedItems" 
    [label]="item.name"
    (tagRemoved)="onItemRemoved($event)">
  </ion-tag>
</ion-tag-group>
```
*Demonstrates a removable tag group where users can delete items by clicking the X icon.*