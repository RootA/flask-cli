@app.route("/")
@cache.cached(timeout=app.config['CACHE_DURATION'])
def index():
	# Logger(request.method, request.endpoint, request.url, 'Welcome to ', request.headers.get('User-Agent'), request.accept_languages)
	return jsonify({'message':'Hello world. Welcome to '})


@app.errorhandler(404)
def page_not_found():
	responseObject ={
		'message' : 'This is not the page you are looking for. Move along.'
	}
	return make_response(jsonify(responseObject)), 404

@app.errorhandler(500)
def internal_error(error):
	db.session.rollback()
	Logger(request.method,request.endpoint, request.url, error, request.headers.get('User-Agent'), request.accept_languages)
	return jsonify({'message' : str(error)}), 500