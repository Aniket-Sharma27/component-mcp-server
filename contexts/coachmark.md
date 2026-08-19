---
realComponent: ion-coachmark-service
description: Injectable Angular service for creating contextual user guidance through individual coachmarks and multi-step tours with state management
themes: [modern-light-ds, modern-dark-ds]
apiTypes: ["service"]
serviceApi:
  serviceName: CoachMarkService
  importPath: "@ionweb/sdk/experimental/angular"
  methods:
    - name: create
      signature: "create(anchor: HTMLElement | CoachMarkSDKComponents, options: ICoachMarkOptions): ICoachMark | null"
      configInterface:
        - field: size
          type: string union
          required: false
          description: Size of the coachmark
        - field: placement
          type: PopoverPlacement
          required: false
          description: "Placement relative to the anchor element"
        - field: showCaret
          type: boolean
          required: false
          description: Determines if the pointer (caret) is shown
        - field: offset
          type: string
          required: false
          description: Offset distance from the anchor element
        - field: width
          type: string
          required: false
          description: Width of the coachmark
        - field: title
          type: string
          required: false
          description: Title text (Markdown-supported)
        - field: description
          type: string
          required: false
          description: Description text (Markdown-supported)
        - field: closeButton
          type: ICoachMarkCloseButton
          required: false
          description: Configuration for close button visibility and click handler
        - field: primaryButton
          type: ICoachMarkButton
          required: false
          description: Configuration for primary button label, icon, and click handler
        - field: secondaryButton
          type: ICoachMarkButton
          required: false
          description: Configuration for secondary button label, icon, and click handler
        - field: automaticallyOpen
          type: boolean
          required: false
          description: Opens the coachmark automatically after creation (true by default)
      returns: "Returns ICoachMark object with methods open(), close(), destroy() and events onClose (Event<void>), onOpen (Event<void>). Returns null if anchor resolves to invalid element or SDK component not registered."
    - name: createTour
      signature: "createTour(options: ICoachMarkTourOptions, tourId?: string): ICoachMarkTour"
      configInterface:
        - field: size
          type: string union
          required: false
          description: Size of coachmarks in the tour
        - field: placement
          type: PopoverPlacement
          required: false
          description: Default placement for all tour steps
        - field: showCaret
          type: boolean
          required: false
          description: Determines if the pointer is shown for all steps
        - field: offset
          type: string
          required: false
          description: Default offset from anchor elements
        - field: width
          type: string
          required: false
          description: Width of coachmarks in the tour
        - field: closeButton
          type: ICoachMarkCloseButton
          required: false
          description: Close button configuration applied to all steps
        - field: primaryButton
          type: ICoachMarkButton
          required: false
          description: Primary button configuration with onClick handler
        - field: secondaryButton
          type: ICoachMarkButton
          required: false
          description: Secondary button configuration for tour steps
        - field: tourLength
          type: number
          required: true
          description: The number of steps in the tour
        - field: onNextStep
          type: "(step: number) => Promise<{ anchor: HTMLElement | CoachMarkSDKComponents, options: ICoachMarkOptions }>"
          required: false
          description: Callback to provide anchor and step-specific options for each tour step
        - field: setSecondaryButtonAsSkip
          type: boolean
          required: false
          description: Enabling this configures the secondary button as a Skip button that marks the tour as skipped in state management
      returns: "Returns ICoachMarkTour object with methods startTour(startStep?: number): Promise<void>, stopTour(): void, destroy(): void, and event onTourStopped(reason: manual | completed): void"
    - name: registerTour
      signature: "registerTour(tourId: string, options: ICoachMarkTourOptions): void"
      configInterface: []
      returns: "void - registers tour configuration for later execution via startTour()"
    - name: getRegisteredTours
      signature: "getRegisteredTours(): Array<{ id: string, options: ICoachMarkTourOptions }>"
      configInterface: []
      returns: "Array of registered tour objects with id and full options configuration"
    - name: startTour
      signature: "startTour(tourId: string, forceShow: boolean = false): Promise<void>"
      configInterface: []
      returns: "Promise that resolves when tour starts or immediately if already started/completed/skipped. Respects stored tour state unless forceShow is true"
    - name: skipTour
      signature: "skipTour(tourId: string): void"
      configInterface: []
      returns: "void - marks the specified tour as skipped in persistent storage and stops it if currently active"
    - name: register
      signature: "register(SdkComponent: CoachMarkSDKComponents, element: HTMLElement, selector?: string): void"
      configInterface: []
      returns: "void - registers a custom anchor element for SDK-defined component identifiers"
    - name: unRegister
      signature: "unRegister(SdkComponent: CoachMarkSDKComponents): void"
      configInterface: []
      returns: "void - removes registration for SDK component identifier"
  events: []
propInteractions:
  - "setSecondaryButtonAsSkip in tour options overrides secondary button label to localized 'Skip' text and automatically configures state management on click"
  - "onNextStep callback can override any tour-wide options per step, including buttons - step-specific options merge with tour defaults"
  - "Button onClick callbacks receive ICoachMarkButtonClickArgs with step number and handled flag for custom tour progression control"
  - "CoachMarks anchored to CoachMarkSDKComponents require prior registration via register() before they can be created"
  - "Tour state persists across sessions: 'seen' on start, 'completed' on finishing final step, 'skipped' when skip button clicked"
  - "Anchor elements must be visible when create() or open() is called, otherwise coachmark will not display"
  - "The ICoachMarkButtonClickArgs.handled property allows preventing default tour progression when set to true in button callbacks"
needsReview:
  - "No design token data found for coachmark-specific spacing, typography, or color values in provided ds_tokens.css - only generic leonardo base colors available"
  - "Dark theme-specific coachmark styling tokens not independently verified - coachmark caret uses --ion-cont-color-ui-base-layer-inverse which may not have separate dark theme variant"
  - "Design tokens for anchor element highlight ring (inkwell effect) traced from .coachmark-anchor::after but full token chain not resolved to final value"
  - "CoachMark component uses button and counter components internally but their token resolution beyond the coachmark-size mapping not documented"
  - "Missing documentation for exact resolved values of --ion-cont-shadow-focus-outset-base used for anchor element highlight"
  - "No token data found for coachmark max-width or default width values in the design token files"
---

## Usage Notes

This component is service-only and has no template element. There is no `<ion-coachmark>` web component to add to your template. All coachmark creation and management happens through the `CoachMarkService` by injecting it into your component and calling its methods programmatically.

Because this is a direct Angular service API (not a web component), all event handlers are standard typed functions and do NOT require `.detail` access. The `Event<T>` types used by this service are the ionweb Event class, not native CustomEvent, and payloads are passed directly to the handler functions.

## Service API

### create

Creates a single standalone coachmark anchored to a specific DOM element.

**Config interface:**
- `size` (`"sm" | "md" | "lg"`): Controls coachmark dimensions. When "lg", renders internal buttons at size "md" and close button at "sm". Default is "md".
- `placement` (`PopoverPlacement`): Position relative to anchor element. Values include "top", "right", "bottom", "left" with "-start" and "-end" variants for edge alignment. Default is "right".
- `showCaret` (boolean): Shows/hides the pointer arrow that visually connects coachmark to anchor. Default is true.
- `offset` (string): Distance in pixels from the anchor element (e.g., "10px").
- `width` (string): Explicit width for the coachmark container. Accepts valid CSS values like "300px".
- `title` (string): Heading text displayed at top of coachmark. Supports Markdown formatting via `| mdStringToHtml` pipe.
- `description` (string): Main body text of the coachmark. Supports Markdown formatting.
- `closeButton` (ICoachMarkCloseButton): Object with `show` boolean and optional `onClick()` callback function.
- `primaryButton` (ICoachMarkButton): Object with optional `label` string, `icon` object (with `name` and `family`), and `onClick(args: ICoachMarkButtonClickArgs)` callback.
- `secondaryButton` (ICoachMarkButton): Same shape as primaryButton for secondary action configuration.
- `automaticallyOpen` (boolean): If true (default), displays coachmark immediately after creation. Set false to control timing with `open()` call.

**Payload shape:**
The returned `ICoachMark` object provides these members:
- `open()`: `void` - displays the coachmark if anchor is visible
- `close()`: `void` - closes coachmark and releases resources
- `destroy()`: `void` - cleanup without raising onClose event (internal use)
- `onClose`: `Event<void>` - fires when coachmark is closed (direct subscription, NO `.detail` needed)
- `onOpen`: `Event<void>` - fires when coachmark is displayed (direct subscription, NO `.detail` needed)

**When to use:**
- Show a one-time help tip or feature explanation anchored to a specific UI element
- Provide contextual guidance that appears in response to user action or application state
- Create a single-point-in-time highlight without the overhead of a tour

**How to use:**

```typescript
import { Component, ElementRef, ViewChild, Inject } from '@angular/core';
import ionweb from '@ionweb/sdk/experimental';
import { ServiceTokens } from '@ionweb/sdk/experimental/angular';

@Component({ /* ... */ })
export class MyComponent {
    @ViewChild('featureAnchor', { read: ElementRef, static: true })
    featureAnchor: ElementRef;

    constructor(
        @Inject(ServiceTokens['ionweb.coachMarkService'])
        private coachMarkService: ionweb.toolkit.ICoachMarkService
    ) {}

    showCoachMark() {
        const coachMark = this.coachMarkService.create(
            this.featureAnchor.nativeElement,
            {
                title: 'New Feature',
                description: 'This is where you can access the new functionality.',
                size: 'md',
                placement: 'right',
                offset: '10px',
                closeButton: { show: true },
                primaryButton: { label: 'Got it', onClick: () => {
                    coachMark.close();
                }}
            }
        );

        if (coachMark) {
            coachMark.onOpen.add(() => {
                console.log('Coachmark opened');
            });
            coachMark.onClose.add(() => {
                console.log('Coachmark closed');
            });
        }
    }
}
```

### createTour

Creates a multi-step guided tour with coachmarks displayed sequentially at different anchor points.

**Payload shape:**
The returned `ICoachMarkTour` object provides these members:
- `startTour(startStep?: number)`: `Promise<void>` - begins tour from specified step (1-based index) or step 1 if omitted
- `stopTour()`: `void` - stops the tour and closes current coachmark
- `destroy()`: `void` - releases tour resources
- `onTourStopped(reason: "manual" | "completed")`: Callback function invoked when tour stops. NO `.detail` access needed - receives plain strings.

**When to use:**
- Walk users through a sequence of features or UI elements in order
- Provide progressive disclosure of complex functionality
- Build onboarding flows that guide users through key application areas
- Implement tutorial experiences that advance through multiple steps

**How to use:**

```typescript
import { Component, ElementRef, ViewChild, Inject } from '@angular/core';
import ionweb from '@ionweb/sdk/experimental';
import { ServiceTokens } from '@ionweb/sdk/experimental/angular';

@Component({ /* ... */ })
export class MyComponent {
    @ViewChild('step1Anchor', { read: ElementRef, static: true })
    step1: ElementRef;

    @ViewChild('step2Anchor', { read: ElementRef, static: true })
    step2: ElementRef;

    @ViewChild('step3Anchor', { read: ElementRef, static: true })
    step3: ElementRef;

    private tour: ionweb.toolkit.ICoachMarkTour;

    constructor(
        @Inject(ServiceTokens['ionweb.coachMarkService'])
        private coachMarkService: ionweb.toolkit.ICoachMarkService
    ) {}

    async startTour() {
        const tourOptions: ionweb.toolkit.ICoachMarkTourOptions = {
            size: 'md',
            placement: 'right',
            showCaret: true,
            offset: '15px',
            width: '320px',
            closeButton: { show: true },
            primaryButton: { label: 'Next' },
            secondaryButton: { label: 'Skip' },
            tourLength: 3,
            onNextStep: async (step: number) => {
                if (step === 1) {
                    return {
                        anchor: this.step1.nativeElement,
                        options: {
                            title: 'Welcome',
                            description: 'Let\'s explore the main features.',
                        }
                    };
                } else if (step === 2) {
                    return {
                        anchor: this.step2.nativeElement,
                        options: {
                            title: 'Feature 2',
                            description: 'Here\'s where you configure settings.',
                        }
                    };
                } else if (step === 3) {
                    return {
                        anchor: this.step3.nativeElement,
                        options: {
                            title: 'All Done!',
                            description: 'You\'re ready to go.',
                            primaryButton: { label: 'Finish' }
                        }
                    };
                }
                return null;
            }
        };

        this.tour = this.coachMarkService.createTour(tourOptions);
        this.tour.onTourStopped = (reason) => {
            console.log(`Tour stopped: ${reason}`);
        };
        await this.tour.startTour();
    }
}
```

### registerTour

Registers a tour configuration globally with a unique identifier for deferred execution.

**When to use:**
- Define tours at application initialization but trigger them later based on user context
- Enable "New Features" dialogs that can show available tours dynamically
- Separate tour definition from execution across different parts of the application

**How to use:**

```typescript
// In app initialization or a dedicated tour config service
const tourOptions: ionweb.toolkit.ICoachMarkTourOptions = {
    // ... configuration ...
    tourLength: 5,
    setSecondaryButtonAsSkip: true,
    onNextStep: async (step) => { /* ... */ }
};

this.coachMarkService.registerTour('welcome-tour-v1', tourOptions);
```

### getRegisteredTours

Retrieves all tours that have been registered with their IDs and full configurations.

**When to use:**
- Build a "New Features" or "Help" dialog that lists all available tours
- Dynamically create navigation entries for tour management
- Inventory registered tours for debugging or testing purposes

**How to use:**

```typescript
const availableTours = this.coachMarkService.getRegisteredTours();

for (const tour of availableTours) {
    console.log(`Tour: ${tour.id}, Length: ${tour.options.tourLength}`);
}
```

### startTour

Starts a previously registered tour by ID, with optional state override.

**When to use:**
- Trigger pre-configured tours from user actions (clicking "Show me around" button)
- Start tours based on application state or user permissions
- Force tour display for testing or admin purposes

**How to use:**

```typescript
// Respects state - won't show if already completed/skipped
this.coachMarkService.startTour('dashboard-intro-v1');

// Force show regardless of stored state
this.coachMarkService.startTour('dashboard-intro-v1', true);
```

### skipTour

Marks a tour as skipped in persistent storage and stops it if currently running.

**When to use:**
- Provide users with "Skip tour forever" option in preferences
- Programatically skip tours based on user attributes or permissions
- Clean up tour state that should no longer be shown

**How to use:**

```typescript
this.coachMarkService.skipTour('onboarding-tour');
```

### register

Associates a real DOM element with a `CoachMarkSDKComponents` enum value for later reference.

**When to use:**
- Enable coachmark targeting of SDK-internal components that don't have stable selectors
- Provide stable anchor references for components that may be rendered dynamically
- Support pre-defined SDK component locations in the application

**How to use:**

```typescript
const advancedFilterButton = document.querySelector('.advanced-filter-trigger');

this.coachMarkService.register(
    ionweb.toolkit.CoachMarkSDKComponents.AdvanceFilterPanelGroupButton,
    advancedFilterButton
);
```

### unRegister

Removes the registration for a `CoachMarkSDKComponents` enum value.

**When to use:**
- Clean up registrations when SDK components are no longer available
- Update anchor references when component structure changes
- Prevent stale registrations from causing errors

**How to use:**

```typescript
this.coachMarkService.unRegister(
    ionweb.toolkit.CoachMarkSDKComponents.AdvanceFilterPanelGroupButton
);
```

## When to use which approach

The CoachMark service provides two primary patterns for creating guided experiences:

**Use `create()` for:**
- Single, one-off coachmarks that explain specific features in context
- Just-in-time help that appears in response to user actions or application state
- Situational guidance tied to particular workflows or interactions
- Coachmarks anchored to elements you have direct references to via ViewChild or selectors

**Use `createTour()` for:**
- Sequential, multi-step onboarding experiences that walk users through a feature
- Progressive disclosure tours that introduce multiple UI elements in order
- Tours with dynamic anchors where elements may not exist at initialization time
- Experiences that require state coordination across multiple steps and buttons

**Use `registerTour()` + `startTour()` for:**
- Tours that should be referenced from multiple locations in the application
- Tours with persistent state management (seen/completed/skipped across sessions)
- "New Features" or "Help" dialogs that list available tours
- Tours defined separately from when they're triggered (e.g., app init vs. user action)

## Examples

```typescript
const coachMark = coachMarkService.create(anchorElement, {
    title: "Welcome to the feature",
    description: "This is where you can find your settings.",
    placement: "right",
    primaryButton: { label: "Got it!", onClick: () => console.log("Acknowledged") }
 });
 coachMark.open();
```
Demonstrates basic single coachmark creation with anchor, content, placement, and button configuration.

```typescript
const tourOptions: ionweb.toolkit.ICoachMarkTourOptions = {
    size: "md",
    placement: "left",
    showCaret: true,
    offset: "20px",
    width: "300px",
    closeButton: { show: true },
    primaryButton: { label: "Next"},
    secondaryButton: { label: "Cancel" },
    tourLength: 5,
    onNextStep: async (step: number) => {
        if (step === 1) return {
            anchor: this.tourButtonAnchor.nativeElement,
            options: { title: "Step 1", description: "This is Step 1" }
        };
        // ... other steps ...
        return null;
    }
};

this.coachMarkTour = this.coachMarkService.createTour(tourOptions);
await this.coachMarkTour.startTour();
```
Demonstrates tour creation with onNextStep callback for dynamic anchor and option provision per step.

```typescript
this.coachMarkService.registerTour('dashboard-tour-v1', {
    setSecondaryButtonAsSkip: true,
    primaryButton: { label: "Next" },
    tourLength: 3,
    onNextStep: async (step) => { /* ... */ }
});

// Later, from user action
this.coachMarkService.startTour('dashboard-tour-v1');
```
Demonstrates tour registration with state management and subsequent launch.

```typescript
coachMarkService.create(anchorElement, {
    automaticallyOpen: false
    // ... other options ...
});

// Later conditionally
coachMark.open();
```
Demonstrates using `automaticallyOpen: false` to control coachmark display timing.

```typescript
this.coachMarkService.register(
    ionweb.toolkit.CoachMarkSDKComponents.GridTemplateSelector,
    templateSelectorElement,
    '.selector-trigger'
);
```
Demonstrates creating coachmarks anchored to SDK-defined components with optional selector refinement.