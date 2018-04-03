watch:
	nohup bash -c 'cd src && ./develop_server.sh start' &
	nohup bash -c 'cd theme/backdrop-theme && grunt watch' &

kill:
	# pgrep -f pelican.server | xargs kill
	nohup bash -c 'cd src && ./develop_server.sh stop' &
	pgrep -f grunt | xargs kill

clean:
	rm -rf output
	rm -f nohup.out
