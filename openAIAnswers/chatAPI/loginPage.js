class AuthForm {
  constructor() {
    this.loginTextInput = '#login-username';
    this.passwordTextInput = '#login-password';
    this.loginSubmitButton = 'button.login';
  }

  enterLogin(username) {
    cy.get(this.loginTextInput).type(username);
  }

  enterPassword(password) {
    cy.get(this.passwordTextInput).type(password);
  }

  submitLogin() {
    cy.get(this.loginSubmitButton).click();
  }
}