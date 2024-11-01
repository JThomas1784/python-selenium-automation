# Created by jamontethomas at 11/1/24
Feature: User can open and close Terms and Conditions from sign-in page

  Scenario: User can open and close Terms and Conditions from sign in page
 Given user open the sign-in page
 When user accesses the store original window
 And clicks on Target terms and conditions link
 And switches to the newly opened window
 Then user can verify Terms and Conditions page is opened
 And User can close new window and switch back to original