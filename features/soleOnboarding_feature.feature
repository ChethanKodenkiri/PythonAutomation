Feature: Sole Account Onboarding Journey

  @SoleJourney
  Scenario: User should be able to complete the onboarding journey as Sole user (Individual)
    Given User starts sole onboarding journey by filling details
    When User fills personal details and proceeds with mobile and email verification
    And User sets password and validates the same with Cognito OTP validation
    And User completes Additional and Nominated details
    And User reviews the details entered
    Then User completes the sole onboarding journey
    And User validates the details against Mambu and CRM APIs
