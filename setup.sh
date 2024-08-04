mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $port\n\
headless=true\n\
\n\
" > ~/.streamlit/config,toml