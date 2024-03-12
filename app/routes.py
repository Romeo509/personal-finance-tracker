from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, login_manager
from app.models import User, Expense
from app.forms import RegistrationForm, LoginForm



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and user.password == form.password.data:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login failed. Please check your username and password.', 'danger')

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()  # Create an instance of the RegistrationForm

    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully. You can now log in!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/expenses')
@login_required
def expenses():
    user_expenses = current_user.expenses.order_by(Expense.date_posted.desc()).all()
    return render_template('expenses.html', expenses=user_expenses)

@app.route('/add_expense', methods=['POST'])
@login_required
def add_expense():
    amount = float(request.form.get('amount'))
    category = request.form.get('category')
    description = request.form.get('description')
    
    if amount <= 0:
        flash('Invalid amount. Please enter a positive value.', 'danger')
    else:
        current_user.add_expense(amount, category, description)
        flash('Expense added successfully!', 'success')

    return redirect(url_for('expenses'))

@app.route('/delete_expense/<int:expense_id>', methods=['GET'])
@login_required
def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)

    if expense.user_id != current_user.id:
        flash('You are not authorized to delete this expense.', 'danger')
    else:
        db.session.delete(expense)
        db.session.commit()
        flash('Expense deleted successfully!', 'success')

    return redirect(url_for('expenses'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error_code=404, error_message="Page not found"), 404

# Error handling for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error_code=500, error_message="Internal Server Error"), 500

@app.route('/dashboard')
@login_required
def dashboard():
    user_expenses = current_user.expenses.order_by(Expense.date_posted.desc()).all()
    return render_template('dashboard.html', expenses=user_expenses)