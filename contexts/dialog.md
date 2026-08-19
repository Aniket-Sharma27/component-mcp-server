---
realComponent: ion-dialog
description: A focused interaction overlay that interrupts the main interface to communicate essential information or request user action, accessible only via the DialogService.showModal() method in the new design system mode.
themes: [modern-light-ds, modern-dark-ds]
apiTypes: ["service"]
serviceApi:
  serviceName: "DialogService"
  importPath: "../public-api/dialogs.i"
  methods:
    - name: "showModal"
      signature: "showModal<T = void>(content: string | IonElement, options?: IModalDialogOptions): IModalDialog<T>"
      configInterface:
        - field: "title"
          type: "string"
          required: false
          description: "Defines the dialog's title text, displayed above the content."
        - field: "intent"
          type: '"neutral" | "negative" | "positive" | "warning" | "info"'
          required: false
          description: "Specifies the semantic meaning and color scheme of the dialog."
        - field: "width"
          type: '"md" | "lg"'
          required: false
          description: "Specifies the width of the dialog. For mobile, width is always constrained to the viewport."
        - field: "height"
          type: "string (in px, vh or %)"
          required: false
          description: "Specifies the height of the dialog."
        - field: "maxHeight"
          type: "string (in px, vh or %)"
          required: false
          description: "Specifies the max height of the dialog."
        - field: "mobilePlacement"
          type: '"full-screen" | "bottom"'
          required: false
          description: "Specifies how the dialog expands in mobile scenarios - full-screen or at the bottom."
        - field: "showIcon"
          type: "boolean"
          required: false
          description: "Specify whether to display the intent icon beside the title."
        - field: "icon"
          type: "string | IIconOptions"
          required: false
          description: "Defines the icon to be displayed beside the title for neutral intent."
        - field: "showCloseButton"
          type: "boolean"
          required: false
          description: "Specify whether to show close icon on the top-right corner of the dialog header."
        - field: "disableEscapeClose"
          type: "boolean"
          required: false
          description: "Specify whether to disable closing of dialog with Esc key."
        - field: "closeOnClickOutside"
          type: "boolean"
          required: false
          description: "Close the dialog when the user clicks outside the modal content area."
        - field: "headerIcons"
          type: "IDialogButtonOptions[]"
          required: false
          description: "Defines custom icon-buttons displayed on the right side of the header. Supports up to three buttons."
        - field: "footerStartButton"
          type: "IDialogButtonOptions"
          required: false
          description: "Defines the action button displayed at the far left of the dialog footer."
        - field: "footerEndButtons"
          type: "IDialogButtonOptions[]"
          required: false
          description: "Defines the action buttons displayed at the end of the dialog footer. Supports max up to two buttons."
        - field: "enableCustomSpacing"
          type: "boolean"
          required: false
          description: "Remove the spacing around dialog content. The application is responsible to provide proper spacing."
      returns: "IModalDialog<T> with properties: closed (Promise<T> that resolves when dialog is closed), opened (Promise<void> that resolves when dialog is opened), dismiss() (method to close dialog programmatically), and dialogRef (reference to underlying component)"
    - name: "show"
      signature: "show<T>(opts: IDialogCreateOptions): IDialog<T>"
      configInterface:
        - field: "title"
          type: "string"
          required: false
          description: "The title of the dialog. By default is empty."
        - field: "template"
          type: "string | IonElement"
          required: false
          description: "The body of the HTML template of the dialog content."
        - field: "textContent"
          type: "string"
          required: false
          description: "Specify the content as plain text instead of Angular template."
        - field: "buttons"
          type: "(string | IDialogCreateOptionsButtonDefinition)[]"
          required: false
          description: "Buttons to add at the bottom of the dialog. Each button can be set as primary to be displayed with the accent color."
        - field: "captionButtons"
          type: "IDialogCaptionButton[]"
          required: false
          description: "Buttons to be added in header."
        - field: "severity"
          type: "DialogSeverity"
          required: false
          description: "Get/Set the severity style of the dialog (Info, Warning, Danger, Success, or Neutral)."
        - field: "enableCustomSpacing"
          type: "boolean"
          required: false
          description: "Remove the spacing around dialog content, false by default."
        - field: "canClose"
          type: "boolean"
          required: false
          description: "Should the dialog be closed when you click outside? By default is false."
        - field: "size"
          type: "DialogSize"
          required: false
          description: "Size of the dialog window (Small, Large, Auto, or Fixed)."
        - field: "mobileLayoutMode"
          type: '"fullscreen" | "responsive"'
          required: false
          description: "Layout to be used for mobile screens. By default is fullscreen."
      returns: "IDialog<T> with properties: dismiss() (method to close dialog), closed (Promise<{ value?: T; cancel: boolean }>), result (Promise<T>), and buttonClick (Event<number>)"
    - name: "showCustom"
      signature: "showCustom<T>(opts: ICustomDialogCreateOptions): IDialog<T>"
      configInterface:
        - field: "template"
          type: "string | IonElement"
          required: false
          description: "The body of the HTML template of the dialog content."
        - field: "textContent"
          type: "string"
          required: false
          description: "Specify the content as plain text instead of Angular template."
        - field: "captionButtons"
          type: "IDialogCaptionButton[]"
          required: false
          description: "Buttons to be added in header."
        - field: "canClose"
          type: "boolean"
          required: false
          description: "Should the dialog be closed when you click outside? By default is false."
        - field: "size"
          type: "DialogSize"
          required: false
          description: "Size of the dialog window (Small, Large, Auto, or Fixed)."
        - field: "mobileLayoutMode"
          type: '"fullscreen" | "responsive"'
          required: false
          description: "Layout to be used for mobile screens. By default is fullscreen."
        - field: "enforceDSDialog"
          type: "boolean"
          required: false
          description: "API to enforce use of DS Dialog."
      returns: "IDialog<T> with properties: dismiss() (method to close dialog), closed (Promise<{ value?: T; cancel: boolean }>), result (Promise<T>), and buttonClick (Event<number>)"
    - name: "showConfirmationDialog"
      signature: "showConfirmationDialog(content: string | ISimpleDialogCreateOptions, title?: string, okText?: string): IDialog<void>"
      configInterface:
        - field: "content"
          type: "string | ISimpleDialogCreateOptions"
          required: true
          description: "The content to be rendered inside the dialog - either a string (rendered as standard dialog text) or an ISimpleDialogCreateOptions instance."
        - field: "title"
          type: "string"
          required: false
          description: "Dialog title."
        - field: "okText"
          type: "string"
          required: false
          description: "Text to display in the button - defaults to Ok."
      returns: "IDialog<void> with properties: dismiss() (method to close dialog), closed (Promise<{ value?: void; cancel: boolean }>), result (Promise<void>), and buttonClick (Event<number>). The closed promise resolves once the button is clicked."
    - name: "showQuestionDialog"
      signature: "showQuestionDialog(content: string | ISimpleDialogCreateOptions, title?: string, positiveText?: string, negativeText?: string): IDialog<DialogResult>"
      configInterface:
        - field: "content"
          type: "string | ISimpleDialogCreateOptions"
          required: true
          description: "The content to be rendered inside the dialog - either a string (rendered as standard dialog text) or an ISimpleDialogCreateOptions instance."
        - field: "title"
          type: "string"
          required: false
          description: "Dialog title."
        - field: "positiveText"
          type: "string"
          required: false
          description: "Text to display in the positive button - defaults to Ok."
        - field: "negativeText"
          type: "string"
          required: false
          description: "Text to display in the negative button - defaults to Cancel."
      returns: "IDialog<DialogResult> with properties: dismiss() (method to close dialog), closed (Promise<{ value?: DialogResult; cancel: boolean }>), result (Promise<DialogResult>), and buttonClick (Event<number>). The result promise resolves with DialogResult.Ok (0) for positive button clicked and DialogResult.Cancel (1) for negative button clicked."
    - name: "showOptionDialog"
      signature: "showOptionDialog(content: string | ISimpleDialogCreateOptions, buttons: (string | IDialogCreateOptionsButtonDefinition)[], title?: string): IDialog<number>"
      configInterface:
        - field: "content"
          type: "string | ISimpleDialogCreateOptions"
          required: true
          description: "The content to be rendered inside the dialog - either a string (rendered as standard dialog text) or an ISimpleDialogCreateOptions instance."
        - field: "buttons"
          type: "(string | IDialogCreateOptionsButtonDefinition)[]"
          required: true
          description: "Array of strings or definition to use as button titles. If text is used, the buttons will be rendered as primary."
        - field: "title"
          type: "string"
          required: false
          description: "Dialog title."
      returns: "IDialog<number> with properties: dismiss() (method to close dialog), closed (Promise<{ value?: number; cancel: boolean }>), result (Promise<number>), and buttonClick (Event<number>).The result promise resolves with the index of the clicked button as result."
    - name: "showTopLevelWindow"
      signature: "showTopLevelWindow(opts: ITopLevelWindowOptions): IDialog<void>"
      configInterface:
        - field: "template"
          type: "string | IonElement"
          required: false
          description: "The body of the HTML template of the window content."
        - field: "size"
          type: "DialogSize"
          required: false
          description: "Size of the window (Small, Large, Auto, or Fixed)."
        - field: "position"
          type: "IDialogPosition"
          required: false
          description: "The initial position of the dialog - an object with left and top properties in pixels."
        - field: "openNewWindow"
          type: "boolean"
          required: false
          description: "If true opens the dialog in a child browser window."
        - field: "autoFitVertically"
          type: "boolean"
          required: false
          description: "Open the top level child window in auto-fit mode - the window is automatically resized based on the content."
        - field: "resizable"
          type: "boolean"
          required: false
          description: "Enable window resizing, false by default."
        - field: "escToClose"
          type: "boolean"
          required: false
          description: "Should the top-level dialog close when the Esc key is pressed? Default is false."
      returns: "IDialog<void> with properties: dismiss() (method to close dialog), closed (Promise<{ value?: void; cancel: boolean }>), result (Promise<void>), buttonClick (Event<number>), ready (Promise<IChildWindow>), show(), hide(), and bringToFront() (method only for non-modal dialogs)"
    - name: "showTopLevelDialog"
      signature: "showTopLevelDialog<T>(opts: ITopLevelDialogOptions): IDialog<T>"
      configInterface:
        - field: "title"
          type: "string"
          required: false
          description: "The title of the dialog. By default is empty."
        - field: "template"
          type: "string | IonElement"
          required: false
          description: "The body of the HTML template of the dialog content."
        - field: "buttons"
          type: "(string | IDialogCreateOptionsButtonDefinition)[]"
          required: false
          description: "Buttons to add at the bottom of the dialog. Each button can be set as primary to be displayed with the accent color."
        - field: "captionButtons"
          type: "IDialogCaptionButton[]"
          required: false
          description: "Buttons to be added in header."
        - field: "canClose"
          type: "boolean"
          required: false
          description: "Should the standard X button to be rendered in the caption? By default is false."
        - field: "severity"
          type: "DialogSeverity"
          required: false
          description: "Get/Set the severity style of the dialog (Info, Warning, Danger, Success, or Neutral)."
        - field: "dialogClassID"
          type: "string"
          required: false
          description: "Class ID of dialog used for cascading."
        - field: "size"
          type: "DialogSize"
          required: false
          description: "Size of the dialog window (Small, Large, Auto, or Fixed)."
        - field: "position"
          type: "IDialogPosition"
          required: false
          description: "The initial position of the dialog - an object with left and top properties in pixels."
        - field: "openNewWindow"
          type: "boolean"
          required: false
          description: "If true opens the dialog in a child browser window."
        - field: "autoFitVertically"
          type: "boolean"
          required: false
          description: "Open the top level child window in auto-fit mode - the window is automatically resized based on the content."
        - field: "resizable"
          type: "boolean"
          required: false
          description: "Enable window resizing, false by default."
        - field: "escToClose"
          type: "boolean"
          required: false
          description: "Should the top-level dialog close when the Esc key is pressed? Default is false."
      returns: "IDialog<T> with properties: dismiss() (method to close dialog), closed (Promise<{ value?: T; cancel: boolean }>), result (Promise<T>), buttonClick (Event<number>), show(), hide(), and bringToFront() (method only for non-modal dialogs)"
jointTokens:
  - combination: "intent=neutral"
    resolvesTo: "#030f26"
    tokenChain: "dialog card icon color -> --ion-comp-dialog-card-icon-color-fg-neutral -> --ion-cont-color-text-icon-base-bold -> --ion-lit-color-leonardo-base-neutral (#030f26)"
    appliesToCssProperty: "color"
  - combination: "intent=negative"
    resolvesTo: "#c70000"
    tokenChain: "dialog card icon color -> --ion-comp-dialog-card-icon-color-fg-negative -> --ion-cont-color-text-icon-status-negative -> --ion-lit-color-leonardo-base-negative (#c70000)"
    appliesToCssProperty: "color"
  - combination: "intent=positive"
    resolvesTo: "#2dc168"
    tokenChain: "dialog card icon color -> --ion-comp-dialog-card-icon-color-fg-positive -> --ion-cont-color-text-icon-status-positive -> --ion-lit-color-leonardo-base-positive (#2dc168)"
    appliesToCssProperty: "color"
  - combination: "intent=warning"
    resolvesTo: "#fe7f2a"
    tokenChain: "dialog card icon color -> --ion-comp-dialog-card-icon-color-fg-warning -> --ion-cont-color-text-icon-status-warning -> --ion-lit-color-leonardo-base-warning (#fe7f2a)"
    appliesToCssProperty: "color"
  - combination: "intent=info"
    resolvesTo: "#007de0"
    tokenChain: "dialog card icon color -> --ion-comp-dialog-card-icon-color-fg-info -> --ion-cont-color-text-icon-status-info -> --ion-lit-color-leonardo-base-info (#007de0)"
    appliesToCssProperty: "color"
  - combination: "width=md"
    resolvesTo: "var(--ion-cont-layout-grid-column-static-span-7)"
    tokenChain: "dialog card sizing max width -> --ion-comp-dialog-card-sizing-max-width-md"
    appliesToCssProperty: "max-width"
  - combination: "width=lg"
    resolvesTo: "var(--ion-cont-layout-grid-column-static-span-12)"
    tokenChain: "dialog card sizing max width -> --ion-comp-dialog-card-sizing-max-width-lg"
    appliesToCssProperty: "max-width"
propInteractions:
  - "When both height and maxHeight are set, height takes precedence and overrides maxHeight with a console warning"
  - "showIcon prop interacts with intent: when intent is 'neutral', icon is only shown if showIcon=true AND an icon is provided; for all other intents, icon is shown if showIcon=true regardless of whether a custom icon is provided"
  - "Dialog footerStartButton intent is forced to 'secondary' or 'negative' - other intents are not supported"
  - "Dialog footerEndButtons intent mapping: single button defaults to 'primary', two buttons have first as 'secondary' and second as 'primary'"
  - "mobilePlacement='bottom' results in bottom sheet style on mobile, while 'full-screen' takes full viewport"
  - "When closeOnClickOutside is true, clicking the dialog backdrop (but not its content) closes the dialog; clicking dialog content does not trigger close"
  - "disableEscapeClose and closeOnClickOutside work independently - you can disable one but allow the other"
  - "headerIcons only supports up to 3 icons; extras are silently ignored with a console warning"
  - "footerEndButtons only supports up to 2 buttons; extras beyond the first two are silently ignored"
needsReview:
  - "No dark theme token traces found for dialog intent icon colors - light theme values were traced but dark theme tokens could not be independently verified in the provided token files"
  - "Dialog card background and border color tokens (--ion-comp-dialog-card-color-bg and --ion-comp-dialog-card-color-border) not fully traced to resolved hex values; only traced to container-level base layer tokens"
  - "Dialog shadow token (--ion-comp-dialog-card-shadow) not traced to final resolved value; only referenced at component level"
  - "Dialog content typography tokens (title, body, body-mobile) not traced to resolved font-size, font-weight values; only traced to typography composite tokens"
  - "Dialog spacing tokens (header, main, footer padding and gaps) traced to container-level spacing tokens but not resolved to final pixel values"
  - "Border radius and width tokens traced to modal-ui container tokens but not resolved to final pixel values"
  - "Custom icon options for neutral intent not fully traced - only default intent mapping documented"
  - "Footer button intent mapping only documented for default behavior - custom intent configurations may exist but were not traceable"
  - "Icon component size and behavior within dialog not fully documented in the token level analysis"
  - "show, showCustom, showConfirmationDialog, showQuestionDialog, showOptionDialog, showTopLevelWindow, and showTopLevelDialog methods are legacy APIs from index-2.md - while supported in the new mode, their design system-specific token mapping behavior needs verification"
  - "Severity enumeration (Info, Warning, Danger, Success, Neutral) for legacy methods not fully traced to Design System intent values - mapping appears to exist but token resolution not verified"
  - "Dialog size enumeration (Small, Large, Auto, Fixed) for legacy methods not fully traced to Design System width values - mapping exists but token resolution not verified"
  - "Mobile layout mode (fullscreen vs responsive) for legacy methods not fully traced to Design System mobilePlacement values - mapping exists but exact token mapping not verified"
  - "Button role property (primary, secondary, none) for legacy methods not fully traced to Design System intent values - conversion exists but token resolution not verified"
  - "The payload shape for service methods returns plain Promise objects, not CustomEvent-wrapped values - .detail access is NOT needed for service method returns"
---

## Usage Notes

Boolean props on this component must always be passed with an explicit string value — e.g. `showCloseButton="true"` or `[showCloseButton]="isEnabled"` — never as bare attribute presence (e.g. `showCloseButton` alone, with no value). Bare attribute presence is a native HTML convention this component does NOT support; it will not be interpreted as true.

## Service API

### showModal

Creates and displays a modal dialog with the specified content and configuration options. This is the primary method for showing design system dialogs.

**Config interface:**
- title: string - Defines the dialog's title text, displayed above the content
- intent: "neutral" | "negative" | "positive" | "warning" | "info" - Specifies the semantic meaning and color scheme
- width: "md" | "lg" - Controls the width of the dialog (md on desktop, viewport-constrained on mobile)
- height: string - Exact height in px, vh, or % (overrides maxHeight if both set)
- maxHeight: string - Maximum height constraint in px, vh, or %
- mobilePlacement: "full-screen" | "bottom" - How the dialog expands on mobile
- showIcon: boolean - Whether to display the intent icon beside the title
- icon: string | IIconOptions - Custom icon for neutral intent dialogs
- showCloseButton: boolean - Whether to show X icon in the top-right corner
- disableEscapeClose: boolean - Whether to disable Escape key dismissal
- closeOnClickOutside: boolean - Whether clicking backdrop closes the dialog
- headerIcons: IDialogButtonOptions[] - Up to 3 header action icons
- footerStartButton: IDialogButtonOptions - Left-aligned action button
- footerEndButtons: IDialogButtonOptions[] - Up to 2 right-aligned action buttons
- enableCustomSpacing: boolean - Remove default content spacing (application provides spacing)

**Returns:** IModalDialog<T> with:
- closed: Promise<T> - Resolves when dialog is closed with the result value
- opened: Promise<void> - Resolves when dialog is opened and rendered
- dismiss(result?: any): void - Closes the dialog programmatically
- dialogRef: IAngularComponent - Reference to the underlying component instance

**Payload shape:** Service methods return plain typed Promise objects, NOT CustomEvent-wrapped values. You should NOT use .detail access - the Promise resolves directly with the result value.

**When to use:**
- Display modal dialogs for critical user decisions or alerts
- Present forms or complex interactions requiring focused attention
- Show confirmation dialogs with explicit action buttons
- Implement status notifications that require user acknowledgment
- Create dialogs with custom content using IonElement components

**How to use:**

```typescript
import { DialogService } from '../public-api/dialogs.i';
import { TemplateRef, ViewChild } from '@angular/core';

export class MyComponent {
  constructor(private dialogService: DialogService) {}

  showWarningDialog(): void {
    const content = "This action cannot be undone. Are you sure you want to proceed?";

    const options = {
      title: "Confirm Deletion",
      intent: "negative",
      showCloseButton: true,
      width: "md",
      footerEndButtons: [
        {
          label: "Cancel",
          intent: "secondary",
          onClick: () => {
            console.log("User cancelled");
            dialog.dismiss();
          }
        },
        {
          label: "Delete",
          intent: "negative",
          onClick: () => {
            console.log("User confirmed deletion");
          }
        }
      ]
    };

    const dialog = this.dialogService.showModal(content, options);

    dialog.closed.then((result) => {
      console.log(`Dialog closed with result: ${result}`);
    });
  }

  showSuccessDialog(): void {
    const options = {
      title: "Operation Complete",
      intent: "positive",
      showIcon: true,
      width: "lg",
      footerEndButtons: [
        {
          label: "OK",
          intent: "primary",
          onClick: () => {
            console.log("User acknowledged success");
            dialog.dismiss("completed");
          }
        }
      ]
    };

    const dialog = this.dialogService.showModal("Your changes have been saved successfully.", options);

    dialog.closed.then((result) => {
      console.log(`Success dialog closed with result: ${result}`);
    });
  }
}
```

**Complete example with all configuration:**

```typescript
showComplexDialog(): void {
  const options = {
    title: "Review Your Submission",
    intent: "info",
    width: "lg",
    maxHeight: "50vh",
    mobilePlacement: "bottom",
    showIcon: true,
    showCloseButton: true,
    disableEscapeClose: false,
    closeOnClickOutside: false,
    enableCustomSpacing: true,
    headerIcons: [
      {
        icon: "help",
        label: "Help",
        ariaLabel: "Get help with this dialog",
        onClick: () => console.log("Help requested")
      }
    ],
    footerStartButton: {
      label: "Back",
      intent: "secondary",
      onClick: () => {
        console.log("Navigate back");
        dialog.dismiss();
      }
    },
    footerEndButtons: [
      {
        label: "Cancel",
        intent: "secondary",
        onClick: () => {
          console.log("Cancelled");
          dialog.dismiss();
        }
      },
      {
        label: "Submit",
        intent: "primary",
        onClick: () => {
          console.log("Form submitted");
          dialog.dismiss("submitted");
        }
      }
    ]
  };

  const customContent = this.createCustomContentElement();
  const dialog = this.dialogService.showModal(customContent, options);

  dialog.closed.then((result) => {
    console.log(`Complex dialog closed. Result: ${result}`);
  });
}
```

### show

Shows a standard dialog with text or custom content. This is a legacy API that now also supports design system dialogs.

**Config interface:**
- title: string - The title of the dialog. By default is empty
- template: string | IonElement - The body of the HTML template of the dialog content
- textContent: string - Specify the content as plain text instead of Angular template
- buttons: (string | IDialogCreateOptionsButtonDefinition)[] - Buttons to add at the bottom of the dialog
- captionButtons: IDialogCaptionButton[] - Buttons to be added in header
- severity: DialogSeverity - Get/Set the severity (Info, Warning, Danger, Success, or Neutral)
- enableCustomSpacing: boolean - Remove the spacing around dialog content, false by default
- canClose: boolean - Should the dialog be closed when you click outside? By default is false
- size: DialogSize - Size of the dialog window (Small, Large, Auto, or Fixed)
- mobileLayoutMode: "fullscreen" | "responsive" - Layout to be used for mobile screens. By default is fullscreen

**Returns:** IDialog<T> with:
- dismiss(): void - Method to cancel the dialog, causes the closed promise to be resolved with cancel: true
- closed: Promise<{ value?: T; cancel: boolean }> - Promise fulfilled when the dialog is closed. It will never be rejected
- result: Promise<T> - Promise resolved with the button result value; rejected if dialog is canceled
- buttonClick: Event<number> - Event raised when a button is clicked with the button index

**Payload shape:** Legacy API returns Promise<{ value?: T; cancel: boolean }> for closed promise and Promise<T> for result promise. These are plain typed objects, NOT CustomEvent-wrapped values. .detail access is NOT needed for service method returns.

**When to use:**
- Legacy showDialog patterns that need to work with both design system and non-design system modes
- Standard dialogs with title, content, and action buttons
- Situations where you need the button click event and dialog result Promise pattern from the original API
- When you need caption buttons in the dialog header

**How to use:**

```typescript
import { DialogService } from '../public-api/dialogs.i';
import { DialogSeverity, DialogSize } from '../public-api/dialogs.i';

export class MyComponent {
  constructor(private dialogService: DialogService) {}

  showLegacyDialog(): void {
    const options = {
      title: "Warning Dialog",
      severity: DialogSeverity.Warning,
      canClose: true,
      size: DialogSize.Large,
      textContent: "This is a warning message that requires your attention.",
      buttons: [
        {
          title: "Cancel",
          role: "secondary"
        },
        {
          title: "Proceed",
          role: "primary",
          isDefault: true
        }
      ]
    };

    const dialog = this.dialogService.show(options);

    dialog.closed.then((result) => {
      console.log(`Dialog closed. Value: ${result.value}, Cancel: ${result.cancel}`);
    });

    dialog.buttonClick.add((sender, buttonIndex) => {
      console.log(`Button ${buttonIndex} clicked`);
    });
  }
}
```

### showCustom

Shows a completely custom dialog UI with no support for standard title and buttons.

**Config interface:**
- template: string | IonElement - The body of the HTML template of the dialog content
- textContent: string - Specify the content as plain text instead of Angular template
- captionButtons: IDialogCaptionButton[] - Buttons to be added in header
- canClose: boolean - Should the dialog be closed when you click outside? By default is false
- size: DialogSize - Size of the dialog window (Small, Large, Auto, or Fixed)
- mobileLayoutMode: "fullscreen" | "responsive" - Layout to be used for mobile screens. By default is fullscreen
- enforceDSDialog: boolean - API to enforce use of DS Dialog

**Returns:** IDialog<T> with:
- dismiss(): void - Method to cancel the dialog, causes the closed promise to be resolved with cancel: true
- closed: Promise<{ value?: T; cancel: boolean }> - Promise fulfilled when the dialog is closed. It will never be rejected
- result: Promise<T> - Promise resolved with the button result value; rejected if dialog is canceled
- buttonClick: Event<number> - Event raised when a button is clicked with the button index

**Payload shape:** Legacy API returns Promise<{ value?: T; cancel: boolean }> for closed promise. These are plain typed objects, NOT CustomEvent-wrapped values. .detail access is NOT needed for service method returns.

**When to use:**
- When you need complete control over dialog layout without standard structure
- For completely custom dialog interfaces that don't need standard header/footer
- When you want to create dialogs with unique layouts that don't follow the standard pattern

**How to use:**

```typescript
import { DialogService } from '../public-api/dialogs.i';

export class MyComponent {
  constructor(private dialogService: DialogService) {}

  showCustomDialog(): void {
    const customTemplate = `<div class="custom-layout">
      <h2>Custom Content</h2>
      <p>This dialog has custom layout</p>
      <button (click)="handleCustomAction()">Custom Action</button>
    </div>`;

    const options = {
      template: customTemplate,
      canClose: true,
      captionButtons: [
        {
          icon: "settings",
          onClick: () => console.log("Settings clicked"),
          tooltip: "Custom Settings"
        }
      ]
    };

    const dialog = this.dialogService.showCustom(options);
    dialog.closed.then((result) => {
      console.log(`Custom dialog closed. Value: ${result.value}, Cancel: ${result.cancel}`);
    });
  }
}
```

### showConfirmationDialog

Shows a standard non-closeable modal dialog with a single button to display a confirmation message.

**Config interface:**
- content: string | ISimpleDialogCreateOptions - The content to be rendered inside the dialog (required)
- title: string - Dialog title
- okText: string - Text to display in the button - defaults to "Ok"

**Returns:** IDialog<void> with:
- dismiss(): void - Method to cancel the dialog
- closed: Promise<{ value?: void; cancel: boolean }> - Promise resolved once the button is clicked
- result: Promise<void> - Promise resolved when button is clicked
- buttonClick: Event<number> - Event raised when the button is clicked

**Payload shape:** Legacy API returns plain Promise objects, NOT CustomEvent-wrapped values. .detail access is NOT needed for service method returns.

**When to use:**
- Simple confirmation dialogs where user acknowledgment is required
- Informational dialogs that need explicit dismissal
- When you need a minimal dialog with a single confirmation action

**How to use:**

```typescript
import { DialogService } from '../public-api/dialogs.i';

export class MyComponent {
  constructor(private dialogService: DialogService) {}

  showSimpleConfirmation(): void {
    const dialog = this.dialogService.showConfirmationDialog(
      "Your changes have been saved successfully.",
      "Success",
      "OK"
    );

    dialog.closed.then((result) => {
      console.log(`Confirmation dialog closed with cancel: ${result.cancel}`);
    });
  }
}
```

### showQuestionDialog

Shows a standard non-closeable modal dialog with a positive and a negative button.

**Config interface:**
- content: string | ISimpleDialogCreateOptions - The content to be rendered inside the dialog (required)
- title: string - Dialog title
- positiveText: string - Text to display in the positive button - defaults to "Ok"
- negativeText: string - Text to display in the negative button - defaults to "Cancel"

**Returns:** IDialog<DialogResult> with:
- dismiss(): void - Method to cancel the dialog
- closed: Promise<{ value?: DialogResult; cancel: boolean }> - Promise resolved with DialogResult.Ok (0) for positive and DialogResult.Cancel (1) for negative
- result: Promise<DialogResult> - Promise resolved with DialogResult.Ok or DialogResult.Cancel
- buttonClick: Event<number> - Event raised when a button is clicked with the button index

**Payload shape:** Legacy API returns Promise<{ value?: DialogResult; cancel: boolean }> for closed promise and Promise<DialogResult> for result promise. These are plain typed objects, NOT CustomEvent-wrapped values. .detail access is NOT needed for service method returns.

**When to use:**
- Binary choice dialogs where user must confirm or cancel an action
- Situations requiring positive vs negative decision
- When you need the DialogResult enum return value for clear decision handling

**How to use:**

```typescript
import { DialogService } from '../public-api/dialogs.i';
import { DialogResult } from '../public-api/dialogs.i';

export class MyComponent {
  constructor(private dialogService: DialogService) {}

  showDeleteConfirmation(): void {
    const dialog = this.dialogService.showQuestionDialog(
      "Are you sure you want to delete this item?",
      "Confirm Deletion",
      "Yes, delete",
      "Cancel"
    );

    dialog.result.then((result) => {
      if (result === DialogResult.Ok) {
        console.log("User confirmed deletion");
        // Perform deletion
      } else {
        console.log("User cancelled");
      }
    });
  }
}
```

### showOptionDialog

Shows a standard non-closeable modal dialog with a custom set of buttons.

**Config interface:**
- content: string | ISimpleDialogCreateOptions - The content to be rendered inside the dialog (required)
- buttons: (string | IDialogCreateOptionsButtonDefinition)[] - Array of strings or definition to use as button titles (required)
- title: string - Dialog title

**Returns:** IDialog<number> with:
- dismiss(): void - Method to cancel the dialog
- closed: Promise<{ value?: number; cancel: boolean }> - Promise resolved with the index of the clicked button
- result: Promise<number> - Promise resolved with the index of the clicked button
- buttonClick: Event<number> - Event raised when a button is clicked with the button index

**Payload shape:** Legacy API returns Promise<{ value?: number; cancel: boolean }> for closed promise and Promise<number> for result promise. These are plain typed objects, NOT CustomEvent-wrapped values. .detail access is NOT needed for service method returns.

**When to use:**
- When you need to offer users multiple choices beyond binary options
- Situations requiring custom button configurations
- When you need the button index as the return value for programmatic handling

**How to use:**

```typescript
import { DialogService } from '../public-api/dialogs.i';

export class MyComponent {
  constructor(private dialogService: DialogService) {}

  showMultipleOptions(): void {
    const dialog = this.dialogService.showOptionDialog(
      "Please select an export format:",
      ["PDF", "Excel", "CSV", "JSON"],
      "Export Options"
    );

    dialog.result.then((selectedIndex) => {
      console.log(`User selected option ${selectedIndex}`);
      const formats = ["PDF", "Excel", "CSV", "JSON"];
      console.log(`Selected format: ${formats[selectedIndex]}`);
      // Perform export with selected format
    });
  }
}
```

### showTopLevelWindow

Creates and shows a custom (empty) top-level non-modal window.

**Config interface:**
- template: string | IonElement - The body of the HTML template of the window content
- size: DialogSize - Size of the window (Small, Large, Auto, or Fixed)
- position: IDialogPosition - The initial position of the dialog - an object with left and top properties in pixels
- openNewWindow: boolean - If true opens the dialog in a child browser window
- autoFitVertically: boolean - Open the top level child window in auto-fit mode
- resizable: boolean - Enable window resizing, false by default
- escToClose: boolean - Should the top-level dialog close when the Esc key is pressed? Default is false

**Returns:** IDialog<void> with:
- dismiss(): void - Method to cancel the dialog
- closed: Promise<{ value?: void; cancel: boolean }> - Promise fulfilled when the dialog is closed
- result: Promise<void> - Promise resolved when dialog is closed
- buttonClick: Event<number> - Event raised when a button is clicked
- ready?: Promise<IChildWindow> - Promise resolved when the Child Window is ready (only if openNewWindow was set)
- show(): void - Method to show the dialog
- hide(): void - Method to hide the dialog
- bringToFront(): void - Method to bring the dialog to front (supported only for non-modal dialogs)

**Payload shape:** Legacy API returns Promise<{ value?: void; cancel: boolean }> for closed promise. These are plain typed objects, NOT CustomEvent-wrapped values. .detail access is NOT needed for service method returns.

**When to use:**
- When you need multiple non-modal windows visible simultaneously
- For floating panels or windows that should not block the main interface
- Situations requiring drag-and-resize functionality
- When you need panels that stay open while allowing interaction with the main UI

**How to use:**

```typescript
import { DialogService } from '../public-api/dialogs.i';
import { DialogSize, IDialogPosition } from '../public-api/dialogs.i';

export class MyComponent {
  constructor(private dialogService: DialogService) {}

  showFloatingPanel(): void {
    const position: IDialogPosition = { left: 100, top: 50 };

    const options = {
      template: `<div class="floating-panel">
        <h3>Properties Panel</h3>
        <p>Drag this panel to reposition it.</p>
      </div>`,
      position: position,
      size: DialogSize.Auto,
      resizable: true
    };

    const window = this.dialogService.showTopLevelWindow(options);

    window.closed.then((result) => {
      console.log(`Floating panel closed. Cancel: ${result.cancel}`);
    });
  }
}
```

### showTopLevelDialog

Creates and shows a standard (with title and buttons) top-level non-modal dialog.

**Config interface:**
- title: string - The title of the dialog. By default is empty
- template: string | IonElement - The body of the HTML template of the dialog content
- buttons: (string | IDialogCreateOptionsButtonDefinition)[] - Buttons to add at the bottom of the dialog
- captionButtons: IDialogCaptionButton[] - Buttons to be added in header
- canClose: boolean - Should the standard X button to be rendered in the caption? By default is false
- severity: DialogSeverity - Get/Set the severity style of the dialog (Info, Warning, Danger, Success, or Neutral)
- dialogClassID: string - Class ID of dialog used for cascading
- size: DialogSize - Size of the dialog window (Small, Large, Auto, or Fixed)
- position: IDialogPosition - The initial position of the dialog - an object with left and top properties in pixels
- openNewWindow: boolean - If true opens the dialog in a child browser window
- autoFitVertically: boolean - Open the top level child window in auto-fit mode
- resizable: boolean - Enable window resizing, false by default
- escToClose: boolean - Should the top-level dialog close when the Esc key is pressed? Default is false

**Returns:** IDialog<T> with:
- dismiss(): void - Method to cancel the dialog
- closed: Promise<{ value?: T; cancel: boolean }> - Promise fulfilled when the dialog is closed
- result: Promise<T> - Promise resolved with the dialog result value
- buttonClick: Event<number> - Event raised when a button is clicked with the button index
- show(): void - Method to show the dialog
- hide(): void - Method to hide the dialog
- bringToFront(): void - Method to bring the dialog to front (supported only for non-modal dialogs)

**Payload shape:** Legacy API returns Promise<{ value?: T; cancel: boolean }> for closed promise. These are plain typed objects, NOT CustomEvent-wrapped values. .detail access is NOT needed for service method returns.

**When to use:**
- When you need non-modal dialogs with standard structure (title, buttons)
- For multiple simultaneous dialogs that don't block the main interface
- Situations requiring cascading dialog positioning
- When you need dialog classes for managing multiple related dialogs

**How to use:**

```typescript
import { DialogService } from '../public-api/dialogs.i';
import { DialogSeverity, IDialogPosition } from '../public-api/dialogs.i';

export class MyComponent {
  constructor(private dialogService: DialogService) {}

  showPropertiesDialog(): void {
    const position: IDialogPosition = { left: 200, top: 100 };

    const options = {
      title: "Properties",
      severity: DialogSeverity.Info,
      position: position,
      canClose: true,
      dialogClassID: "propertiesDialog",
      buttons: [
        {
          title: "Apply",
          role: "primary"
        },
        {
          title: "Close",
          role: "secondary"
        }
      ],
      template: `<div class="properties-content">
        <p>Properties panel content here</p>
      </div>`
    };

    const dialog = this.dialogService.showTopLevelDialog(options);

    dialog.result.then((result) => {
      console.log(`Properties dialog closed with result: ${result}`);
    });
  }
}
```

## When to use which approach

This component is a service-only component — it has no template element representation. All dialog instances must be created through the DialogService methods.

**Choose `showModal` when:**
- You're implementing new functionality and can use the modern design system API
- You need the simplified IModalDialog return type with Promise-based lifecycle management
- You want access to the full range of design system configuration options (intent, mobile placement, custom spacing, etc.)
- You need design system-specific features like intent icons, modern button configurations, and responsive mobile layouts
- You're working on features that should only run in design system mode

**Choose legacy API methods (`show`, `showCustom`, `showConfirmationDialog`, `showQuestionDialog`, `showOptionDialog`, `showTopLevelWindow`, `showTopLevelDialog`) when:**
- You're maintaining existing code that already uses these APIs and would benefit from design system styling without major refactoring
- You need to support both design system and non-design system modes within the same codebase
- You rely on specific legacy features like severity enumeration, DialogSize enum values, or the traditional buttonClick event pattern
- You need features that were deprecated or removed in the new showModal API (e.g., draggable dialogs, custom positioning, top-level windows)

## Examples

```typescript
const options: IModalDialogOptions = {
  title: "Modal Dialog",
  intent: "warning",
  showCloseButton: true,
  width: "md",
  footerEndButtons: [
    {
      label: "OK",
      onClick: () => {
        console.log("SUBMITTED");
      }
    }
  ]
};

const content = "A Modal Dialog is a focused overlay that temporarily interrupts the main interface to capture user attention for critical information or actions.";

const dialog = this.dialogService.showModal(content, options);
```
Demonstrates a standard warning modal dialog with title, content, and action button.

```typescript
const dialogOptions: IModalDialogOptions = {
  title: "Modal Dialog",
  intent: "neutral",
  showCloseButton: true,
  width: "md",
  maxHeight: "30vh",
  height: "300px",
  showIcon: true,
  icon: "placeholder",
  mobilePlacement: "full-screen",
  disableEscapeClose: true,
  closeOnClickOutside: true,
  footerStartButton: {
    label: "Start",
    onClick: () => {
      console.log("Start Clicked");
    }
  },
  footerEndButtons: [
    {
      label: "Cancel",
      intent: "secondary",
      emphasis: "moderate",
      onClick: () => {
        console.log("CANCELLED");
        dialog.dismiss();
      }
    },
    {
      label: "Submit",
      onClick: () => {
        console.log("SUBMITTED");
      }
    }
  ],
  headerIcons: [
    { icon: "help", ariaLabel: "Help", label: "Help", onClick: () => console.log("HELP CLICKED") },
    { icon: "delete", ariaLabel: "Delete", label: "Delete", onClick: () => console.log("DELETED") },
    { icon: "settings", ariaLabel: "Settings", label: "Settings", onClick: () => console.log("SETTINGS CLICKED") }
  ]
};

const dialogContents = this.componentService.createNgComponent(DialogContentComponent);
const dialogContent = dialogContents.location.nativeElement;
const dialog = this.dialogService.showModal(dialogContent, dialogOptions);
```
Demonstrates comprehensive dialog configuration with custom content, header icons, and multiple footer buttons.

```typescript
const legacyOptions = {
  title: "Warning Dialog",
  severity: DialogSeverity.Warning,
  canClose: true,
  textContent: "This is a warning message that requires your attention.",
  buttons: [
    {
      title: "Cancel",
      role: "secondary"
    },
    {
      title: "Proceed",
      role: "primary"
    }
  ]
};

const dialog = this.dialogService.show(legacyOptions);

dialog.closed.then((result) => {
  console.log(`Legacy dialog closed. Value: ${result.value}, Cancel: ${result.cancel}`);
});
```
Demonstrates legacy API usage with severity enumeration and standard button configuration for design system mode.

```typescript
const questionDialog = this.dialogService.showQuestionDialog(
  "Are you sure you want to delete this item?",
  "Confirm Deletion",
  "Yes, delete",
  "Cancel"
);

questionDialog.result.then((result) => {
  if (result === DialogResult.Ok) {
    console.log("User confirmed deletion");
  } else {
    console.log("User cancelled");
  }
});
```
Demonstrates question dialog with positive and negative buttons using showQuestionDialog legacy method.

```typescript
const optionsDialog = this.dialogService.showOptionDialog(
  "Please select an export format:",
  ["PDF", "Excel", "CSV", "JSON"],
  "Export Options"
);

optionsDialog.result.then((selectedIndex) => {
  const formats = ["PDF", "Excel", "CSV", "JSON"];
  console.log(`User selected option ${selectedIndex}: ${formats[selectedIndex]}`);
});
```
Demonstrates option dialog with multiple custom buttons using showOptionDialog legacy method.

```typescript
const topLevelOptions = {
  title: "Properties Panel",
  position: { left: 100, top: 50 },
  canClose: true,
  resizable: true,
  buttons: [
    {
      title: "Apply",
      role: "primary"
    },
    {
      title: "Close",
      role: "secondary"
    }
  ],
  template: "<div class='properties-content'><p>Property settings here</p></div>"
};

const topLevelDialog = this.dialogService.showTopLevelDialog(topLevelOptions);

topLevelDialog.result.then((result) => {
  console.log(`Top-level dialog closed with result: ${result}`);
});
```
Demonstrates non-modal top-level dialog with positioning and resizing capabilities using showTopLevelDialog legacy method.
