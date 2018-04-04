watch: clean
	nohup bash -c 'cd src && ./develop_server.sh start' &
	nohup bash -c 'cd theme/backdrop-theme && grunt watch' &
	tail -f nohup.out

kill:
	nohup bash -c 'cd src && ./develop_server.sh stop' &
	nohup bash -c 'pgrep -f grunt | xargs kill -9' &
	nohup bash -c 'pgrep -f pelican.server | xargs kill -9' &

restart: kill watch

clean:
	rm -rf output
	rm -f nohup.out
