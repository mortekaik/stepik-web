def application(env, start_response):
	data = ''
	for item in env['QUERY_STRING'].split('&'):
		data = data + item + '\n'
	start_response('200 OK', [('Content-Type', 'text/plain')])
	return [data]