# pushover notifications for motionyeye 
Pushover is a paid $5 app after a 30 day trial. [Pushover Account](https://pushover.net/) **required** and or [IOS AppStore](https://apps.apple.com/us/app/pushover-notifications/id506088175) or [Google PlayStore](https://play.google.com/store/apps/details?id=net.superblock.pushover) with [MotioEye project](https://github.com/motioneye-project/motioneye/wiki/Installation)    
As long as file has executible permissions it'll work fine. `chmod +x filename.sh` in teminal.`./filename.sh` add `sudo` if needed.  
[WinSCP](https://winscp.net/) works good for this also. <ins>Not necessary</ins>.    
Insert your pushover credentials. **Examples:**  
`YOUR_TOKEN_HERE` `YOUR_USER_KEY_HERE` `YOUR_PUSHOVER_DEVICE_NAME(S)_HERE` `YOUR_PUSHOVER_SOUND_HERE`  
`YOUR_TITLE_HERE` `YOUR_URL_HERE`  
[Pushover API](https://pushover.net/api) 
## Sounds
<ul>
        <li><code>pushover</code> - Pushover (default)
          &nbsp;
          <a href="#" onclick="playSound('po.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>bike</code> - Bike
          &nbsp;
          <a href="#" onclick="playSound('bk.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>bugle</code> - Bugle
          &nbsp;
          <a href="#" onclick="playSound('bu.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>cashregister</code> - Cash Register
          &nbsp;
          <a href="#" onclick="playSound('ch.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>classical</code> - Classical
          &nbsp;
          <a href="#" onclick="playSound('cl.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>cosmic</code> - Cosmic
          &nbsp;
          <a href="#" onclick="playSound('co.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>falling</code> - Falling
          &nbsp;
          <a href="#" onclick="playSound('fa.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>gamelan</code> - Gamelan
          &nbsp;
          <a href="#" onclick="playSound('gl.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>incoming</code> - Incoming
          &nbsp;
          <a href="#" onclick="playSound('ic.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>intermission</code> - Intermission
          &nbsp;
          <a href="#" onclick="playSound('im.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>magic</code> - Magic
          &nbsp;
          <a href="#" onclick="playSound('ma.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>mechanical</code> - Mechanical
          &nbsp;
          <a href="#" onclick="playSound('mc.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>pianobar</code> - Piano Bar
          &nbsp;
          <a href="#" onclick="playSound('pn.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>siren</code> - Siren
          &nbsp;
          <a href="#" onclick="playSound('si.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>spacealarm</code> - Space Alarm
          &nbsp;
          <a href="#" onclick="playSound('sp.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>tugboat</code> - Tug Boat
          &nbsp;
          <a href="#" onclick="playSound('tg.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>alien</code> - Alien Alarm (long)
          &nbsp;
          <a href="#" onclick="playSound('ln.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>climb</code> - Climb (long)
          &nbsp;
          <a href="#" onclick="playSound('mb.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>persistent</code> - Persistent (long)
          &nbsp;
          <a href="#" onclick="playSound('ps.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>echo</code> - Pushover Echo (long)
          &nbsp;
          <a href="#" onclick="playSound('ec.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>updown</code> - Up Down (long)
          &nbsp;
          <a href="#" onclick="playSound('ud.mp3'); return false;"
          title="Click to play"><img src="/images/speaker16.png" width=16 height=16
          srcset="/images/speaker16.png 1x, /images/speaker32.png 2x"></a>
        <li><code>vibrate</code> - Vibrate Only
        <li><code>none</code> - None (silent)
      </ul>
