# libjpeg GYP Module

** Experimental **

expose libjpeg through gyp

- can be used stand alone to compile libjpeg-turbo as static/shared libraries ( / dll) 
	static/shared library can be changed in the variables section of libjpeg.gyp
- can be used as part of a bigger gyp project (which was the original intent) :

```
'dependencies':[
	'libjpeg.module/libjpeg.gyp:libjpeg'
]
```

libjpeg-turbo 
http://libjpeg-turbo.virtualgl.org/

Using as module from:
https://github.com/svn2github/libjpeg-turbo


```
gyp libjpeg.gyp -DOS=win -Dtarget_arch=ia32 -Duse_system_yasm=0 --depth=. -f msvs -G msvs_version=2013 --generator-output=./build.vs2013/

gyp libjpeg.gyp -DOS=win -Dtarget_arch=x64 -Duse_system_yasm=0 --depth=. -f msvs -G msvs_version=2013 --generator-output=./build.vs2013/

gyp libjpeg.gyp -DOS=linux -Dtarget_arch=ia32 -Duse_system_yasm=1 --depth=. -f make --generator-output=./build.linux32/

gyp libjpeg.gyp -DOS=linux -Dtarget_arch=x64 -Duse_system_yasm=1 --depth=. -f make --generator-output=./build.linux64/

gyp libjpeg.gyp -DOS=android -Dtarget_arch=arm --depth=. -f make --generator-output=./build.android/
```

libjpeg requires yasm to compile on ia32 and x64 architectures

