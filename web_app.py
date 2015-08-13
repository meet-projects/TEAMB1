from flask import Flask, render_template, request, redirect,url_for
app = Flask(__name__)

# SQLAlchemy stuff
from database_setup import Base,Recipe #<--- Import your tables here!!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def main():
    return render_template('main_page.html')

@app.route('/search' , methods=['GET','POST'])
def search():
	if request.method == 'POST':
		word = request.form["search_word"]
		matches = []
		recipes=session.query(Recipe).all()
		for recipe in recipes:
			if word in recipe.name.lower():
				matches.append(recipe)
		return render_template('search.html', matches = matches)
	else: 
		return render_template('search.html',matches=[])
			
		


@app.route('/recipe/<int:Recipe_id>')
def view_recipe(Recipe_id):
    recipe = session.query(Recipe).filter_by(id=Recipe_id).first()
    return render_template('recipe.html',recipe=recipe)

@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
	if request.method == 'GET':	
		return render_template('new_recipe.html')
	else:
		new_name = request.form['name']
        	new_ingr = request.form['ingr']
        	new_nationality = request.form['origin']
        	new_how_to = request.form['how_to']
		new_photo = request.form['photo']
		new_story = request.form['story']		
		new_recipe= Recipe(name=new_name,ingr=new_ingr,origin=new_nationality,how_to=new_how_to , photo=new_photo, story = new_story)
		session.add(new_recipe)
		session.commit()
		return redirect(url_for('view_recipe',Recipe_id=new_recipe.id))






@app.route('/culture/<string:culture_name>')
def go_to_cult(culture_name):
	cult= session.query(Recipe).filter_by(origin=culture_name)
	return render_template('country_food.html',cult=cult,country=culture_name)
	


if __name__ == '__main__':
    app.run(debug=True)




