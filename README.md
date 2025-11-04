# 123

```
--filter-udp=443 --hostlist="%LIST_PATH%" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="%BIN%quic_initial_www_google_com.bin" --new ^
--filter-udp=1400,596-599,50000-50100 --filter-l7=discord,stun --dpi-desync=fake --dpi-desync-repeats=6 --new ^
--wf-l3=ipv4 --wf-tcp=80 --methodeol ^
--filter-tcp=80 --hostlist="%LIST_PATH%" --dpi-desync=fake,multisplit --dpi-desync-autottl=2 --dpi-desync-fooling=md5sig --new ^
--wf-l3=ipv4 --wf-tcp=80 --methodeol ^
--wf-l3=ipv4 --wf-tcp=443 --dpi-desync=multisplit --dpi-desync-split-pos=2 --dpi-desync-split-seqovl=336 --dpi-desync-split-seqovl-pattern=/cygdrive/c/Users/pixar/Desktop/howdi/bin/blockcheck/zapret/files/fake/tls_clienthello_iana_org.bin ^
--wf-l3=ipv4 --wf-tcp=80 --dpi-desync=multisplit --dpi-desync-split-pos=method+2 ^
--wf-l3=ipv4 --wf-tcp=80 --dpi-desync=multidisorder --dpi-desync-split-pos=midsld ^
--wf-l3=ipv4 --wf-tcp=80 --dpi-desync=fake --dpi-desync-ttl=8 ^
--wf-l3=ipv4 --wf-tcp=80 --dpi-desync=fake --dpi-desync-fooling=datanoack ^
--filter-udp=443 --hostlist="%LIST_PATH%" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="%BIN%quic_initial_www_google_com.bin" --new ^
--filter-udp=1400,596-599,50000-50100 --filter-l7=discord,stun --dpi-desync=fake --dpi-desync-repeats=6 --new ^
--filter-tcp=80 --hostlist="%LIST_PATH%" --dpi-desync=fake,multisplit --dpi-desync-autottl=2 --dpi-desync-fooling=md5sig --new ^
--filter-tcp=443 --hostlist="%LIST_PATH%" --dpi-desync=multisplit --dpi-desync-repeats=2 --dpi-desync-split-seqovl=681 --dpi-desync-split-pos=1 --dpi-desync-split-seqovl-pattern="%BIN%tls_clienthello_www_google_com.bin" --new ^
--filter-udp=443 --ipset="%CLOUDFLARE_IPSET_PATH%" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="%BIN%quic_initial_www_google_com.bin" --new ^
--filter-tcp=80 --ipset="%CLOUDFLARE_IPSET_PATH%" --dpi-desync=fake,multisplit --dpi-desync-autottl=2 --dpi-desync-fooling=md5sig --new ^
--filter-tcp=443,%GModeRange% --ipset="%CLOUDFLARE_IPSET_PATH%" --dpi-desync=multisplit --dpi-desync-split-seqovl=681 --dpi-desync-split-pos=1 --dpi-desync-split-seqovl-pattern="%BIN%tls_clienthello_www_google_com.bin" --new ^
--filter-udp=%GModeRange% --ipset="%CLOUDFLARE_IPSET_PATH%" --dpi-desync=fake --dpi-desync-autottl=2 --dpi-desync-repeats=12 --dpi-desync-any-protocol=1 --dpi-desync-fake-unknown-udp="%BIN%quic_initial_www_google_com.bin" --dpi-desync-cutoff=n2 ^
--wf-l3=ipv4 --wf-tcp=443 --dpi-desync=multidisorder --dpi-desync-split-pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1 ^
--wf-l3=ipv4 --wf-tcp=443 --dpi-desync=fake --dpi-desync-fooling=badseq ^
--filter-tcp=443 --hostlist="%LIST_PATH%" --dpi-desync=multisplit --dpi-desync-split-seqovl=652 --dpi-desync-split-pos=2 --dpi-desync-split-seqovl-pattern="%BIN%tls_clienthello_www_google_com.bin" --new ^
--filter-udp=443 --ipset="%CLOUDFLARE_IPSET_PATH%" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="%BIN%quic_initial_www_google_com.bin" --new ^
--filter-tcp=80 --ipset="%CLOUDFLARE_IPSET_PATH%" --dpi-desync=fake,multisplit --dpi-desync-autottl=2 --dpi-desync-fooling=md5sig --new ^
--filter-tcp=443,%GModeRange% --ipset="%CLOUDFLARE_IPSET_PATH%" --dpi-desync=multisplit --dpi-desync-split-seqovl=652 --dpi-desync-split-pos=2 --dpi-desync-split-seqovl-pattern="%BIN%tls_clienthello_www_google_com.bin" --new ^
--filter-udp=%GModeRange% --ipset="%CLOUDFLARE_IPSET_PATH%" --dpi-desync=fake --dpi-desync-autottl=2 --dpi-desync-repeats=12 --dpi-desync-any-protocol=1 --dpi-desync-fake-unknown-udp="%BIN%quic_initial_www_google_com.bin" --dpi-desync-cutoff=n2 ^
--wf-l3=ipv4 --wf-tcp=443 --dpi-desync=fake --dpi-desync-ttl=4 ^
--wf-l3=ipv4 --wf-tcp=443 --dpi-desync=fake --dpi-desync-fooling=datanoack --dpi-desync-fake-tls-mod=rnd,dupsid,rndsni,padencap ^


 hub.spacestation14.com
spacestation14.com
spacestation14.io
cloudflare-dns.com
cloudflare-ech.com
cloudflare-esni.com
cloudflare-gateway.com
cloudflare-quic.com
cloudflare.com
cloudflare.net
cloudflare.tv
cloudflareaccess.com
cloudflareapps.com
cloudflarebolt.com
cloudflareclient.com
cloudflareinsights.com
cloudflareok.com
cloudflarepartners.com
cloudflareportal.com
cloudflarepreview.com
cloudflareresolve.com
cloudflaressl.com
cloudflarestatus.com
cloudflarestorage.com
cloudflarestream.com
cloudflaretest.com
cloudflarewarp.com
cloudflare-cn.com
cloudflare-dns.com
cloudflare-esni.com
cloudflare-gateway.com
cloudflare-quic.com
cloudflare.com
cloudflare.net
cloudflare-ipfs.com
cloudflare-stream.com
cloudflare-tv.com
cloudflare-access.com
cloudflare-apps.com
cloudflare-bolt.com
cloudflare-client.com
cloudflare-insights.com
cloudflare-ok.com
cloudflare-partners.com
cloudflare-portal.com
cloudflare-preview.com
cloudflare-resolve.com
cloudflare-ssl.com
cloudflare-status.com
cloudflare-storage.com
cloudflare-test.com
cloudflare-warp.com
cloudflareanycast.net
cloudflarechina.cn
cloudflareglobal.net
cloudflareinsights-cn.com
cloudflareperf.com
cloudflareprod.com
cloudflarestaging.com
 ```
