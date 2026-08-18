# Build Booking Platforms With React and TypeScript

## 簡介

The Build Booking Platforms With React and TypeScript prompt is a free AI prompt that generates complete, production-ready booking applications for developers building reservation systems across appointments, rentals, events, travel, and accommodations. This booking platform prompt for ChatGPT, Claude, and Cursor outputs a modular React 18+ codebase with TypeScript that handles any reservable product or service through a flexible JSON-based configuration system. It delivers a full design system with Tailwind CSS and Framer Motion, core features spanning discovery to checkout, real-time availability engines, dynamic pricing displays, payment integration mockups, user dashboards, and WCAG 2.1 AA accessible interfaces. The architecture lets you add new booking types without touching the codebase, whether you're building yoga class scheduling, car rentals, hotel reservations, or event ticketing. Reach for this prompt when you need enterprise-grade booking infrastructure that scales from $50 appointments to $5000+ luxury packages while maintaining consistent performance and professional UI across all contexts. ● JSON configuration schema that adapts interfaces and business logic to match mental models for appointments, rentals, travel packages, and events without code changes ● Complete React component library with DatePicker, TimeSlot, AvailabilityCalendar, PriceDisplay, and multi-step checkout flows using modern patterns like custom hooks and Context API ● Performance optimizations including code splitting, lazy loading, memoization, virtualization, optimistic updates, and loading skeletons for production-grade responsiveness ● Full documentation covering setup, development workflow, step-by-step guides for adding booking types via configuration, and deployment considerations for hosting and build optimization ## Prompt

```
## Role

Senior full-stack engineer specializing in booking systems, inventory management, real-time availability, dynamic pricing, and conversion optimization.

## Task

Build a production-ready universal booking application using React 18+ with TypeScript that handles any type of reservable product or service through a flexible JSON-based configuration system.

## Context

The platform supports diverse booking types (appointments, rentals, travel packages, event tickets, accommodations) with prices ranging from $50 to $5000+. The system uses JSON configuration to adapt interfaces to match user mental models for each booking type while maintaining consistent technical architecture and enterprise-grade performance.

{{booking-requirements}}

Specify: booking categories to support, required features (calendar/time-slot selection, capacity limits, cancellation policies, guest management, add-ons, etc.), visual style and brand guidelines, technology stack modifications, performance targets, and accessibility requirements.

## Output

Deliver complete, production-ready code with this structure:

### Configuration System
- JSON schema defining booking category behavior (availability rules, pricing models, form fields, validation)
- TypeScript interfaces for type safety across all booking types
- 3+ example configurations showing appointments, rentals, and event bookings
- Documentation on adding new booking types without code changes

### Design System & Components
- Tailwind CSS with modern glass-morphism effects and minimalist design language
- Reusable component library: DatePicker, TimeSlot, AvailabilityCalendar, PriceDisplay, BookingSummary
- Framer Motion micro-interactions for state transitions and feedback
- Responsive patterns optimized for mobile, tablet, and desktop
- Professional color scheme and typography that scales across price points

### Core Features
- **Discovery**: Search/filter interface with real-time results, sorting, and faceted navigation
- **Selection**: Product detail view with visual availability feedback, dynamic pricing display, capacity indicators
- **Checkout**: Multi-step flow (date/time → options → details → payment) with progress tracking, inline validation, and cart persistence
- **Payment**: Integration mockup (Stripe/PayPal interface)
- **Dashboard**: User booking management (upcoming/past/cancelled), rebooking, cancellation handling
- **Account**: Profile, preferences, payment methods, notification settings

### Code Quality
- Complete file structure with clear separation of concerns (components/, hooks/, utils/, types/, config/)
- Modern React patterns: custom hooks for booking logic, Context for global state, composition over inheritance
- Comprehensive TypeScript typing with no `any` types
- Error boundaries, loading skeletons, optimistic updates
- Performance optimizations: code splitting, lazy loading, memoization, virtualization for lists
- WCAG 2.1 AA compliance: keyboard navigation, ARIA labels, focus management, color contrast
- Realistic mock data covering edge cases (sold out dates, partial availability, price variations, multi-day bookings)

### Documentation
- Setup instructions (dependencies, environment variables, dev server)
- Development workflow and folder conventions
- Step-by-step guide for adding new booking types via JSON configuration
- Deployment considerations (environment setup, build optimization, hosting recommendations)

Emphasize modular, configurable architecture. The same codebase should elegantly handle a yoga class booking, car rental, and hotel reservation through configuration alone.
```

## 用法 / Usage
- 必填變數 / Variables: {{booking-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Build Booking Platforms With React and TypeScript prompt is a free AI prompt that generates complete, prod…
