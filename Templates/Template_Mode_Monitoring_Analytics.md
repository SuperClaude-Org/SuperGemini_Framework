# [Monitoring Mode Name] Mode

```yaml
---
name: [mode-name]
description: "[Clear purpose and behavioral modification description]"
type: monitoring

# Mode Classification
category: tracking
complexity: system
scope: framework

# Activation Configuration
activation:
  automatic: [true|false]
  manual-flags: [list of flags]
  confidence-threshold: [0.0-1.0]
  detection-patterns: [monitoring trigger patterns]

# Integration Configuration
framework-integration:
  mcp-servers: [list of coordinated servers]
  commands: [list of monitored commands]
  modes: [list of coordinated modes]
  quality-gates: [monitoring integration points]

# Performance Profile
performance-profile: real-time
performance-targets: [specific monitoring requirements]
---
```

**[Optional Subtitle]** - [Brief description of real-time monitoring and metrics collection capabilities]

## Purpose & Monitoring Scope

[Clear description of what aspects of the system this mode monitors and tracks. Explain the real-time monitoring capabilities and why continuous metrics collection is critical for this domain.]

### Monitoring Domains
- **[Domain 1]**: [What aspects are monitored and why]
- **[Domain 2]**: [Specific metrics and tracking requirements]
- **[Domain 3]**: [Performance characteristics monitored]

### Tracking Objectives
- **[Objective 1]**: [Specific measurement goals and targets]
- **[Objective 2]**: [Quality metrics and thresholds]
- **[Objective 3]**: [Performance optimization goals]

## Core Capabilities

### 1. Real-Time Metrics Collection
- **[Metric Category]**: [Description of metrics tracked and collection method]
- **[Metric Category]**: [Real-time measurement approach and frequency]
- **[Metric Category]**: [Data aggregation and storage strategy]
- **[Metric Category]**: [Historical trend analysis capabilities]

### 2. Performance Monitoring
- **[Performance Aspect]**: [Specific performance metrics and targets]
- **[Performance Aspect]**: [Threshold monitoring and alert systems]
- **[Performance Aspect]**: [Optimization detection and recommendations]
- **[Performance Aspect]**: [Resource utilization tracking]

### 3. Analytics & Pattern Recognition
- **[Analysis Type]**: [Pattern detection algorithms and insights]
- **[Analysis Type]**: [Trend analysis and predictive capabilities]
- **[Analysis Type]**: [Anomaly detection and alert mechanisms]
- **[Analysis Type]**: [Correlation analysis across metrics]

### 4. Dashboard & Reporting
- **[Dashboard Type]**: [Real-time dashboard format and information]
- **[Report Format]**: [Structured reporting capabilities and frequency]
- **[Alert System]**: [Notification mechanisms and escalation paths]
- **[Export Capabilities]**: [Data export formats and integration options]

## Activation Patterns

### Automatic Activation
1. **[Monitoring Trigger]**: [Specific conditions that automatically enable monitoring]
2. **[Performance Threshold]**: [Performance degradation or optimization opportunities]
3. **[System Event]**: [System lifecycle events requiring monitoring]
4. **[Risk Indicator]**: [High-risk operations needing continuous tracking]
5. **[Quality Gate]**: [Integration with SuperGemini quality validation steps]

### Manual Activation
- **Primary Flag**: `--[shorthand]` or `--[fullname]`
- **Monitoring Scope**: `--monitor-[scope]` for targeted monitoring
- **Alert Level**: `--alert-level [level]` for threshold configuration
- **Context**: [When users would manually activate comprehensive monitoring]

### Smart Detection Patterns
- **[Pattern Type]**: [Detection algorithms and confidence thresholds]
- **[Context Indicator]**: [Situational awareness patterns]
- **[Risk Assessment]**: [Risk-based activation strategies]

## Performance Targets

### Response Time Requirements
- **Metrics Collection**: [Target collection frequency and latency]
- **Dashboard Updates**: [Real-time update requirements]
- **Alert Generation**: [Alert response time targets]
- **Report Generation**: [Report compilation time limits]

### Accuracy Standards
- **Measurement Precision**: [Required accuracy levels for different metrics]
- **Data Integrity**: [Data validation and consistency requirements]
- **Historical Accuracy**: [Long-term data preservation standards]

### Resource Efficiency
- **CPU Overhead**: [Maximum CPU usage for monitoring operations]
- **Memory Usage**: [Memory footprint limits and optimization]
- **Storage Requirements**: [Data retention and compression strategies]
- **Network Impact**: [Network utilization limits for distributed monitoring]

## Monitoring Framework

### Metrics Collection Engine
- **[Collection Method]**: [Real-time data collection approach and tools]
- **[Aggregation Strategy]**: [Data aggregation algorithms and time windows]
- **[Storage Architecture]**: [Metrics storage and retrieval system]
- **[Retention Policy]**: [Data lifecycle and archival strategies]

### Real-Time Monitoring Systems
- **[Monitoring Component]**: [Continuous monitoring implementation]
- **[Alert Engine]**: [Real-time alert generation and routing]
- **[Threshold Management]**: [Dynamic threshold adjustment capabilities]
- **[Escalation System]**: [Alert escalation and notification workflows]

### Analytics Infrastructure
- **[Analysis Engine]**: [Real-time analytics processing capabilities]
- **[Pattern Detection]**: [Automated pattern recognition systems]
- **[Predictive Analytics]**: [Forecasting and trend prediction capabilities]
- **[Correlation Analysis]**: [Cross-metric correlation and causation analysis]

## Integration Patterns

### Session Lifecycle Integration
- **Session Start**: [Monitoring initialization and baseline establishment]
- **Active Monitoring**: [Continuous tracking during work sessions]
- **Checkpoint Integration**: [Metrics capture during checkpoints]
- **Session End**: [Final metrics collection and summary generation]

### Quality Gates Integration
- **[Quality Gate Step]**: [Specific monitoring integration point]
- **[Validation Phase]**: [Performance validation during quality checks]
- **[Compliance Monitoring]**: [Framework compliance tracking]

### Command Coordination
- **[Command Category]**: [Monitoring integration with specific command types]
- **[Operation Type]**: [Performance tracking for different operation categories]
- **[Workflow Integration]**: [Monitoring embedded in standard workflows]

### MCP Server Coordination
- **[Server Name]**: [Monitoring integration with specific MCP servers]
- **[Cross-Server Analytics]**: [Coordination monitoring across multiple servers]
- **[Performance Correlation]**: [Server performance impact analysis]

### Mode Interactions
- **[Coordinated Mode]**: [How monitoring integrates with other active modes]
- **[Mode Switching]**: [Monitoring behavior during mode transitions]
- **[Multi-Mode Analytics]**: [Analysis across multiple active modes]

## Analytics & Reporting

### Dashboard Formats
- **[Dashboard Type]**: [Real-time dashboard structure and components]
- **[Visualization Format]**: [Chart types and data presentation methods]
- **[Interactive Features]**: [User interaction capabilities and drill-down options]

### Report Structures
- **[Report Category]**: [Structured report format and content organization]
- **[Summary Format]**: [Executive summary and key metrics presentation]
- **[Detailed Analysis]**: [In-depth analysis report structure]

### Trend Analysis
- **[Trend Type]**: [Historical trend analysis capabilities]
- **[Predictive Modeling]**: [Forecasting algorithms and accuracy metrics]
- **[Comparative Analysis]**: [Baseline comparison and performance evolution]

### Alert Systems
- **[Alert Level]**: [Alert severity classification and response requirements]
- **[Notification Methods]**: [Alert delivery mechanisms and routing]
- **[Escalation Procedures]**: [Alert escalation workflows and timeouts]

## Advanced Features

### [Feature Category 1]
- **[Advanced Feature]**: [Description of sophisticated monitoring capability]
- **[Integration Method]**: [How advanced features integrate with core monitoring]
- **[Performance Impact]**: [Resource requirements and optimization strategies]

### [Feature Category 2]
- **[Analytics Feature]**: [Advanced analytics and machine learning capabilities]
- **[Automation Feature]**: [Automated response and optimization features]
- **[Integration Feature]**: [Advanced integration with external systems]

## Hook System Integration

### Event-Driven Monitoring
- **[Hook Category]**: [Monitoring hooks for specific event types]
- **[Trigger Events]**: [Events that activate monitoring collection]
- **[Response Actions]**: [Automated responses to monitoring events]

### Performance Hooks
- **[Performance Event]**: [Performance-related hook integration]
- **[Optimization Trigger]**: [Automatic optimization based on monitoring data]
- **[Alerting Hook]**: [Hook-based alert generation and routing]

## Error Handling & Recovery

### Monitoring Failures
- **[Failure Type]**: [How different monitoring failures are handled]
- **[Fallback Strategy]**: [Backup monitoring approaches and degraded modes]
- **[Recovery Procedure]**: [Automatic recovery and manual intervention options]

### Data Integrity
- **[Validation Method]**: [Data validation and consistency checking]
- **[Corruption Handling]**: [Data corruption detection and recovery]
- **[Backup Strategy]**: [Monitoring data backup and restoration procedures]

## Configuration

```yaml
[mode_name]_monitoring:
  # Activation Configuration
  activation:
    automatic: [true|false]
    confidence_threshold: [0.0-1.0]
    detection_patterns: [list]
    
  # Performance Targets
  performance:
    collection_frequency_ms: [number]
    alert_response_time_ms: [number]
    dashboard_update_interval_ms: [number]
    report_generation_timeout_ms: [number]
    
  # Metrics Configuration
  metrics:
    collection_interval: [duration]
    retention_period: [duration]
    aggregation_windows: [list]
    precision_level: [number]
    
  # Monitoring Scope
  scope:
    commands: [list]
    operations: [list]
    resources: [list]
    integrations: [list]
    
  # Alert Configuration
  alerts:
    enabled: [true|false]
    severity_levels: [list]
    notification_methods: [list]
    escalation_timeout: [duration]
    
  # Dashboard Configuration
  dashboard:
    real_time_updates: [true|false]
    refresh_interval_ms: [number]
    visualization_types: [list]
    interactive_features: [true|false]
    
  # Analytics Configuration
  analytics:
    pattern_detection: [true|false]
    trend_analysis: [true|false]
    predictive_modeling: [true|false]
    correlation_analysis: [true|false]
    
  # Storage Configuration
  storage:
    backend_type: [string]
    compression_enabled: [true|false]
    retention_policy: [string]
    archival_strategy: [string]
    
  # Integration Configuration
  integration:
    quality_gates: [list]
    mcp_servers: [list]
    hook_system: [true|false]
    session_lifecycle: [true|false]
```

---

# Monitoring Mode Template Guide

## Overview
This template provides a specialized format for documenting Monitoring and Analytics Modes in the SuperGemini framework. These modes focus on real-time tracking, metrics collection, performance monitoring, and analytical insights.

## Key Characteristics: Monitoring Modes

### Primary Focus Areas
- **Real-Time Tracking**: Continuous monitoring with immediate feedback
- **Performance Metrics**: Quantitative measurement and optimization
- **System Analytics**: Pattern recognition and trend analysis
- **Quality Assurance**: Compliance monitoring and validation
- **Resource Optimization**: Efficiency tracking and improvement

### Behavioral Modifications
- **Continuous Collection**: Ongoing metrics gathering during operations
- **Alert Generation**: Proactive notification of issues or opportunities
- **Dashboard Updates**: Real-time information presentation
- **Trend Analysis**: Historical pattern recognition and forecasting
- **Performance Optimization**: Automatic or recommended improvements

## Section Guidelines

### Purpose & Monitoring Scope
- Define what aspects of the system are monitored
- Explain the value and necessity of continuous tracking
- Identify specific domains and objectives for monitoring
- Clarify the scope and boundaries of monitoring activities

### Core Capabilities
- **Real-Time Metrics**: Continuous data collection and processing
- **Performance Monitoring**: System performance tracking and optimization
- **Analytics & Pattern Recognition**: Data analysis and insight generation
- **Dashboard & Reporting**: Information presentation and communication

### Activation Patterns
- Document automatic activation triggers based on system conditions
- Include performance thresholds and quality gate integration
- Specify manual activation flags and configuration options
- Define smart detection patterns and confidence thresholds

### Performance Targets
- Specify concrete timing requirements for all monitoring operations
- Define accuracy standards and data integrity requirements
- Set resource efficiency limits and optimization constraints
- Establish baseline performance metrics and improvement targets

### Monitoring Framework
- Detail the technical implementation of metrics collection
- Describe real-time monitoring systems and alert engines
- Explain analytics infrastructure and processing capabilities
- Document data storage, retention, and archival strategies

### Integration Patterns
- Show how monitoring integrates with session lifecycle
- Define quality gate integration points and validation phases
- Explain coordination with commands, MCP servers, and other modes
- Detail hook system integration for event-driven monitoring

### Analytics & Reporting
- Define dashboard formats and visualization approaches
- Specify report structures and content organization
- Explain trend analysis capabilities and predictive modeling
- Detail alert systems and notification mechanisms

### Configuration
- Comprehensive YAML configuration covering all monitoring aspects
- Include performance targets, alert settings, and integration options
- Define storage configuration and analytics capabilities
- Specify activation parameters and scope settings

## Best Practices for Monitoring Modes

### Performance-First Design
1. **Minimal Overhead**: Monitoring should not significantly impact system performance
2. **Efficient Collection**: Optimize data collection methods for minimal resource usage
3. **Smart Aggregation**: Use intelligent aggregation to reduce storage and processing requirements
4. **Selective Monitoring**: Enable targeted monitoring based on context and needs

### Real-Time Responsiveness
1. **Immediate Feedback**: Provide real-time updates and immediate alert generation
2. **Low Latency**: Minimize delay between events and monitoring response
3. **Continuous Operation**: Ensure monitoring continues even during system stress
4. **Graceful Degradation**: Maintain essential monitoring even when resources are constrained

### Data Quality & Integrity
1. **Accurate Measurement**: Ensure monitoring data is precise and reliable
2. **Consistent Collection**: Maintain consistency in data collection methods
3. **Validation Checks**: Implement data validation and integrity checking
4. **Error Handling**: Robust error handling for monitoring failures

### Integration Excellence
1. **Seamless Integration**: Monitoring should integrate transparently with existing workflows
2. **Framework Compliance**: Maintain compliance with SuperGemini framework standards
3. **Cross-Mode Coordination**: Coordinate effectively with other active modes
4. **Hook System Integration**: Leverage hook system for event-driven monitoring

## File Naming Convention
- Use prefix: `MODE_[MonitoringType]_Monitoring.md`
- Examples: `MODE_Performance_Monitoring.md`, `MODE_Quality_Analytics.md`, `MODE_Resource_Tracking.md`

## Location
All Monitoring Mode documentation files should be placed in:
`SuperGemini/Modes/`

## Integration with Template System
This template specializes the base `Template_Mode.md` for monitoring and analytics use cases, providing:
- Enhanced performance target specifications
- Comprehensive monitoring framework documentation
- Advanced analytics and reporting capabilities
- Real-time system integration patterns
- Sophisticated configuration options for monitoring systems