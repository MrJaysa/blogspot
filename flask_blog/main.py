from flask import Flask, render_template, jsonify, send_file


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def homepage():
	name = "Harmony HuB"
	opening_txt = 'Still in development, Tired is going all lorems for dummy text and taking the chance to think of my cms at for now, like it\'s structure for now.... Have\'nt done the cms now so i\'ll pass jinja python datatypes in hard code '
	images_urls = [['img/pro.jpg', 'it is quite amazing looking at the sea at dusk but am thinking of taking a cool evening dive, i might catch a cold but it\'s summer so it a might.... get it?'], ['img/about.jpg', 'Skydiving and taking cool mountain arial pictures!, the temperature is chilling me up so much my adrenaline can\'t keep up and am thinking of deploying the paraschute'], ['img/pic.jpg', 'The woods at a foggy day, looking mysterious don\'t you think, some people say you can find the hibigan at this kind of period of the year...'], ['img/asse.jpg', 'you need one of these as a developer!!!!, seriously cos that system might crash and you will have to like.... get in there, you know like, really in there, get to that motherboard with tools like this']]
	logs = len(images_urls)
	info_images_urls = [['img/acad.jpg', 'The busy street of lagos', 'people hustling like never before in the streets of lagos, making millions'], ['img/about.jpg','The mountain region of china','legend has it that mystical rocks are found in abundance in this area, well could they be mystical rocks or meteor rocks'], ['img/bg.jpg', 'What the body needs', 'Yoga the exercise for both the body and mind, relaxes the muscles like never before. come and experience this'], ['img/kat.png', 'the hunger games new premier','katniss everdeen is back with new vigor, it is said that they have now discover the true mastermind behind'], ['img/img-08.jpg','Delicious treat for you', 'Ice cream every childs first love after their parent, this creams will blow mind and can be gotten close to you'], ['img/bg_02.jpg', 'Reserves in Nigeria', 'Enjoy exotic wildlife reserve at the southern region, This is a sight to behold and fresh air in plenty like none other'], ['img/img-04.jpg', 'Meadow scenes', 'Can you believe this scene is created on blender by jaysa\'s enterprise'], ['img/bg_05_big.jpg', 'The White Lotus', 'Found only in the wild but you can now grow them in your garden, you can get the seeds at harmony markets powered by harmony comm'], ['img/pic.jpg', 'The Woods in Nigeria', 'This is a good source of wood for wood works and also a great camping site you will love the experience'], ['img/bg_06.jpg', 'The Jorney: andronomeda', 'This new scene can be found in the upcoming release mass effect game'], ['img/bg_08.jpg', 'Non like Mother and Child', 'A new book release and currently trending, explaining the love behind Jessy the mom and angela the daughter how they pass'], ['img/image1.jpg', 'The early morning Jug', 'This has been taken for granted by most people but scientist just came up with a discovery']]
	advs =  [['img/acad.jpg', 'Sky scrappers Hotel', 'Jaysa\'s cooperation now offers reservations at high places'], ['img/about.jpg', 'Glade Glide @14.99$', 'Jaysa\'s cooperation now give you exotic gliding experience'], ['img/bg.jpg', 'Outdoor Yoga', 'Harmony hub offers this free for yound ladies'], ['img/kat.png', 'Jayscenama', 'Come and watch movies to stupor'], ['img/img-08.jpg', 'Tasty Treat', 'Get you tasty treats at uncle Jay store now'], ['img/bg_02.jpg', 'Wild Life', 'Jay Wild TV now showing wild life documentation'], ['img/img-06.jpg', 'Arid land', 'See how AgroJay transforms this plain land']]

	return render_template('index.html', name=name, nom=logs, images=images_urls, infos=info_images_urls, ads=advs, opening_txt=opening_txt)

@app.route('/dashboard/')
def dashboard():
	return 'hi'

@app.route('/get_image', methods=['GET'])
def get_image():
   filename = 'ok.gif'
   filename = 'error.gif'
   return send_file(filename, mimetype='image/gif')

@app.route('/api/requested/', methods=['GET'])
def receive_word():
    array = ('static/img/pro.jpg', 'static/img/about.jpg', 'static/img/pic.jpg')
    return jsonify(array)

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port=5000)