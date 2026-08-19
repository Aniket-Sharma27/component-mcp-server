---
realComponent: ion-date-time-picker
description: A visual date and time picker component with calendar view, customizable date ranges, and support for tenor/tag-based date selection.
themes: [modern-light-ds, modern-dark-ds]
apiTypes: ["element"]
props:
  - name: size
    type: MQ<string>
    category: visual
    required: false
    default: "md"
    values: []
    designTokens: {}
  - name: disabled
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
  - name: transpose
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
  - name: disableWeekends
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
  - name: enableDropdowns
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
  - name: hideNavigation
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
  - name: fixedWeekRows
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
  - name: locale
    type: string
    category: content
    required: false
    default: ""
    values: []
    designTokens: {}
  - name: monthFormat
    type: "MonthFormat"
    category: visual
    required: false
    default: long
    values: [long, short, numeric, narrow, "2-digit"]
    designTokens: {}
  - name: weekFormat
    type: "WeekFormat"
    category: visual
    required: false
    default: short
    values: [long, short, narrow]
    designTokens: {}
  - name: numberOfCalendars
    type: number
    category: visual
    required: false
    default: 1
    values: []
    designTokens: {}
  - name: weekStartsOn
    type: number
    category: visual
    required: false
    default: 1
    values: []
    designTokens: {}
  - name: initDate
    type: Date
    category: content
    required: false
    default: "none found in interface, computed from Temporal.Now.plainDateISO()"
    values: []
    designTokens: {}
  - name: value
    type: "Date | null"
    category: content
    required: false
    default: "no initial value selected"
    values: []
    designTokens: {}
  - name: minDate
    type: Date
    category: content
    required: false
    default: "toNativeDate(Temporal.PlainDate.from(GLOBAL_MIN_DATE))"
    values: []
    designTokens: {}
  - name: maxDate
    type: Date
    category: content
    required: false
    default: "toNativeDate(Temporal.PlainDate.from(\"2100-12-31\"))"
    values: []
    designTokens: {}
  - name: dateDisabled
    type: "(date: Date) => boolean"
    category: accessibility
    required: false
    default: "() => false"
    values: []
    designTokens: {}
  - name: dateTooltip
    type: "(date: Date) => string | IonElement"
    category: content
    required: false
    default: "() => \"\""
    values: []
    designTokens: {}
  - name: mode
    type: "CalendarPickerMode"
    category: content
    required: false
    default: "date-time"
    values: [date, time, "date-time"]
    designTokens: {}
  - name: tenorIntent
    type: "TenorIntent"
    category: visual
    required: false
    default: secondary
    values: [primary, secondary, negative, positive, buy, sell, inverse, on-light, on-dark]
    designTokens:
      primary:
        light:
          resolvesTo: "#007de0"
          tokenChain: "button primary intent -> --ion-lit-color-leonardo-base-primary (#007de0)"
          appliesToCssProperty: "background-color"
      secondary:
        light:
          resolvesTo: "#030f26"
          tokenChain: "button secondary intent -> --ion-lit-color-leonardo-base-secondary (#030f26)"
          appliesToCssProperty: "background-color"
      negative:
        light:
          resolvesTo: "#c70000"
          tokenChain: "button negative intent -> --ion-lit-color-leonardo-base-negative (#c70000)"
          appliesToCssProperty: "background-color"
      positive:
        light:
          resolvesTo: "#2dc168"
          tokenChain: "button positive intent -> --ion-lit-color-leonardo-base-positive (#2dc168)"
          appliesToCssProperty: "background-color"
      buy:
        light:
          resolvesTo: "#007de0"
          tokenChain: "button buy intent -> --ion-lit-color-leonardo-base-buy (#007de0)"
          appliesToCssProperty: "background-color"
      sell:
        light:
          resolvesTo: "#c70000"
          tokenChain: "button sell intent -> --ion-lit-color-leonardo-base-sell (#c70000)"
          appliesToCssProperty: "background-color"
  - name: dateTimeTenors
    type: "IDateTimeTenor<Date>[]"
    category: content
    required: false
    default: []
    values: []
    designTokens: {}
  - name: hideTenorPanel
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
  - name: confirmOnApply
    type: boolean
    category: behavioral
    required: false
    default: false
    values: []
    designTokens: {}
  - name: datepickerOptions
    type: "IDatePickerOptions"
    category: behavioral
    required: false
    default: "See IDatePickerOptions interface definition"
    values: []
    designTokens: {}
  - name: useDateTimeTags
    type: boolean
    category: behavioral
    required: false
    default: false
    values: []
    designTokens: {}
  - name: preventAutoTagSelection
    type: boolean
    category: behavioral
    required: false
    default: false
    values: []
    designTokens: {}
  - name: hideTagPanel
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
  - name: dateTimeTags
    type: "IDateTimeTenor<Date>[]"
    category: content
    required: false
    default: []
    values: []
    designTokens: {}
  - name: compact
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
  - name: date
    type: "Date | null"
    category: content
    required: false
    default: "no initial value selected"
    values: []
    designTokens: {}
events:
  - name: clearButtonClicked
    payloadType: CustomEvent<void>
    firesWhen: "User clicks the 'Clear' button in the footer when 'confirmOnApply' is true"
    detailAccess: "void, event.detail is undefined"
    bindingSyntax: "(clearButtonClicked)=\"onClearButtonClicked($event)\""
  - name: applyButtonClicked
    payloadType: CustomEvent<void>
    firesWhen: "User clicks the 'Apply' button in the footer when 'confirmOnApply' is true"
    detailAccess: "void, event.detail is undefined"
    bindingSyntax: "(applyButtonClicked)=\"onApplyButtonClicked($event)\""
  - name: dateChanged
    payloadType: "CustomEvent<{ oldValue: Date | null, newValue: Date | null }>"
    firesWhen: "Date value changes - on day selection when 'confirmOnApply' is false AND on both clear and apply button clicks when 'confirmOnApply' is true"
    detailAccess: "event.detail.oldValue (Date | null) and event.detail.newValue (Date | null)"
    bindingSyntax: "(dateChanged)=\"onDateChanged($event)\""
jointTokens:
  - combination: "intent=secondary, emphasis=bold (for tenor buttons)"
    resolvesTo: "#030f26"
    tokenChain: "tenor button background -> --ion-lit-color-leonardo-base-secondary (#030f26)"
    appliesToCssProperty: "background-color"
  - combination: "intent=secondary, emphasis=moderate (for tenor buttons)"
    resolvesTo: "#e9eaeb"
    tokenChain: "tenor button secondary moderate background -> --ion-lit-color-palette-light-navy-200 (#e9eaeb)"
    appliesToCssProperty: "background-color"
propInteractions:
  - "compact overrides size parsing to force 'sm' regardless of input value"
  - "preventAutoTagSelection suppresses automatic tenor selection when date is selected"
  - "hideTenorPanel and hideTagPanel both control tenor panel visibility; hideTenorPanel is the primary hideTagPanel is for backward compatibility"
  - "dateTimeTenors takes precedence over dateTimeTags when both are provided"
  - "datepickerOptions fields provide backward compatibility overrides for main props including dateDisabled dateTooltip transpose hideWeekends hideNavigation numberOfCalendars weekStartsOn initDate minDate maxDate"
  - "confirmOnApply controls whether date selection updates value immediately or waits for explicit apply button click (this only applies when footer is shown)"
  - "date and value props both track selected date; value is the two-way binding model date is backward compatibility read-only prop"
  - "weekStartsOn is clamped to valid range 1, 7 representing Monday through Sunday"
  - "numberOfCalendars is clamped to valid range 1, 3 calendar views"
  - "mode controls calendar visibility; date shows full calendar time hides calendar (shows time only) date-time shows both (though time section is currently empty placeholder)"
  - "tenorIntent applies to all tenor or button tags in the tenor panel"
  - "initDate minDate and maxDate relationships constrain navigation and selection; view month/year automatically adjusted to respect min/max bounds"
  - "locale and monthFormat or weekFormat work together; locale falls back to default when empty or invalid monthFormat and weekFormat transform through Intl.DateTimeFormat"
needsReview:
  - "Time picker functionality is present in HTML template but appears to be incomplete or placeholder; mode equals time and mode equals date-time show empty time div with no implementation found"
  - "Dark theme design tokens not found for tenor intent values; button component intent tokens are theme-invariant (leonardo base colors) in ds_tokens.css but could not independently verify dark theme variants exist"
  - "Tenor button emphasis color values only partially traced; secondary moderate background color traced but bold emphasis combination and other intents not fully documented"
  - "Tenor intent values inverse on-light and on-dark have no design tokens documented - these are special intent types that could not be traced in ds_tokens.css; confirm this is intentional and not an oversight"
  - "Size prop visual tokens not traced for sm or md or lg values; calendar sizing tokens referenced in calendar-ds.css but final resolved pixel values not found in provided token definitions"
  - "Calendar-specific design tokens for day states including today weekend weekday selected disabled in-range are extensively defined in calendar-ds.css as CSS custom properties but token chain resolution to ds_tokens.css values could not be traced"
  - "Mode enum values including date time and date-time not verified against enum definition beyond calendar-utils.ts; confirm these are the only valid values"
  - "Backward compatibility props including datepickerOptions useDateTimeTags preventAutoTagSelection hideTagPanel dateTimeTags compact and date overlap with main props; interaction precedence could use clarification"
  - "Event emission timing for dateChanged when confirmOnApply equals true; verify it emits on both clear AND apply not just apply"
  - "Calendar card component is internal child but has extensive prop interface; interdependencies between parent date-time-picker and child calendar-card not fully documented"
  - "WeekStartsOn 1-based index with 1 equals Monday vs 0-based with 0 equals Sunday; verify this matches user expectations across locales"
---

## Usage Notes

Boolean props on this component must always be passed with an explicit string value — e.g. `disabled="true"` or `[disabled]="isDisabled"` — never as bare attribute presence (e.g. `disabled` alone, with no value). Bare attribute presence is a native HTML convention this component does NOT support; it will not be interpreted as true.

## size

Controls the overall size of the date-time picker component, affecting the dimensions of calendar cells, labels, and spacing. Supports MQ design strings for responsive sizing.

**Visual cues:**
- md: Medium size (default), standard dimensions for desktop interfaces
- sm: Small size, more compact for space-constrained layouts
- lg: Large size, expanded dimensions for touch interfaces or prominent displays
- MQ strings like "xs=sm;md=md;lg=lg" for different sizes at different breakpoints

**When to use:**
- md: Standard applications, general-purpose date selection (default)
- sm: Compact toolbars, modals, or panels with space constraints
- lg: Touch-first interfaces, accessibility-focused applications
- MQ strings: Responsive interfaces that need different sizes at different screen widths

## disabled

Controls whether the entire date-time picker is disabled and non-interactive.

**Visual cues:**
- When true: Component appears grayed out, all calendar cells, buttons, and inputs are non-interactive
- Calendar navigation buttons appear disabled
- Calendar cells and tenor buttons cannot be selected
- Clear and apply buttons (when shown) are disabled

**When to use:**
- Set true when date selection is temporarily unavailable
- Use when form validation or business rules prevent date changes
- Override default false when application state requires disabling

## transpose

Controls the calendar layout orientation in multi-calendar scenarios.

**Visual cues:**
- When false (default): Multiple calendars stack vertically (side-by-side with vertical week labels)
- When true: Calendars stack horizontally (above/below with horizontal day labels), single week label bar shared across all calendars

**When to use:**
- false: Standard vertical calendar layout for most applications
- true: Horizontal layout when vertical space is constrained or for specific design requirements
- Particularly relevant when numberOfCalendars > 1

## disableWeekends

Controls whether weekend days (Saturday and Sunday) are disabled and non-selectable.

**Visual cues:**
- When true: Weekend calendar cells appear disabled with gray/semi-transparent styling
- Weekend cells cannot be selected or hovered
- Applies to all Saturdays and Sundays across all calendar views

**When to use:**
- Set true for business applications that only allow weekday selection
- Use when weekends are not meaningful for the date selection context
- Override default false when business logic restricts weekend dates

## enableDropdowns

Controls whether month and year dropdown selectors are shown in the calendar header.

**Visual cues:**
- When true: Dropdown selectors appear for changing month and year
- When false: Only navigation arrow buttons are available for month/year changes

**When to use:**
- Set true to allow direct month/year selection via dropdowns
- Keep false for cleaner, more minimal interface when navigation buttons suffice
- Useful when rapid navigation between distant months/years is needed

## hideNavigation

Controls whether the calendar navigation controls (previous/next buttons) are hidden.

**Visual cues:**
- When true: Previous and next navigation buttons are hidden
- When false: Navigation buttons appear above calendar for month-by-month navigation

**When to use:**
- Set true for static calendar displays without navigation needs
- Use when month/year selection is handled externally (e.g., via enableDropdowns)
- Override default false when navigation should be restricted

## fixedWeekRows

Controls whether the calendar always shows a fixed number of week rows regardless of month length.

**Visual cues:**
- When true: Calendar always shows exactly 42 day cells (6 weeks × 7 days), even for months with fewer weeks
- When false: Calendar height varies by month (4-5 weeks for shorter months)
- Prevents calendar resizing when navigating between months

**When to use:**
- Set true when you need consistent calendar dimensions across months
- Useful for modal dialogs or panels where size changes would cause layout shifts
- Keep false for more compact displays when space is at a premium

## locale

Controls the language/region for formatting month and week labels. Falls back to application default when empty or invalid.

**Visual cues:**
- Affects month labels (e.g., "January" vs "janvier" vs "1月")
- Affects week labels (e.g., "Mon" vs "Lun" vs "月")
- When empty: Uses application language service locale setting

**When to use:**
- Override app default when calendar should use specific locale
- Set to BCP 47 language tags like "en-US", "fr-FR", "ja-JP", "de-DE"
- Use empty string to defer to application-level language setting
- Useful for multi-language applications or locale-specific date formats

## monthFormat

Controls the format of month labels displayed in calendar headers.

**Visual cues:**
- long: Full month name (e.g., "January", "February") - default
- short: Abbreviated month name (e.g., "Jan", "Feb")
- numeric: Numeric month (e.g., "1", "2")
- narrow: Single character abbreviation (e.g., "J", "F")
- 2-digit: Two-digit numeric month (e.g., "01", "12")

**When to use:**
- long: Standard applications with sufficient space (default)
- short: Compact headers where full names are too long
- numeric: Very compact headers or for international consistency
- narrow: Extremely space-constrained interfaces

## weekFormat

Controls the format of day-of-week labels displayed in calendar headers.

**Visual cues:**
- short: Abbreviated day names (e.g., "Mon", "Tue") - default for medium/large sizes
- narrow: Single character abbreviations (e.g., "M", "T") - used for small size
- long: Full day names (e.g., "Monday", "Tuesday")

**When to use:**
- short: Standard compact day labels (default)
- narrow: Very space-constrained layouts or small calendar sizes
- long: Full day labels when space allows and clarity is needed

## numberOfCalendars

Controls how many consecutive month calendars are displayed simultaneously.

**Visual cues:**
- 1: Single month calendar (default)
- 2: Two consecutive months shown side-by-side
- 3: Three consecutive months shown side-by-side
- Clamped to range [1, 3]; values outside this range are automatically adjusted

**When to use:**
- 1: Standard single-month selection (default)
- 2-3: Range selection or multi-month comparisons
- Useful when comparing dates across months or selecting date ranges

## weekStartsOn

Controls which day of the week the calendar starts with (1 = Monday, 7 = Sunday).

**Visual cues:**
- 1: Monday first (default)
- 6: Saturday first
- 7: Sunday first
- Affects the order of day labels and column arrangement

**When to use:**
- 1: Standard business/ISO week (default)
- 7: Sunday-first weeks for US/consumer applications
- Other values for locale-specific week starts
- Clamped to range [1, 7] for valid weekday indices

## initDate

Controls which date the calendar initially opens to when first displayed.

**Visual cues:**
- Calendar opens to the month/year of initDate
- Does not make that date selected; only affects initial navigation
- Falls back to current date (Temporal.Now.plainDateISO) if not specified

**When to use:**
- Set to relevant business date (e.g., start of fiscal quarter, upcoming deadline)
- Use when defaulting to current date doesn't make sense for the context
- Useful for modal dialogs that should open to a specific month

## value

Controls the selected date value in a two-way binding.

**Visual cues:**
- Selected date is highlighted with specific styling (color, border)
- Calendar navigates to the month/year of selected date on init
- When null: No date is selected and highlighted

**When to use:**
- Bind to form field data model for controlled date selection
- Initialize with pre-selected date from backend data
- Set to null to clear selection
- Primary two-way binding prop for the component

## minDate

Controls the earliest selectable date in the calendar.

**Visual cues:**
- Dates before minDate appear disabled with gray styling
- Cannot select or navigate to months before minDate
- Calendar navigation buttons disable when at minDate boundary

**When to use:**
- Set earliest valid date for booking/reservation systems
- Use for historical date constraints (e.g., date of birth)
- Useful in business scenarios with validity periods
- Works with maxDate to define valid date range

## maxDate

Controls the latest selectable date in the calendar.

**Visual cues:**
- Dates after maxDate appear disabled with gray styling
- Cannot select or navigate to months after maxDate
- Calendar navigation buttons disable when at maxDate boundary

**When to use:**
- Set latest valid date for booking/expiry systems
- Use for transaction date constraints
- Useful for future date limitations
- Works with minDate to define valid date range

## dateDisabled

Custom function that determines whether individual dates should be disabled.

**Visual cues:**
- Dates that return true appear disabled with special styling
- Disabled dates cannot be selected
- Overrides minDate/maxDate and disableWeekends for specific dates

**When to use:**
- Disable holidays, weekends (custom patterns), or business-specific dates
- Block dates that are already booked/unavailable
- Use for complex date logic beyond simple ranges
- Function receives date as Date object and returns boolean

## dateTooltip

Custom function that provides tooltip content for individual calendar days.

**Visual cues:**
- Hovering over a date shows tooltip with custom content
- Returns either string or IonElement (custom DOM structure)
- Empty string returns no tooltip

**When to use:**
- Show additional context for specific dates (holidays, events)
- Display custom formatted dates or business information
- Use IonElement for rich tooltips with custom styling
- Useful for highlighting special dates in calendar

## mode

Controls which date/time selection modes are shown.

**Visual cues:**
- date: Shows full calendar with date selection only
- time: Shows time picker only (calendar hidden) - currently empty placeholder
- date-time: Shows both calendar and time picker - time section currently incomplete
- Determines whether calendar widget is rendered in template

**When to use:**
- date: Most common case for date-only selection (default)
- time: Time-only selection (when implemented)
- date-time: Combined date and time selection (when time picker complete)
- Note: Time picker functionality is currently incomplete in source code

## tenorIntent

Controls the visual intent/color scheme of tenor buttons in the side panel.

**Visual cues:**
- primary: Blue (#007de0) primary action buttons
- secondary: Dark navy (#030f26) secondary buttons (default)
- negative: Red (#c70000) destructive action buttons
- positive: Green (#2dc168) success/confirm action buttons
- buy: Blue (#007de0) trading buy action buttons
- sell: Red (#c70000) trading sell action buttons
- Applies to all tenor buttons when showing preset date shortcuts

**When to use:**
- secondary: Most common for neutral date shortcuts (default)
- primary/buy: Highlight recommended or default date options
- negative/sell: Warn about special or cautionary dates
- positive: Indicate favorable or confirmed dates
- Use different intents to semantically color-code date options

## dateTimeTenors

Array of date shortcuts/tenors displayed as selectable buttons in the side panel.

**Visual cues:**
- Displays vertical list of buttons with tenor names and associated dates
- Selected tenor is highlighted with bold emphasis
- Tenor buttons use tenorIntent for color scheme
- Hidden when array is empty or when hideTenorPanel is true

**When to use:**
- Provide quick access to common date scenarios (Today, Tomorrow, +1 Week)
- Show business-specific date shortcuts (Trade dates, Reporting dates)
- Use for preset date ranges or recurring dates
- Each tenor should have name (string) and date (Date) properties

## hideTenorPanel

Controls whether the tenor/date shortcuts panel is hidden.

**Visual cues:**
- When true: Side panel with date shortcuts is completely hidden
- When false: Tenor panel shows on the left side of calendar
- Affects overall component width and layout

**When to use:**
- Set true when date shortcuts aren't needed
- Use false to provide convenient date presets (default behavior)
- Useful for space-constrained interfaces or when tenors are controlled externally

## confirmOnApply

Controls whether date selection requires explicit confirmation via apply button.

**Visual cues:**
- When true: Shows footer with Clear and Apply buttons; date changes don't update value immediately
- When false: Date selection immediately updates value; no footer shown
- Applies to both calendar day selection and tenor button selection

**When to use:**
- Set true for dialogs where user should review selection before confirming
- Use false for direct, immediate date selection (default)
- Useful for workflows requiring explicit confirmation step
- Can prevent accidental date changes by requiring intentional apply

## datepickerOptions

Legacy backward compatibility object that provides alternative interface for many main props.

**Visual cues:**
- Properties in this object override corresponding main props
- Supports legacy prop names like transposeDayCalendar, hideWeekends
- Used for existing code that expects older API format

**When to use:**
- Only for backward compatibility with existing code
- New implementations should use main props directly
- Provides migration path from old API
- Contains nested options like dateDisabled callback and dateTooltip callback

## useDateTimeTags

Legacy backward compatibility flag for tenor functionality.

**Visual cues:**
- When true: Enables tenor/tag functionality using dateTimeTags array
- When false: Tenors disabled unless dateTimeTenors array provided
- Works with preventAutoTagSelection and hideTagPanel props

**When to use:**
- Only for backward compatibility with legacy code
- New code should use dateTimeTenors directly
- Part of old API that has been superceded
- Use when maintaining compatibility with older component versions

## preventAutoTagSelection

Controls whether selecting a date automatically selects associated tenors/tags.

**Visual cues:**
- When true: Date selection does not auto-select matching tenor buttons
- When false: Date selection automatically highlights matching tenors (default behavior)
- Affects tenor panel highlighting when dates are selected via calendar

**When to use:**
- Set true when tenor selection should be manual/independent
- Use false for convenience (date selection auto-selects matching tenors)
- Useful when multiple tenors might share the same date
- Prevents unexpected tenor selection on date changes

## hideTagPanel

Legacy alias for hideTenorPanel.

**Visual cues:**
- Provides same functionality as hideTenorPanel
- Used for backward compatibility with older component versions
- When both provided, hideTenorPanel takes precedence

**When to use:**
- Only for backward compatibility with legacy code
- New implementations should use hideTenorPanel
- Dual naming maintains API compatibility
- Modern code should prefer hideTenorPanel

## dateTimeTags

Legacy backward compatibility alternative to dateTimeTenors array.

**Visual cues:**
- Same visual behavior as dateTimeTenors
- Used when useDateTimeTags is true
- Provides same tenor/button shortcut functionality

**When to use:**
- Only for maintaining backward compatibility
- New code should use dateTimeTenors array
- Supports legacy code that uses dateTimeTags property
- Works with useDateTimeTags flag for enable/disable control

## compact

Controls whether the component uses compact sizing mode.

**Visual cues:**
- When true: Forces component to small (sm) size regardless of size prop value
- When false: Uses the size prop value normally
- Overrides size parsing to apply compact dimensions

**When to use:**
- Set true for compact interfaces where small size is always needed
- Use false when size prop should be respected
- Useful for responsive designs with size constraints
- More direct than setting size="sm" when compactness is a design feature

## date

Legacy read-only prop that tracks the selected date.

**Visual cues:**
- Functions like value prop but for read-only access
- Provides same selected date information
- Color-coded highlight on the selected day in calendar

**When to use:**
- Only for backward compatibility with existing code
- New implementations should use value prop for two-way binding
- Provides migration path from component's earlier API design
- Maintains compatibility for code expecting date prop

## Events

### clearButtonClicked

This event fires when the user clicks the "Clear" button in the footer when `confirmOnApply` is true. It signifies that the user wants to clear the current date selection.

**Emitted args:** `CustomEvent<void>`

**When to use:**
- Respond to user clearing the date selection
- Reset form validation state or related fields
- Update UI to reflect cleared selection state

**How to use:**
```typescript
onClearButtonClicked(event: CustomEvent<void>): void {
  console.log('Clear button clicked');
  this.selectedDate = null;
  this.dateInput.reset();
}
```

**Binding syntax:**
```html
<ion-date-time-picker (clearButtonClicked)="onClearButtonClicked($event)"></ion-date-time-picker>
```

### applyButtonClicked

This event fires when the user clicks the "Apply" button in the footer when `confirmOnApply` is true. It signifies that the user has reviewed and confirmed the selected date.

**Emitted args:** `CustomEvent<void>`

**When to use:**
- Respond to user confirming the date selection
- Trigger form validation or submission
- Update backend or state with confirmed date

**How to use:**
```typescript
onApplyButtonClicked(event: CustomEvent<void>): void {
  console.log('Apply button clicked');
  this.confirmDateSelection();
  this.dateInput.closeCalendar();
}
```

**Binding syntax:**
```html
<ion-date-time-picker (applyButtonClicked)="onApplyButtonClicked($event)"></ion-date-time-picker>
```

### dateChanged

This event fires when the date value changes. The timing depends on `confirmOnApply`: when false, it fires immediately on day/tenor selection; when true, it fires only on Clear/Apply button clicks. Always fires with both old and new values for tracking changes.

**Emitted args:** `CustomEvent<{ oldValue: Date | null, newValue: Date | null }>`

**When to use:**
- Track date changes in forms or state management
- Implement side effects when user changes the selected date
- Validate date selection against business rules
- Update dependent form fields based on date changes

**How to use:**
```typescript
onDateChanged(event: CustomEvent<{ oldValue: Date | null, newValue: Date | null }>): void {
  const { oldValue, newValue } = event.detail;
  console.log(`Date changed from ${oldValue?.toDateString()} to ${newValue?.toDateString()}`);
  
  if (newValue) {
    this.validateDate(newValue);
    this.updateRelatedFields(newValue);
  }
}
```

**Binding syntax:**
```html
<ion-date-time-picker (dateChanged)="onDateChanged($event)"></ion-date-time-picker>
```

### Complete event binding example

```html
<ion-date-time-picker 
  [value]="selectedDate"
  [confirmOnApply]="true"
  (dateChanged)="onDateChanged($event)"
  (clearButtonClicked)="onClearButtonClicked($event)"
  (applyButtonClicked)="onApplyButtonClicked($event)">
</ion-date-time-picker>
```

```typescript
// Combined handler implementation
onDateChanged(event: CustomEvent<{ oldValue: Date | null, newValue: Date | null }>): void {
  const { oldValue, newValue } = event.detail;
  console.log('Date changed:', { oldValue, newValue });
}

onClearButtonClicked(event: CustomEvent<void>): void {
  console.log('Selection cleared');
  this.selectedDate = null;
  this.resetRelatedValidation();
}

onApplyButtonClicked(event: CustomEvent<void>): void {
  console.log('Selection confirmed');
  if (this.selectedDate) {
    this.submitDate(this.selectedDate);
  }
}
```

## Examples

```html
<ion-date-time-picker
  size="md"
  mode="date"
  [minDate]="minDate"
  [maxDate]="maxDate"
  [value]="selectedDate">
</ion-date-time-picker>
```
Demonstrates basic date-only picker with size control, date range constraints, and two-way value binding.

```html
<ion-date-time-picker
  size="sm"
  mode="date"
  [disableWeekends]="true"
  [numberOfCalendars]="2"
  [transpose]="true"
  [value]="selectedDate">
</ion-date-time-picker>
```
Demonstrates compact multi-calendar picker with weekends disabled and horizontal (transposed) layout.

```html
<ion-date-time-picker
  [confirmOnApply]="true"
  [value]="selectedDate"
  (dateChanged)="onDateChanged($event)"
  (clearButtonClicked)="onClearButtonClicked($event)"
  (applyButtonClicked)="onApplyButtonClicked($event)">
</ion-date-time-picker>
```
Demonstrates apply/cancel workflow with explicit confirmation and all event handlers wired up.

```html
<ion-date-time-picker
  mode="date"
  [dateTimeTenors]="dateTimeTenors"
  [hideTenorPanel]="false"
  tenorIntent="secondary"
  [value]="selectedDate">
</ion-date-time-picker>
```
Demonstrates tenor/date shortcuts panel with predefined date options for quick selection.

```html
<ion-date-time-picker
  mode="date"
  [locale]="ja-JP"
  [monthFormat]="'long'"
  [weekStartsOn]="1"
  [value]="selectedDate">
</ion-date-time-picker>
```
Demonstrates locale customization with Japanese month labels, Monday start of week, and full month names.

```html
<ion-date-time-picker
  mode="date"
  [dateDisabled]="dateDisabled"
  [dateTooltip]="dateTooltip"
  [fixedWeekRows]="true"
  [enableDropdowns]="true"
  [value]="selectedDate">
</ion-date-time-picker>
```
Demonstrates advanced configuration with custom date disabling logic, tooltips, fixed calendar height, and month/year dropdown selectors.
