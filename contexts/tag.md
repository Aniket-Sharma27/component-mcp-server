---
realComponent: "ion-tag"
description: A flexible tag component supporting non-interactive, selectable, and removable variants with design system styling, truncation modes, and enhancers
themes: ["ion-modern-light-ds", "ion-modern-dark-ds"]
props:
  - name: name
    type: string
    category: content
    required: false
    default: none found
    values: []
    designTokens: {}
  - name: type
    type: enum
    category: visual
    required: false
    default: "non-interactive"
    values: ["non-interactive", "selectable", "removable"]
    designTokens: {}
  - name: disabled
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
  - name: disabledInternal
    type: boolean
    category: behavioral
    required: false
    default: none found
    values: []
    designTokens: {}
  - name: readOnly
    type: boolean
    category: visual
    required: false
    default: none found
    values: []
    designTokens: {}
  - name: size
    type: enum
    category: visual
    required: false
    default: "md"
    values: ["sm", "md", "lg"]
    designTokens:
      sm:
        resolvesTo: none found
        tokenChain: component size tokens not traced to final values
        appliesToCssProperty: min-height, padding, border-radius, font-size
      md:
        resolvesTo: none found
        tokenChain: component size tokens not traced to final values
        appliesToCssProperty: min-height, padding, border-radius, font-size
      lg:
        resolvesTo: none found
        tokenChain: component size tokens not traced to final values
        appliesToCssProperty: min-height, padding, border-radius, font-size
  - name: label
    type: string
    category: content
    required: false
    default: none found
    values: []
    designTokens: {}
  - name: maxWidth
    type: string
    category: visual
    required: false
    default: "200px"
    values: []
    designTokens: {}
  - name: startEnhancer
    type: ReadonlyEnhancer
    category: content
    required: false
    default: none found
    values: []
    designTokens: {}
  - name: endEnhancer
    type: ReadonlyEnhancer
    category: content
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
  - name: truncationMode
    type: enum
    category: visual
    required: false
    default: "end"
    values: ["start", "middle", "end"]
    designTokens: {}
  - name: selected
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
  - name: disableDefaultTooltip
    type: boolean
    category: behavioral
    required: false
    default: false
    values: []
    designTokens: {}
  - name: customTooltip
    type: ITagTooltipOptions
    category: behavioral
    required: false
    default: none found
    values: []
    designTokens: {}
  - name: badgeOptions
    type: ITagBadgeOptions
    category: visual
    required: false
    default: none found
    values: []
    designTokens: {}
  - name: takeFullWidth
    type: boolean
    category: behavioral
    required: false
    default: none found
    values: []
    designTokens: {}
  - name: active
    type: boolean
    category: visual
    required: false
    default: false
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
    type: function
    category: behavioral
    required: false
    default: "() => void"
    values: []
    designTokens: {}
  - name: removeTag
    type: function
    category: behavioral
    required: false
    default: "() => void"
    values: []
    designTokens: {}
events:
  - name: tagRemoved
    payloadType: CustomEvent<ITagRemoveEventArgs>
    firesWhen: When a removable tag's remove button is clicked or programmatic removal is triggered via removeTag method/tagRemoved event emission
    detailAccess: event.detail.name (string), event.detail.label (string)
    bindingSyntax: (tagRemoved)="onTagRemoved($event)"
  - name: selectionChange
    payloadType: CustomEvent<ITagChangeEventArgs>
    firesWhen: When a selectable tag is clicked or activated via keyboard, toggling its selection state
    detailAccess: event.detail.name (string), event.detail.label (string), event.detail.selection (boolean)
    bindingSyntax: (selectionChange)="onSelectionChange($event)"
  - name: tagClicked
    payloadType: CustomEvent<ITagRemoveEventArgs>
    firesWhen: When a removable tag is clicked (not just the remove button), targeting the tag container itself
    detailAccess: event.detail.name (string), event.detail.label (string)
    bindingSyntax: (tagClicked)="onTagClicked($event)"
  - name: focusIn
    payloadType: CustomEvent<void>
    firesWhen: When the tag receives browser focus
    detailAccess: void, event.detail is undefined
    bindingSyntax: (focusIn)="onFocusIn($event)"
  - name: focusOut
    payloadType: CustomEvent<void>
    firesWhen: When the tag loses browser focus
    detailAccess: void, event.detail is undefined
    bindingSyntax: (focusOut)="onFocusOut($event)"
jointTokens: []
propInteractions:
  - "type determines interactive behavior and container class selection - non-interactive tags display static content, selectable tags emit selectionChange on click, removable tags show remove button and emit tagRemoved"
  - "endEnhancer positioning affects remove button visibility in type=removable - remove button still renders after end enhancer if present"
  - "maxWidth interacts with truncationMode to handle overflowing text - truncation only applies when content exceeds maxWidth"
  - "selected prop only affects type=selectable tags - controls visual selection state and determines ariaLabelMessage content"
  - "readOnly only affects type=removable tags - when true, removes remove button and changes ariaLabel to 'readonly [label]'"
  - "disableDefaultTooltip controls default tooltip behavior independently of customTooltip - when true, prevents automatic label overflow tooltip even if label is truncated"
  - "takeFullWidth overrides maxWidth behavior - when true, sets width: 100% and ignores maxWidth constraint"
  - "size supports MQ design strings parsed by MqDesignStringParserService for responsive sizing"
  - "disabled or disabledInternal both suppress interaction regardless of which one is true - combined in finalDisabledState"
  - "active prop only affects type=removable tags - visual active state indicator"
  - "tabIndex is computed based on type and disabled state - selectable/removable tags get tabindex='0' when enabled, otherwise '-1'"
needsReview:
  - "No design token values traced for size prop (sm, md, lg) - component CSS references tokens like --ion-comp-tag-non-selectable-container-sizing-min-height-md but final resolved pixel values not found in provided token files"
  - "No color/theme-specific token data traced for type, selected, disabled, or other visual state combinations - ds_tokens.css contains only base palette colors, not component-specific tag color tokens"
  - "border-radius, padding, and spacing values not resolved to final pixel values for any size variant"
  - "Typography font-size not traced to final values for different size variants (sm, md, lg)"
  - "Dark theme design tokens for tag colors, states (active, disabled, selected) could not be traced - only light theme base palette colors found in ds_tokens.css"
  - "Design tokens for focus ring, hover states, and other interactive states not traced from provided token files"
  - "Component-level tag tokens in tag-ds.css (--ion-comp-tag-*) not resolved to base leonardo colors or final values"
  - "MQ design string parsing results not verifiable without runtime screen size context - defaults to md when MQ strings used"
  - "badgeOptions prop described but specific badge styling tokens and badgeIntent color values not traced"
  - "customTooltip behavior documented but tooltip service implementation details not verified"
  - "endEnhancer interaction with remove button positioning may need clarification on z-index or overlap scenarios"
---

## Usage Notes

Boolean props on this component must always be passed with an explicit string value — e.g. `disabled="true"` or `[disabled]="isDisabled"` — never as bare attribute presence (e.g. `disabled` alone, with no value). Bare attribute presence is a native HTML convention this component does NOT support; it will not be interpreted as true.

## name

Controls the tag's identifier, used for form submission and event payload identification. This prop is not derivable from visual design and should generally be left at its default unless the developer's request specifically calls for it.

**Visual property:** none (data/identification)

**Default behavior:**
- Optional property for unique identification
- Included in event payloads for event.target.name tracking
- Used in form data when tags are part of a form
- Defaults to undefined if not set

**Event payload usage:**
- tagRemoved event: emits event.detail.name
- selectionChange event: emits event.detail.name
- tagClicked event: emits event.detail.name

## type

Controls the interactive behavior and visual structure of the tag. This is a critical prop that determines all other interactive behaviors and what events are available.

**Visual cues:**
- "non-interactive": Static tag with no interactive elements, no remove button, no selection indicators
- "selectable": Clickable tag that toggles selection state, shows selection indicators when selected
- "removable": Tag with remove button (X icon) on the right side when not readOnly

**When to use:**
- "non-interactive": Displaying static information, badges, categories, or status indicators that users shouldn't modify
- "selectable": Multi-select scenarios where users choose between options (e.g. filter tags, category selection)
- "removable":-items that users can dismiss or remove (e.g. selected filters, search keywords, list items)

**Behavioral differences:**
- type="non-interactive": No click handlers, no keyboard interaction, no selection state
- type="selectable": Toggles selected state on click/keyboard, emits selectionChange, supports Enter/Space keyboard activation
- type="removable": Shows remove button, emits tagRemoved on remove button click, emits tagClicked on tag click, supports Delete key for removal

**Container class mapping:**
- type="removable" && !readOnly: .ion-ds-tag-non-selectable-container-with-remove
- type="selectable": .ion-ds-tag-selectable-container
- otherwise: .ion-ds-tag-non-selectable-container

## disabled

Controls whether the tag is visually and functionally disabled. When true, prevents all user interaction.

**Visual cues:**
- When true: Tag appears non-interactive with disabled styling (.disabled CSS class)
- Suppressed interactive elements (remove button becomes non-functional, click handlers don't fire)
- Applied via finalDisabledState which combines disabled and disabledInternal

**When to use:**
- Set true when tag action is not currently available (e.g. feature disabled, permission-based restrictions)
- DisabledInternal prop used internally by tag-group to disable individual tags
- Either disabled=true or disabledInternal=true results in fully disabled state

**Interaction with other props:**
- Overrides interactive behavior regardless of type value
- When true, remove button pointer events are disabled
- When true, click handlers don't emit events
- Affects computed tabIndex (disabled tags get tabindex="-1")

## disabledInternal

Internal API used by tag-group to set disabled state on individual tags. This avoids letting tag group set disabled directly to maintain clear API boundaries.

**Visual property:** Same as disabled (combined in finalDisabledState)

**When to use:**
- This is an internal prop not intended for direct use - use disabled instead
- Used by tag-group component to disable individual tags when the entire group is disabled
- Combined with disabled via finalDisabledState logic

**Behavioral notes:**
- Has same visual and functional effects as disabled prop
- Allows tag-group to control individual tag state without modifying user-set disabled prop
- When either disabled=true or disabledInternal=true, tag is fully disabled

## readOnly

Controls whether a removable tag's remove button is visible and functional. Only applicable when type="removable".

**Visual cues:**
- When true: Remove button is hidden, tag appears as non-interactive
- Affects container class (when type="removable" && !readOnly shows remove button)
- Changes ariaLabel to include "readonly" prefix

**When to use:**
- Set true for removable tags that should not be removed (e.g., mandatory filters, locked items)
- Only meaningful when type="removable"

**Behavioral impact:**
- When type="removable" and readOnly=true:
  - Remove button not rendered (see tag.component.html line 21: @if(type === "removable" && !readOnly))
  - Container uses .ion-ds-tag-non-selectable-container instead of .ion-ds-tag-non-selectable-container-with-remove
  - Aria-label becomes: "readonly [label]"
- When type="removable" and readOnly=false:
  - Remove button is visible and functional
  - Container uses .ion-ds-tag-non-selectable-container-with-remove
  - Aria-label becomes: "remove [label]"

## size

Controls the tag's sizing via CSS size classes and supports responsive MQ design strings.

**Visual cues:**
- sm: Small tag, compact spacing, smaller font size
- md: Medium tag (default), standard spacing and typography
- lg: Large tag, more prominent spacing and larger font size

**Size-specific CSS classes:**
- .ion-ds-sm: Applied to tag wrapper elements for small size
- .ion-ds-md (default): Applied for medium size
- .ion-ds-lg: Applied for large size

**When to use:**
- sm: Compact layouts, navigation areas, dense content, or when many tags displayed together
- md: Standard rows, form controls, general use cases (default)
- lg: Prominent display, hero sections, or when tags need visual emphasis

**Responsive behavior:**
- Supports MQ design strings parsed by MqDesignStringParserService
- MQ string example: "xs=sm;sm=md;md=md;lg=lg;xl=lg;xxl=md"
- Returns default "md" if invalid size string provided

**Affects:**
- Container min-height, padding, border-radius, gap
- Label/enhancer font sizes and related typography
- Remove button sizing (min-height, min-width, padding)

## label

Controls the text content displayed inside the tag. This is the primary content of the tag.

**Visual cues:**
- Displays text in the center of the tag
- Text color and styling determined by tag type and state (disabled, selected)
- Subject to truncation when maxWidth is exceeded

**When to use:**
- Primary method for conveying tag meaning through text
- Required for meaningful tag content (empty tags render with no visible content unless enhancers present)

**Interaction with other props:**
- Label overflow handled by truncationMode and maxWidth props
- Label content influences ariaLabel (if ariaLabel not explicitly set)
- Label is split into two parts (labelOnUIFirstPart, labelOnUISecondPart) when truncationMode="middle"

**Accessibility:**
- When ariaLabel is not explicitly set, label value is used as fallback
- When ariaLabel is explicitly provided, overrides label for screen readers

## maxWidth

Controls the maximum width constraint for the tag, affecting when truncation occurs.

**Visual cues:**
- Sets max-width CSS style on tag element
- Default value is "200px" from tag.stories.ts and index.md
- When label exceeds maxWidth, truncation triggers based on truncationMode value

**When to use:**
- Override default when consistent sizing needed across multiple tags
- Set to larger value when expecting long labels
- Set to smaller value for compact layouts

**Interaction with truncationMode:**
- Truncation only activates when label content exceeds maxWidth
- Different truncation modes handle overflowing differently:
  - "start": Truncates beginning, ellipsis at start
  - "middle": Splits label into two parts, ellipsis between
  - "end": Truncates end, ellipsis at end (default)

**CSS application:**
- Applied via [ngStyle]="{'max-width': maxWidth ? maxWidth : '200px'}"
- Affects container width constraint and label overflow behavior

## startEnhancer

Adds visual enhancer (text, icon, or category) at the beginning (left side) of the tag.

**Visual cues:**
- Renders before label in tag content
- Type determined by enhancer.type property: "text", "icon", or "category"
- Color and styling determined by tag type and state (disabled, selected)
- Size scaled relative to tag size via getIconSizeForTag()

**When to use:**
- Add pictorial context or icons at left side of label
- Display category badges or status indicators at start
- Show additional information or metadata prefix

**ReadonlyEnhancer interface:**
- value: string - The content of the enhancer (icon name, category name, or text)
- type: "text" | "icon" | "category" - The type of enhancer
- ariaLabel?: string - Accessibility label for the enhancer
- iconFontFamily?: string - Font family for icons (when type="icon")
- iconColor?: string - Specific color for icons (when type="icon")

**Examples from tagSample component:**
- Icon: `{ value: "add", type: "icon" }`
- Category: `{ value: "category1", type: "category" }` (valid values: red, amber, yellow, mint, green, blue, purple, navy, pink, sky)

## endEnhancer

Adds visual enhancer (text, icon, or category) at the end (right side) of the tag, positioned before the remove button in type="removable".

**Visual cues:**
- Renders after label in tag content
- Type determined by enhancer.type property: "text", "icon", or "category"
- Color and styling determined by tag type and state (disabled, selected)
- Size scaled relative to tag size via getIconSizeForTag()
- When type="removable", positioned before remove button

**When to use:**
- Add pictorial context or icons at right side of label
- Display status indicators or metadata suffix
- Show trailing information or secondary content

**Interaction with type:**
- In type="removable", endEnhancer appears before the remove button
- In other type values, endEnhancer appears at tag's right edge

**ReadonlyEnhancer interface:**
Same as startEnhancer:
- value: string - The content of the enhancer
- type: "text" | "icon" | "category" - The type of enhancer
- ariaLabel?: string - Accessibility label for the enhancer
- iconFontFamily?: string - Font family for icons (when type="icon")
- iconColor?: string - Specific color for icons (when type="icon")

## ariaLabel

Provides custom accessibility label for screen readers and assistive technologies.

**Visual property:** none (accessibility-only)

**Default behavior:**
- Defaults to label value if not explicitly set (see tag.component.ts line 468-471)
- ariaLabelMessage getter constructs full label based on type and state:
  - type="selectable": Includes "(not) selected" state: "[label] selected" or "[label] not selected"
  - type="removable": Prefixes with "remove" or "readonly": "remove [label]" or "readonly [label]"
  - type="non-interactive": Uses label directly or provided ariaLabel

**When to use:**
- Override default behavior for specific accessibility needs
- Provide more descriptive label than tag text suggests
- Set custom label for screen readers that differs from visual label
- Use when label doesn't fully convey tag meaning to assistive technologies

**Priority for aria-label attribute:**
1. Explicitly set _ariaLabel property
2. Computed ariaLabelMessage based on type, selected, readOnly, label
3. Final aria-label constructed with state information

## truncationMode

Controls how truncated label text is displayed when content exceeds maxWidth.

**Visual cues:**
- "start": Truncates beginning, ellipsis at left: "...is a very long label"
- "middle": Splits label into two parts with ellipsis between: "...is a very ...ng label"
- "end": Truncates end, ellipsis at right (default): "This is a ver..."

**When to use:**
- "end": Most common default pattern for preserving beginning of text (default)
- "start": When end of text is more important (e.g., file names where extension is key)
- "middle": When both beginning and end are important, truncates middle instead

**Implementation details:**
- "start": Applies CSS .truncation-direction-rtl which sets direction: rtl
- "middle": Splits label at index = Math.round(label.length * 0.75), renders in two spans with ellipsis between
- "end": Normal text truncation with text-overflow: ellipsis (CSS default)

**Interaction with maxWidth:**
- Truncation only activates when labelElement.scrollWidth > labelElement.clientWidth
- Overflow detection in labelOverflowHandler() method
- Only affects visual presentation, not the actual label property value

## selected

Controls the selected state for tags with type="selectable". This prop only affects selectable tags.

**Visual cues:**
- When true: Tag shows selected state with selection styling
- When false: Tag shows unselected state
- Affects .selected CSS class on tag container
- Changes ariaLabelMessage to include "selected" or "not selected"

**When to use:**
- Set true when tag should appear selected (e.g., active filter, selected category)
- Set false when tag should appear unselected (default)
- Only meaningful when type="selectable" - ignored by other type values

**Behavioral interaction:**
- User clicking/selectable tag toggles this value automatically
- Changes trigger selectionChange event emission
- ARIa-label includes selection state for accessibility
- Selection state persisted through selected prop

**Event emission:**
- When toggled, emits { name, label, selection: true/false } in selectionChange event
- Event fired on click and keyboard activation (Enter/Space keys)

## disableDefaultTooltip

Controls whether the default tooltip behavior is suppressed. When true, prevents automatic display of label tooltip when tag content is truncated.

**Visual property:** none (behavioral)

**When to use:**
- Set true to prevent default tooltip from appearing on hover
- Useful when customTooltip is used instead
- Set true when automatic label tooltip is not desired

**Default behavior:**
- When false (default): Default tooltip shows on hover when label is truncated
- Tooltip shows truncated label content to help users read full text
- Only appears when labelElement.scrollWidth > labelElement.clientWidth

**Interaction with customTooltip:**
- customTooltip.content takes priority over default tooltip behavior
- If customTooltip.content is set, shows custom tooltip instead of default
- disableDefaultTooltip can be set to true to prevent default even when no custom tooltip

**Implementation:**
- Checked in tagHoverIn() method at tag.component.ts line 219
- Default tooltip only created if !disableDefaultTooltip and label is overflowing
- Custom tooltip service for both default and custom tooltips

## customTooltip

Provides custom tooltip content and configuration, overriding the default tooltip behavior.

**Visual property:** Tooltip content displayed on hover

**When to use:**
- Set custom tooltip content different from truncated label
- Display additional information in tooltip beyond label text
- Use when custom tooltip behavior is needed

**ITagTooltipOptions interface:**
- content: string - The text content to display in custom tooltip

**Behavior:**
- Takes priority over default tooltip behavior
- Shows on tag hover when content is set
- Custom tooltip instance created via tooltipService.createTooltip()
- Placement fixed to "bottom", trigger set to "manual", openDelay of 300ms

**Interaction with disableDefaultTooltip:**
- If customTooltip.content is provided, it's shown regardless of disableDefaultTooltip
- If disableDefaultTooltip=true AND no custom content, no tooltip appears
- If disableDefaultTooltip=false AND custom content provided, custom tooltip appears

**Implementation:**
- Checked in tagHoverIn() method at tag.component.ts line 211
- Created with position relative to tagElement reference
- Destroyed on mouse out via tagHoverOut() method

## badgeOptions

Provides configuration for displaying a badge on the tag.

**Visual cues:**
- When showBadge=true: Badge appears positioned absolute at top-right of tag
- Badges use ion-badge component with styling from tag-ds.css
- Positioned with top: 0, right: 0, transform: translate(50%, -50%)

**ITagBadgeOptions interface:**
- showBadge: boolean - Whether badge should be displayed
- badgeIntent?: string - The intent color for the badge (e.g., "info")

**When to use:**
- Set showBadge=true to display notification count or status indicator
- Use badgeIntent to set semantic color (info, warning, error, etc.)
- Common use cases: notification counts, status indicators, count badges

**Implementation details:**
- Rendered in tag.component.html line 27-29
- Badge uses parsedSize for its size prop
- Badge positioned absolutely with .ion-ds-tag-badge CSS class
- Badge intent defaults to "info" if not provided (tag.component.ts line 133)

**Interaction:**
- Badge appears on top of tag content, visually overlaid
- Badge presence doesn't affect tag dimensions or layout
- Badge positioned using CSS absolute positioning with negative margin transform

## takeFullWidth

Controls whether the tag should expand to fill its container width. When true, overrides maxWidth and other width constraints.

**Visual property:** none (layout)

**When to use:**
- Set true when tag should span full container width
- Use for full-width tag display scenarios
- Common use case: internal usage within combo-box as mentioned in code comments

**Behavior:**
- When true: Sets width: 100% via ngStyle binding
- When false: Sets width: fit-content via ngStyle binding (default)
- Overrides maxWidth constraint when set to true
- Internal API, documented as "created for usage internally in combo box"

**Implementation:**
- Applied via [ngStyle]="{... width: takeFullWidth ? '100%' : 'fit-content' }"
- Located in tag.component.html line 3
- Use when tag should expand to fill parent container regardless of content

## active

Controls active state visual indicator for removable tags. This prop only affects type="removable" tags.

**Visual cues:**
- When true: Tag shows active state with .active CSS class
- Only applied when tag type is "removable" (see setter validation)
- Affects container and remove button styling

**When to use:**
- Set true to show active/removing state indication
- Use for visual feedback during removal operations
- Only meaningful for type="removable" - ignored by other type values

**Behavioral restrictions:**
- Setter only applies when type === "removable" (tag.component.ts line 500)
- When type is "removable" and active=true, active state styling applied
- When type is not "removable", active value is not applied to the tag

**Visual impact:**
- Applies .active CSS class to container and related elements
- Affects tag background, border colors, and other visual properties
- Used for visual feedback during interactions or multi-step removal processes

## tabIndex

Controls keyboard focusability via HTML tabindex attribute. Computed based on tag type and disabled state.

**Visual property:** none (accessibility/behavior)

**Default behavior (auto-computed):**
- Interactive tags (selectable or removable) + not disabled: tabindex="0"
- Non-interactive or disabled tags: tabindex="-1"

**When to use:**
- Override default tabIndex for custom focus management
- Set tabindex="0" to make tag focusable via keyboard navigation
- Set tabindex="-1" to remove from tab order while still being focusable programmatically

**Computation logic:**
```typescript
get tabIndex(): string {
  if ((this.type === "selectable" || this.type === "removable") && !this.disabled) {
    return this._tabIndex ?? "0";  // Default to "0" if not set
  }
  return this._tabIndex ?? "-1";   // Default to "-1" if not set
}
```

**Accessibility impact:**
- tabindex="0": Tag can receive keyboard focus via Tab key
- tabindex="-1": Tag not reachable via Tab navigation
- Combined with focusIn/focusOut events for complete accessibility

## setFocus

Provides programmatic focus control for the tag. Focuses the appropriate element based on tag type.

**Visual property:** none (behavioral)

**When to use:**
- This is a behavioral prop not derivable from visual design
- Should generally be left at its default unless specifically called for in request
- Use when programmatic focus is needed (though this is likely internal API)

**Implementation:**
- find appropriate element to focus based on type:
  - type="selectable": focuses .ion-ds-tag-selectable-container-outer
  - type="removable": focuses .ion-ds-tag-non-selectable-container-outer (or removeButton.shadowRoot)
- Uses shadowRoot.querySelector to find elements in web component shadow DOM

**Method signature:**
```typescript
setFocus() {
  let targetElement: any;
  if (this.type === "selectable") {
    targetElement = this.shadowRoot.querySelector(".ion-ds-tag-selectable-container-outer");
  } else if (this.type === "removable") {
    targetElement = this.removeButton?.nativeElement || this.shadowRoot.querySelector(".ion-ds-tag-non-selectable-container-outer");
  }
  if (targetElement) {
    targetElement.focus();
  }
}
```

**Usage:**
- Likely internal API for parent components (like tag-group) to control focus
- Enables programmatic focus management for accessibility

## removeTag

Provides programmatic tag removal functionality. Internal API for triggering tag removal.

**Visual property:** none (behavioral)

**When to use:**
- This is a behavioral prop not derivable from visual design
- Should generally be left at its default unless specifically called for in request
- Likely internal API for parent components (like tag-group) to trigger removal

**Implementation:**
- Default function calls onRemoveClick() which:
- Emits tagRemoved event with { name, label }
- Removes DOM element via element.nativeElement.remove()
- Cleans up via ngOnDestroy()

**Method signature:**
```typescript
removeTag: (() => void) | undefined = () => {
  this.onRemoveClick();
};
```

**Behavior:**
- Emits tagRemoved event before removing element
- Cleans up DOM and component lifecycle
- May be called by parent components like tag-group to programmatically remove tags
- Used as programmatic alternative to user clicking remove button

## Events

### tagRemoved

Event triggered when a user removes a removable tag by clicking the remove button, or when tag is programmatically removed.

**Emitted args:** CustomEvent<ITagRemoveEventArgs>

**ITagRemoveEventArgs interface:**
- name: string - The tag's identifier
- label: string - The tag's display label

**When to use:**
- Clean up data model when user removes a tag
- Provide user feedback (e.g., snackbar, undo functionality) after removal
- Update parent component state when tags are removed
- Track removal analytics

**How to use:**
```typescript
onTagRemoved(event: CustomEvent<ITagRemoveEventArgs>) {
  const { name, label } = event.detail;
  // Access payload via event.detail, not $event itself
  console.log(`Removed tag: ${label} (${name})`);
  // Clean up your data model here
  this.tags = this.tags.filter(tag => tag.name !== name);
}
```

**Binding syntax:**
```html
<ion-tag [type]="'removable'" [label]="label" (tagRemoved)="onTagRemoved($event)"></ion-tag>
```

**Triggers:**
- User clicks remove button (X icon) on type="removable" tag
- Programmatic removal via removeTag() method (rare in normal usage)

### selectionChange

Event triggered when a selectable tag's selection state changes, either by user click or keyboard activation (Enter/Space keys).

**Emitted args:** CustomEvent<ITagChangeEventArgs>

**ITagChangeEventArgs interface:**
- name: string - The tag's identifier
- label: string - The tag's display label
- selection: boolean - The new selection state (true if selected, false if unselected)

**When to use:**
- Update data model when user selects/deselects tags
- Synchronize selection state across multiple components
- Sync with form controls when tags represent selections
- Track selection analytics

**How to use:**
```typescript
onSelectionChange(event: CustomEvent<ITagChangeEventArgs>) {
  const { name, label, selection } = event.detail;
  // Access payload via event.detail, not $event itself
  console.log(`${label} selection changed to: ${selection}`);
  // Update your data model here
  if (selection) {
    this.selectedTags = [...this.selectedTags, name];
  } else {
    this.selectedTags = this.selectedTags.filter(tag => tag !== name);
  }
}
```

**Binding syntax:**
```html
<ion-tag [type]="'selectable'" [label]="label" (selectionChange)="onSelectionChange($event)"></ion-tag>
```

**Triggers:**
- User clicks on type="selectable" tag
- User presses Enter or Space key while type="selectable" tag is focused

**Selection behavior:**
- Event fires both when selecting and when deselecting
- selection boolean in payload indicates new state
- Component automatically toggles selected state before emitting

### tagClicked

Event triggered when user clicks on a removable tag (not specifically the remove button). Emits tag identifier and label.

**Emitted args:** CustomEvent<ITagRemoveEventArgs>

**ITagRemoveEventArgs interface:**
- name: string - The tag's identifier
- label: string - The tag's display label

**When to use:**
- Track tag click analytics separate from removal action
- Provide feedback when user clicks on tag body
- Show additional information on tag body click (e.g., tag details)

**How to use:**
```typescript
onTagClicked(event: CustomEvent<ITagRemoveEventArgs>) {
  const { name, label } = event.detail;
  // Access payload via event.detail, not $event itself
  console.log(`Tag clicked: ${label} (${name})`);
  // Show tag details or perform other action
  this.showTagDetails(name);
}
```

**Binding syntax:**
```html
<ion-tag [type]="'removable'" [label]="label" (tagClicked)="onTagClicked($event)"></ion-tag>
```

**Triggers:**
- User clicks on tag body (not remove button)
- Only relevant for type="removable" tags

**Difference from tagRemoved:**
- tagClicked fires on any tag body click
- tagRemoved fires specifically on remove button click or programmatic removal

### focusIn

Event triggered when tag receives browser focus via keyboard navigation or programmatic focus.

**Emitted args:** CustomEvent<void>

**When to use:**
- Track focus events for accessibility compliance
- Set up focus-related visual effects or state
- Manage focus-related application state

**How to use:**
```typescript
onFocusIn(event: CustomEvent<void>) {
  // event.detail is undefined for void payload
  console.log('Tag received focus');
  // Update your UI or manage state as needed
  this.tagFocused = true;
}
```

**Binding syntax:**
```html
<ion-tag [label]="label" (focusIn)="onFocusIn($event)"></ion-tag>
```

**Triggers:**
- Tag receives focus via Tab key navigation
- Tag receives focus via programmatic setFocus() call
- Tag receives focus via element.focus() directly

### focusOut

Event triggered when tag loses browser focus, typically when user tabs away or clicks elsewhere.

**Emitted args:** CustomEvent<void>

**When to use:**
- Track focus leave events for accessibility compliance
- Clean up focus-related visual effects or state
- Validate or save data when focus leaves tag
- Manage focus-related application state

**How to use:**
```typescript
onFocusOut(event: CustomEvent<void>) {
  // event.detail is undefined for void payload
  console.log('Tag lost focus');
  // Update your UI or manage state as needed
  this.tagFocused = false;
}
```

**Binding syntax:**
```html
<ion-tag [label]="label" (focusOut)="onFocusOut($event)"></ion-tag>
```

**Triggers:**
- User tabs away from tag to another focusable element
- User clicks elsewhere in the application
- Tag loses focus via programmatic blur

## Examples

### Non-interactive Tag

```html
<ion-tag
  [type]="'non-interactive'"
  [label]="label"
  [size]="size"
  [disabled]="disabled"
  [maxWidth]="maxWidth"
  [startEnhancer]="startEnhancer"
  [endEnhancer]="endEnhancer"
  [ariaLabel]="ariaLabel"
  [truncationMode]="truncationMode">
</ion-tag>
```
Demonstrates basic non-interactive tag with enhancers and truncation control.

### Removable Tag with Event Handler

```html
<ion-tag
  [type]="'removable'"
  [label]="label"
  [size]="size"
  [disabled]="disabled"
  [startEnhancer]="startEnhancer"
  [endEnhancer]="endEnhancer"
  [ariaLabel]="ariaLabel"
  [truncationMode]="truncationMode"
  (tagRemoved)="onTagRemoved($event)">
</ion-tag>
```
Demonstrates removable tag with tagRemoved event handler for removal notification and cleanup.

### Selectable Tag with Selection Handler

```html
<ion-tag
  [type]="'selectable'"
  [label]="label"
  [size]="size"
  [selected]="selected"
  [disabled]="disabled"
  [startEnhancer]="startEnhancer"
  [endEnhancer]="endEnhancer"
  [ariaLabel]="ariaLabel"
  [truncationMode]="truncationMode"
  (selectionChange)="onSelectionChange($event)">
</ion-tag>
```
Demonstrates selectable tag with controlled selected state and selection change event handler.

### Complete Event Binding Example

```html
<ion-tag
  [type]="'removable'"
  [label]="'My Removable Tag'"
  [name]="'tag1'"
  [ariaLabel]="'My custom aria label'"
  [size]="'md'"
  [startEnhancer]="{ value: 'category1', type: 'category' }"
  (tagRemoved)="onTagRemoved($event)"
  (tagClicked)="onTagClicked($event)"
  (focusIn)="onFocusIn($event)"
  (focusOut)="onFocusOut($event)">
</ion-tag>
```

Demonstrates all events bound to a single removable tag with complete handler implementation:

```typescript
onTagRemoved(event: CustomEvent<ITagRemoveEventArgs>) {
  const { name, label } = event.detail;
  console.log(`Tag removed: ${label} (${name})`);
  this.tags = this.tags.filter(tag => tag.name !== name);
}

onTagClicked(event: CustomEvent<ITagRemoveEventArgs>) {
  const { name, label } = event.detail;
  console.log(`Tag clicked: ${label} (${name})`);
  this.showTagDetails(name);
}

onFocusIn(event: CustomEvent<void>) {
  console.log('Tag received focus');
  this.tagFocused = true;
}

onFocusOut(event: CustomEvent<void>) {
  console.log('Tag lost focus');
  this.tagFocused = false;
}
```

### Storybook Examples

From tag.stories.ts - NonInteractivePlayground:

```html
<ion-tag
  [type]="'non-interactive'"
  [label]="label"
  [disabled]="disabled"
  [maxWidth]="maxWidth"
  [startEnhancer]="startEnhancer"
  [endEnhancer]="endEnhancer"
  [size]="size"
  [truncationMode]="truncationMode"
  (selectionChange)="onSelectionChange($event)"
  (tagRemoved)="onTagRemoved($event)">
</ion-tag>
```
Demonstrates non-interactive playground with configurable props and event bindings.

From tag.stories.ts - SelectablePlayground:

```html
<ion-tag
  [type]="'selectable'"
  [label]="label"
  [size]="size"
  [selected]="selected"
  [disabled]="disabled"
  [maxWidth]="maxWidth"
  [startEnhancer]="startEnhancer"
  [endEnhancer]="endEnhancer"
  [ariaLabel]="ariaLabel"
  [truncationMode]="truncationMode"
  (selectionChange)="onSelectionChange($event)"
  (tagRemoved)="onTagRemoved($event)">
</ion-tag>
```
Demonstrates selectable playground with selection state and selectionChange event.

From tag.stories.ts - RemovablePlayground:

```html
<ion-tag
  [type]="'removable'"
  [label]="label"
  [size]="size"
  [disabled]="disabled"
  [maxWidth]="maxWidth"
  [startEnhancer]="startEnhancer"
  [endEnhancer]="endEnhancer"
  [ariaLabel]="ariaLabel"
  [truncationMode]="truncationMode"
  (selectionChange)="onSelectionChange($event)"
  (tagRemoved)="onTagRemoved($event)">
</ion-tag>
```
Demonstrates removable playground with tagRemoved event.

From tag-sample/tag-tab.component.html:

```html
<ion-tag #sampleTag [name]="name" [readonly]="readOnly" [selected]="selected" [truncationMode]="truncationMode" [type]="tagType" [label]="tagLabel" [disabled]="disabled"
  [size]="sizeString" [maxWidth]="maxWidth" [startEnhancer]="startEnhancer" [endEnhancer]="endEnhancer"
  [attr.aria-label]="tagAriaLabel" (selectionChange)="selectionChange($event)"
  (tagRemoved)="tagRemoved($event)"></ion-tag>
```
Demonstrates sample tag with all interactive props bound and event handlers for selection and removal.