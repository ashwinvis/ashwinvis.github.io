watch: clean
	nohup bash -c 'cd backdrop-theme && grunt serve' &
	xdg-open http://localhost:8000
	nohup bash -c 'cd src && make devserver' &
	tail -f nohup.out

kill:
	nohup bash -c 'pgrep -f grunt | xargs kill -9' &
	nohup bash -c 'pgrep -f pelican | xargs kill -9' &

restart: kill watch

clean:
	rm -rf output
	rm -f nohup.out
