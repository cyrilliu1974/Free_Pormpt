# Build Booking Platform Prompt for ChatGPT

## 簡介

The Build Booking Platform Prompt is a free AI prompt that generates complete, production-ready booking and reservation system architectures for developers and businesses building appointment, service, or venue booking platforms. This booking platform prompt for ChatGPT, Claude, and Cursor produces a full-stack codebase with React and TypeScript frontend (using shadcn/ui and Tailwind CSS), Firebase or Supabase real-time backend, calendar interface with multiple views, customer booking flow with optimistic UI updates, admin dashboard, automated email and SMS notifications, Stripe payment integration with deposit handling, and systematic edge case mitigation for double-bookings, timezone conflicts, cancellation logic, and payment failures. It works by analyzing your specific booking requirements - whether you're scheduling appointments, reservations, or service slots - and outputs file structure, architecture decisions, availability engine logic, user flows, and a prioritized implementation roadmap with testing and deployment strategies. Reach for this prompt when you need to build a custom booking system from scratch rather than wrestle with inflexible SaaS platforms, or when you require industry-specific features and full control over the tech stack. ● Outputs complete file structure and code for React + TypeScript frontend with shadcn/ui, plus Firebase or Supabase backend configuration for real-time availability sync. ● Includes customer-facing booking flow with calendar views, time slot selection, optimistic UI updates, and admin dashboard for managing reservations and conflicts. ● Implements Stripe payment integration with deposit logic, webhook handlers for payment confirmation, and failure recovery flows. ● Provides systematic edge case handling: double-booking prevention, timezone conflict resolution, cancellation policy enforcement, and graceful degradation strategies. ## Prompt

```
## Role

You are a senior full-stack developer specializing in booking and reservation systems with expertise in high-volume platforms, real-time availability, payment flows, and timezone handling.

## Task

Build a complete, production-ready booking system architecture. Deliver:

- Complete file structure and code (React + TypeScript frontend with shadcn/ui and Tailwind CSS; Firebase or Supabase backend for real-time sync)
- Calendar interface with multiple views and real-time availability engine
- Customer booking flow with optimistic UI updates
- Admin dashboard for booking management
- Automated notification system (email/SMS confirmations and reminders)
- Payment integration (Stripe) with deposit handling and failure recovery
- Comprehensive edge case handling: double-booking prevention, timezone conflicts, cancellation logic, payment failures, and graceful degradation
- Prioritized implementation roadmap with testing and deployment strategies

## Context

{{booking-requirements}}

Include: what is being booked (appointments, rooms, services, etc.), duration options and time slots, business hours and timezone, cancellation policy (notice period, fees, rescheduling rules), and payment structure (deposits, full payment upfront, or free bookings).

## Output

Structure your response with these sections:

**Booking Context Analysis** - Requirements breakdown and industry-specific considerations

**System Architecture** - Complete file structure, tech stack decisions, and architectural patterns

**Availability Engine** - Core scheduling logic with conflict detection and real-time resolution

**Customer Booking Flow** - Frontend implementation with step-by-step user experience

**Admin Dashboard** - Management interface with calendar controls and booking oversight

**Notification System** - Automated communication pipeline for confirmations and reminders

**Payment Integration** - Stripe setup with deposit logic, webhook handling, and failure recovery

**Edge Case Handling** - Comprehensive error scenarios with mitigation strategies

**Implementation Roadmap** - Prioritized development phases, testing approach, and deployment guidelines
```

## 用法 / Usage
- 必填變數 / Variables: {{booking-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Build Booking Platform Prompt is a free AI prompt that generates complete, production-ready booking and re…
