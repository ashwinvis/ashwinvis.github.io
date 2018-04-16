watch: clean
	nohup bash -c 'cd src && make devserver' &
	nohup bash -c 'cd theme/backdrop-theme && grunt watch' &
	tail -f nohup.out

stop:
	nohup bash -c 'cd src && make stopserver' &
	nohup bash -c 'pgrep -f grunt | xargs kill -9' &

kill: stop
	nohup bash -c 'pgrep -f pelican.server | xargs kill -9' &

restart: stop watch

clean:
	rm -rf output
	rm -f nohup.out
