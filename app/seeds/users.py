from app.models import db, User, environment, SCHEMA, Question, UserAnswer


# Adds a demo user, you can add other users here if you want
def seed_users():
    riktor = User(
        username='riktor', email='demo@user.io', password='password', age=20, first_name='riktor',
        gender='male', preferred_genders='female', min_age=20, max_age=40, city='Beverly Hills', state='CA', bio='I like to run fast'
    )
    viktor = User(
        username='viktor', email='viktor@aa.io', password='password', age=20, first_name='viktor',
        gender='male', preferred_genders='female', min_age=20, max_age=40, city='Beverly Hills', state='CA', bio='I like to jump high'
    )
    edktor = User(
        username='edktor', email='edktor@aa.io', password='password', age=20, first_name='edktor',
        gender='male', preferred_genders='female', min_age=20, max_age=40, city='Beverly Hills', state='CA', bio='I like to eat fast'
    )
    abcde = User(
        username='abcde', email='abcde@aa.io', password='password', age=20, first_name='abcde',
        gender='female', preferred_genders='male', min_age=20, max_age=40, city='Beverly Hills', state='CA', bio="It's pronounced ab city"
    )
    optimusa = User(
        username='optimusa', email='optimusa@aa.io', password='password', age=20, first_name='optimusa',
        gender='female', preferred_genders='male', min_age=20, max_age=40, city='Beverly Hills', state='CA', bio='My mom really liked transformers'
    )
    camden = User(
        username="camcam", email="camcam@gmail.com", password="camcam",
        age=22, first_name="Camden", gender="male", preferred_genders="female",
        min_age=18, max_age=30, city='San Francisco', state='CA', bio="Like to look toward the future and travels lots."
    )
    tam = User(
        username="tamtam", email="tamtam@gmail.com", password="tamtam",
        age=25, first_name="Tam", gender="female", preferred_genders="female, male",
        min_age=20, max_age=35, city='San Francisco', state='CA', bio="All I do all day is sit on my butt and watch my cats."
    )
    jack = User(
        username="jack_bauer", email="jack_bauer@gmail.com", password="jack_bauer",
        age=22, first_name="Jack", gender="male", preferred_genders="female",
        min_age=18, max_age=30, city='San Francisco', state='CA', bio="I am running out of time! tick tock tick tock"
    )
    micheal = User(
        username="littlekidlover", email="bestboss@gmail.com", password="1234",
        age=40, first_name="Micheal", gender="male", preferred_genders="female",
        min_age=30, max_age=50, city='San Francisco', state='CA', bio="I want kids, lots of them if you cannot tell by my user name. I am a manager, comedian, and a friend."
    )
    cupid = User(
        username="thecupid", email="okstupid@gmail.com", password="okstupid",
        age=25, first_name="Cupid", gender="nonbinary", preferred_genders="nonbinary",
        min_age=18, max_age=100, city='San Francisco', state='CA', bio="This cupid is loved by all and loves all"
    )
    demo5 = User(
        username="Demo5", email="demo5@aa.io", password="password", age=35, first_name="Demaux", gender="nonbinary", preferred_genders="nonbinary", min_age=26, max_age=36, city='San Francisco', state='CA', bio="I love being a demo user!"
    )
    alpal = User(
        username="alpal", email="alpal@aa.io", password="password", age=26, first_name="Alex", gender="female", preferred_genders="male, female, nonbinary", min_age=26, max_age=38, city='San Francisco', state='CA', bio="brb learning to code")
    wesley = User(
        username="dreadPirate", email="dread_pirate@aa.io", password="password", age=25, first_name="Wesley", gender="male", preferred_genders="female", min_age=18, max_age=30, city='San Francisco', state='CA', bio="I am on a quest to save my love Buttercup from Prince Humperdink! But hmu might have time to take a stroll through the fire swamp")
    buttercup = User(
        username="princess", email="princess@aa.io", password="password", age=20, first_name="Buttercup", gender="female", preferred_genders="male", min_age=20, max_age=45, city='San Francisco', state='CA', bio="Waiting for my Wesley to come save me. Will you get here first?")
    inigo = User(
        username="inigo_montoya", email="inigo_montoya@aa.io", password="password", age=35, first_name="Inigo", gender="male", preferred_genders="female, male, nonbinary", min_age=25, max_age=55, city='San Francisco', state='CA', bio="My name is Inigo Montoya. You killed my father. Prepare to die.")
    brett = User(
        username='brett', email='brett@aa.io', password='password', age=51, first_name='Brett', gender='male', preferred_genders='female', min_age=30, max_age=80, city='Beverly Hills', state='CA', bio='I like pickleball and long walks on the beach. #retiredlyf'
    )
    lyn = User(
        username='lyn', email='lyn@aa.io', password='password', age=53, first_name='Lyn', gender='female', preferred_genders='male', min_age='30', city='Beverly Hills', state='CA', bio='Cats are my thing. I foster all types of animals. Ex-field hockey pro'
    )
    conner = User(
        username='conner', email='conner@aa.io', password='password', age=28, first_name='Conner', gender='male', preferred_genders='male, female, nonbinary', min_age=18, max_age=99, city='Beverly Hills', state='CA', bio='Call me dungeon master. Started with world of warcraft and now I run my own games. You can find me in that fresh powpow'
    )
    eddy = User(
        username='eddy', email='eddy@aa.io', password='password', age=22, first_name='Eddy', gender='female', preferred_genders='male, female, nonbinary', min_age=18, max_age=50, city='Beverly Hills', state='CA', bio='I am studying to be a nurse practitioner. I used to play lacrosse but now I hate it with a passion. #cape'
    )
    demo = User(
        username='demo', email='demo@aa.io', password='password', age=35, first_name='Demo', gender='male', preferred_genders='male', min_age=18, max_age=99, city='Beverly Hills', state='CA', bio='I will demolish you.'
    )
    user99m = User(
        username='user99m', email='user99m@aa.io', password='password', age=99, first_name='OldUser', gender='male', preferred_genders='male, female, nonbinary', min_age=18, max_age=99, city='Washington', state='DC', bio='I am 99'
    )
    user99f = User(
        username='user99f', email='user99f@aa.io', password='password', age=99, first_name='OldUser', gender='female', preferred_genders='male, female, nonbinary', min_age=18, max_age=99, city='Washington', state='DC', bio='I am 99'
    )
    user95m = User(
        username='user95m', email='user95m@aa.io', password='password', age=95, first_name='OldUser', gender='male', preferred_genders='male, female, nonbinary', min_age=18, max_age=99, city='Washington', state='DC', bio='I am 95'
    )
    user95f = User(
        username='user95f', email='user95f@aa.io', password='password', age=95, first_name='OldUser', gender='female', preferred_genders='male, female, nonbinary', min_age=18, max_age=99, city='Washington', state='DC', bio='I am 95'
    )
    user90m = User(
        username='user90m', email='user90m@aa.io', password='password', age=90, first_name='OldUser', gender='male', preferred_genders='male, female, nonbinary', min_age=18, max_age=99, city='Washington', state='DC', bio='I am 90'
    )
    user90f = User(
        username='user90f', email='user90f@aa.io', password='password', age=90, first_name='OldUser', gender='female', preferred_genders='male, female, nonbinary', min_age=18, max_age=90, city='Washington', state='DC', bio='I am 90'
    )
    user85m = User(
        username='user85m', email='user85m@aa.io', password='password', age=85, first_name='OldUser', gender='male', preferred_genders='male, female, nonbinary', min_age=18, max_age=99, city='Washington', state='DC', bio='I am 85'
    )
    user85f = User(
        username='user85f', email='user85f@aa.io', password='password', age=85, first_name='OldUser', gender='female', preferred_genders='male, female, nonbinary', min_age=18, max_age=90, city='Washington', state='DC', bio='I am 85'
    )
    user80m = User(
        username='user80m', email='user80m@aa.io', password='password', age=80, first_name='OldUser', gender='male', preferred_genders='male, female, nonbinary', min_age=18, max_age=99, city='Washington', state='DC', bio='I am 80'
    )
    user80f = User(
        username='user80f', email='user80f@aa.io', password='password', age=80, first_name='OldUser', gender='female', preferred_genders='male, female, nonbinary', min_age=18, max_age=90, city='Washington', state='DC', bio='I am 80'
    )
    user75m = User(
        username='user75m', email='user75m@aa.io', password='password', age=75, first_name='OldUser', gender='male', preferred_genders='male, female, nonbinary', min_age=18, max_age=99, city='Washington', state='DC', bio='I am 75'
    )
    user75f = User(
        username='user75f', email='user75f@aa.io', password='password', age=75, first_name='OldUser', gender='female', preferred_genders='male, female, nonbinary', min_age=18, max_age=90, city='Washington', state='DC', bio='I am 75'
    )
    user70m = User(
        username='user70m', email='user70m@aa.io', password='password', age=70, first_name='OldUser', gender='male', preferred_genders='male, female, nonbinary', min_age=18, max_age=99, city='Washington', state='DC', bio='I am 70'
    )
    user70f = User(
        username='user70f', email='user70f@aa.io', password='password', age=70, first_name='OldUser', gender='female', preferred_genders='male, female, nonbinary', min_age=18, max_age=90, city='Washington', state='DC', bio='I am 70'
    )
    user65m = User(
        username='user65m', email='user65m@aa.io', password='password', age=65, first_name='OldUser', gender='male', preferred_genders='male, female, nonbinary', min_age=18, max_age=99, city='Washington', state='DC', bio='I am 65'
    )
    user65f = User(
        username='user65f', email='user65f@aa.io', password='password', age=65, first_name='OldUser', gender='female', preferred_genders='male, female, nonbinary', min_age=18, max_age=90, city='Washington', state='DC', bio='I am 65'
    )
    user60m = User(
        username='user60m', email='user60m@aa.io', password='password', age=60, first_name='OldUser', gender='male', preferred_genders='male, female, nonbinary', min_age=18, max_age=99, city='Washington', state='DC', bio='I am 60'
    )
    user60f = User(
        username='user60f', email='user60f@aa.io', password='password', age=60, first_name='OldUser', gender='female', preferred_genders='male, female, nonbinary', min_age=18, max_age=90, city='Washington', state='DC', bio='I am 60'
    )
    user55m = User(
        username='user55m', email='user55m@aa.io', password='password', age=55, first_name='OldUser', gender='male', preferred_genders='male, female, nonbinary', min_age=18, max_age=99, city='Washington', state='DC', bio='I am 55'
    )
    user55f = User(
        username='user55f', email='user55f@aa.io', password='password', age=55, first_name='OldUser', gender='female', preferred_genders='male, female, nonbinary', min_age=18, max_age=90, city='Washington', state='DC', bio='I am 55'
    )
    user50m = User(
        username='user50m', email='user50m@aa.io', password='password', age=50, first_name='OldUser', gender='male', preferred_genders='male, female, nonbinary', min_age=18, max_age=99, city='Washington', state='DC', bio='I am 50'
    )
    user50f = User(
        username='user50f', email='user55f@aa.io', password='password', age=50, first_name='OldUser', gender='female', preferred_genders='male, female, nonbinary', min_age=18, max_age=90, city='Washington', state='DC', bio='I am 50'
    )
    user45m = User(
        username='user45m', email='user45m@aa.io', password='password', age=45, first_name='OldUser', gender='male', preferred_genders='male, female, nonbinary', min_age=18, max_age=99, city='Washington', state='DC', bio='I am 45'
    )
    user45f = User(
        username='user45f', email='user45f@aa.io', password='password', age=45, first_name='OldUser', gender='female', preferred_genders='male, female, nonbinary', min_age=18, max_age=90, city='Washington', state='DC', bio='I am 45'
    )
    user40m = User(
        username='user40m', email='user40m@aa.io', password='password', age=40, first_name='OldUser', gender='male', preferred_genders='male, female, nonbinary', min_age=18, max_age=99, city='Washington', state='DC', bio='I am 40'
    )
    user40f = User(
        username='user40f', email='user40f@aa.io', password='password', age=40, first_name='OldUser', gender='female', preferred_genders='male, female, nonbinary', min_age=18, max_age=90, city='Washington', state='DC', bio='I am 40'
    )
    user35m = User(
        username='user35m', email='user35m@aa.io', password='password', age=35, first_name='OldUser', gender='male', preferred_genders='male, female, nonbinary', min_age=18, max_age=99, city='Washington', state='DC', bio='I am 35'
    )
    user35f = User(
        username='user35f', email='user35f@aa.io', password='password', age=35, first_name='OldUser', gender='female', preferred_genders='male, female, nonbinary', min_age=18, max_age=90, city='Washington', state='DC', bio='I am 35'
    )

    users = [demo, brett, lyn, conner, eddy, riktor, viktor, edktor, abcde, optimusa,
             camden, tam, jack, micheal, cupid, demo5, alpal, wesley, buttercup, inigo, user99m, user99f, user95m, user95f, user90m, user90f, user85m, user85f, user80m, user80f, user75m, user75f, user70m, user70f, user65m, user65f, user60m, user65f, user60m, user60f, user55m, user55f, user50m, user50f, user55f, user45m, user45f, user40m, user40f, user35m, user35f]

    demo.dislikes = [eddy, conner, brett, cupid]
    demo.likes = [camden, tam, demo5]
    demo5.dislikes = [cupid, viktor, abcde, micheal]
    demo5.likes = [jack, riktor, conner]
    eddy.dislikes = [demo]
    conner.dislikes = [demo]
    brett.dislikes = [demo]
    cupid.dislikes = [demo, demo5]
    viktor.dislikes = [demo5]
    abcde.dislikes = [demo5]
    micheal.dislikes = [demo5]
    [db.session.add(user) for user in users]
    questions = Question.query.all()
    [[UserAnswer(user=user, question=question)
      for question in questions] for user in users]
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.


def undo_users():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.dislikes RESTART IDENTITY CASCADE;")
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.likes RESTART IDENTITY CASCADE;")
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.user_answers RESTART IDENTITY CASCADE;")

    else:
        db.session.execute("DELETE FROM users")
        db.session.execute("DELETE FROM dislikes")
        db.session.execute("DELETE FROM likes")
        db.session.execute("DELETE FROM user_answers")

    db.session.commit()
