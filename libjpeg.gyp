# started with https://github.com/zenoalbisser/chromium/blob/master/chromium/third_party/libjpeg_turbo/libjpeg.gyp
# ended up rewriting most of it (Dror Gluska)

# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  # This file is not used when use_system_libjepg==1. Settings for building with
  # the system libjpeg is in third_party/libjpeg/libjpeg.gyp.
	'variables': {
		#'library' : 'static_library',
		'library' : 'shared_library',
		
		'yasm_output_path': '<(INTERMEDIATE_DIR)',
	},
	
	'targets': [
		{
			'target_name': 'libjpeg',
			'type': '<(library)',
			'include_dirs': [
				'config',
				'libjpeg-turbo_src',
			],
			'direct_dependent_settings': {
				'include_dirs': [
					'libjpeg-turbo_src',
				],
			},
			'defines': [
				'WITH_SIMD', 'MOTION_JPEG_SUPPORTED',
			],
			
			
			
			
		'sources': [
			'config/jconfig.h',
			
			'libjpeg-turbo_src/jchuff.c',
			'libjpeg-turbo_src/jchuff.h',
			'libjpeg-turbo_src/jdct.h',
			'libjpeg-turbo_src/jdhuff.c',
			'libjpeg-turbo_src/jdhuff.h',
			'libjpeg-turbo_src/jerror.c',
			'libjpeg-turbo_src/jerror.h',
			'libjpeg-turbo_src/jinclude.h',
			'libjpeg-turbo_src/jmemsys.h',
			'libjpeg-turbo_src/jmorecfg.h',
			'libjpeg-turbo_src/jpegint.h',
			'libjpeg-turbo_src/jpeglib.h',
			'libjpeg-turbo_src/jversion.h',
			'libjpeg-turbo_src/jsimd.h',
			'libjpeg-turbo_src/jsimddct.h',
			'libjpeg-turbo_src/jpegcomp.h',
			'libjpeg-turbo_src/jpeg_nbits_table.h',
			'libjpeg-turbo_src/jcapimin.c',
			'libjpeg-turbo_src/jcapistd.c',
			'libjpeg-turbo_src/jccoefct.c',
			'libjpeg-turbo_src/jccolor.c',
			'libjpeg-turbo_src/jcdctmgr.c',
			'libjpeg-turbo_src/jcinit.c',
			'libjpeg-turbo_src/jcmainct.c',
			'libjpeg-turbo_src/jcmarker.c',
			'libjpeg-turbo_src/jcmaster.c',
			'libjpeg-turbo_src/jcomapi.c',
			'libjpeg-turbo_src/jcparam.c',
			'libjpeg-turbo_src/jcphuff.c',
			'libjpeg-turbo_src/jcprepct.c',
			'libjpeg-turbo_src/jcsample.c',
			'libjpeg-turbo_src/jctrans.c',
			'libjpeg-turbo_src/jdapimin.c',
			'libjpeg-turbo_src/jdapistd.c',
			'libjpeg-turbo_src/jdatadst.c',
			'libjpeg-turbo_src/jdatasrc.c',
			'libjpeg-turbo_src/jdcoefct.c',
			'libjpeg-turbo_src/jdcolor.c',
			'libjpeg-turbo_src/jddctmgr.c',
			'libjpeg-turbo_src/jdinput.c',
			'libjpeg-turbo_src/jdmainct.c',
			'libjpeg-turbo_src/jdmarker.c',
			'libjpeg-turbo_src/jdmaster.c',
			'libjpeg-turbo_src/jdmerge.c',
			'libjpeg-turbo_src/jdphuff.c',
			'libjpeg-turbo_src/jdpostct.c',
			'libjpeg-turbo_src/jdsample.c',
			'libjpeg-turbo_src/jdtrans.c',
			'libjpeg-turbo_src/jfdctflt.c',
			'libjpeg-turbo_src/jfdctfst.c',
			'libjpeg-turbo_src/jfdctint.c',
			'libjpeg-turbo_src/jidctflt.c',
			'libjpeg-turbo_src/jidctfst.c',
			'libjpeg-turbo_src/jidctint.c',
			'libjpeg-turbo_src/jidctred.c',
			'libjpeg-turbo_src/jquant1.c',
			'libjpeg-turbo_src/jquant2.c',
			'libjpeg-turbo_src/jutils.c',
			'libjpeg-turbo_src/jmemmgr.c',
			'libjpeg-turbo_src/jmemnobs.c',
			
			#with_arith
			'libjpeg-turbo_src/jaricom.c',
			
			#with_arith_enc
			'libjpeg-turbo_src/jcarith.c',
			
			#with_arith_dec
			'libjpeg-turbo_src/jdarith.c',
			
			#with_turbojpeg
			#'libjpeg-turbo_src/turbojpeg.c',
			#'libjpeg-turbo_src/turbojpeg.h',
			#'libjpeg-turbo_src/transupp.c',
			#'libjpeg-turbo_src/transupp.h',
			#'libjpeg-turbo_src/jdatadst-tj.c',
			#'libjpeg-turbo_src/jdatasrc-tj.c',
			

		
			
			#'libjpeg-turbo_src/BUILDING.txt',
			
			#'libjpeg-turbo_src/change.log',
			#'libjpeg-turbo_src/ChangeLog.txt',
			#'libjpeg-turbo_src/coderules.txt',
			#'libjpeg-turbo_src/jccolext.c',
			#'libjpeg-turbo_src/jconfig.txt',
			#'libjpeg-turbo_src/jdcol565.c',
			#'libjpeg-turbo_src/jdcolext.c',
			#'libjpeg-turbo_src/jdmrg565.c',
			#'libjpeg-turbo_src/jdmrgext.c',
			#'libjpeg-turbo_src/jsimd_none.c',
			#'libjpeg-turbo_src/jstdhuff.c',
			#'libjpeg-turbo_src/libjpeg.txt',
			
			
			
			#'libjpeg-turbo_src/rdrle.c',
			
			#'libjpeg-turbo_src/README',
			#'libjpeg-turbo_src/README-turbo.txt',
			#'libjpeg-turbo_src/structure.txt',
			#'libjpeg-turbo_src/testimages',
			
			#'libjpeg-turbo_src/usage.txt',
			#'libjpeg-turbo_src/wrrle.c',
			
		],
		'direct_dependent_settings': {
			'include_dirs': [
				'libjpeg-turbo_src',
			],
		},
		'msvs_disabled_warnings': [4018, 4101],
		# VS2010 does not correctly incrementally link obj files generated
		# from asm files. This flag disables UseLibraryDependencyInputs to
		# avoid this problem.
		'msvs_2010_disable_uldi_when_referenced': 1,
		
		
		'variables':{
			'yasm_flags':[
				'-I', 'config/<(OS)',
				'-I', 'config',
			],
			'conditions':[
				['library == "shared_library"',{
					'yasm_flags':[
						'-DPIC',
					],
				}],
			],
		},
		
		'conditions': [
			['library == "shared_library"',{
				'cflags':[
					'-fPIC',
				],
			}],
			['target_arch in "ia32 x64"',{
				'includes':[
					'yasm_compile.gypi',
				],
			}],
		
			[ 'OS!="win"', {'product_name': 'jpeg_turbo'}],
			['OS == "win"',{
				'defines':[
					#"INLINE=inline",
				],
			}],
			['OS == "win" and library == "shared_library"',{
				'sources':[
					'config/jpeg8.def',
				],
			}],
			# Add target-specific source files.
			['target_arch == "ia32"',{
				'defines':[
					'SIZEOF_SIZE_T=4',
				],
			}],
			['OS == "win" and target_arch == "ia32"',{
				'variables':{
					'yasm_flags':[
						'-DWIN32',
					],
				},
			}],
			['OS == "win" and target_arch == "x64"',{
				'variables':{
					'yasm_flags':[
						'-DWIN64',
					],
				},
			}],
			['OS != "win"',{
				'variables':{
					'yasm_flags':[
						'-DELF',
					],
				},
			}],
			
			[ 'target_arch in "ia32"', {
				
				'sources': [
					#extra
					#'libjpeg-turbo_src/simd/jccolext-mmx.asm',
					#'libjpeg-turbo_src/simd/jcgryext-mmx.asm',
					#'libjpeg-turbo_src/simd/jdcolext-mmx.asm',
					#'libjpeg-turbo_src/simd/jdmrgext-mmx.asm',
					#'libjpeg-turbo_src/simd/jccolext-sse2.asm',
					#'libjpeg-turbo_src/simd/jcgryext-sse2.asm',
					#'libjpeg-turbo_src/simd/jdcolext-sse2.asm',
					#'libjpeg-turbo_src/simd/jdmrgext-sse2.asm',
					
					'libjpeg-turbo_src/simd/jsimd_i386.c',
					'libjpeg-turbo_src/simd/jsimd.h',
					'libjpeg-turbo_src/simd/jsimdcfg.inc.h',
					'libjpeg-turbo_src/simd/jsimdext.inc',
					'libjpeg-turbo_src/simd/jcolsamp.inc',
					'libjpeg-turbo_src/simd/jdct.inc',
					'libjpeg-turbo_src/simd/jsimdcpu.asm',
					'libjpeg-turbo_src/simd/jfdctflt-3dn.asm',
					'libjpeg-turbo_src/simd/jidctflt-3dn.asm',
					'libjpeg-turbo_src/simd/jquant-3dn.asm',
					'libjpeg-turbo_src/simd/jccolor-mmx.asm',
					'libjpeg-turbo_src/simd/jcgray-mmx.asm',
					'libjpeg-turbo_src/simd/jcsample-mmx.asm',
					'libjpeg-turbo_src/simd/jdcolor-mmx.asm',
					'libjpeg-turbo_src/simd/jdmerge-mmx.asm',
					'libjpeg-turbo_src/simd/jdsample-mmx.asm',
					'libjpeg-turbo_src/simd/jfdctfst-mmx.asm',
					'libjpeg-turbo_src/simd/jfdctint-mmx.asm',
					'libjpeg-turbo_src/simd/jidctfst-mmx.asm',
					'libjpeg-turbo_src/simd/jidctint-mmx.asm',
					'libjpeg-turbo_src/simd/jidctred-mmx.asm',
					'libjpeg-turbo_src/simd/jquant-mmx.asm',
					'libjpeg-turbo_src/simd/jfdctflt-sse.asm',
					'libjpeg-turbo_src/simd/jidctflt-sse.asm',
					'libjpeg-turbo_src/simd/jquant-sse.asm',
					'libjpeg-turbo_src/simd/jccolor-sse2.asm',
					'libjpeg-turbo_src/simd/jcgray-sse2.asm',
					'libjpeg-turbo_src/simd/jcsample-sse2.asm',
					'libjpeg-turbo_src/simd/jdcolor-sse2.asm',
					'libjpeg-turbo_src/simd/jdmerge-sse2.asm',
					'libjpeg-turbo_src/simd/jdsample-sse2.asm',
					'libjpeg-turbo_src/simd/jfdctfst-sse2.asm',
					'libjpeg-turbo_src/simd/jfdctint-sse2.asm',
					'libjpeg-turbo_src/simd/jidctflt-sse2.asm',
					'libjpeg-turbo_src/simd/jidctfst-sse2.asm',
					'libjpeg-turbo_src/simd/jidctint-sse2.asm',
					'libjpeg-turbo_src/simd/jidctred-sse2.asm',
					'libjpeg-turbo_src/simd/jquantf-sse2.asm',
					'libjpeg-turbo_src/simd/jquanti-sse2.asm',
					
					#'libjpeg-turbo_src/simd/jcsample.h',
					
				
				],
			}],
			[ 'target_arch=="x64"', {
				'variables':{
					'yasm_flags':[
						'-D__x86_64__',
					],
				},
				'defines':[
					'SIZEOF_SIZE_T=8',
				],
				'sources': [
					'libjpeg-turbo_src/simd/jsimd_x86_64.c',		
					'libjpeg-turbo_src/jsimd.h',				
					'libjpeg-turbo_src/simd/jsimdcfg.inc.h',
					'libjpeg-turbo_src/simd/jsimdext.inc',
					'libjpeg-turbo_src/simd/jcolsamp.inc',
					'libjpeg-turbo_src/simd/jdct.inc',
					'libjpeg-turbo_src/simd/jfdctflt-sse-64.asm',
					'libjpeg-turbo_src/simd/jccolor-sse2-64.asm',
					'libjpeg-turbo_src/simd/jcgray-sse2-64.asm',
					'libjpeg-turbo_src/simd/jcsample-sse2-64.asm',
					'libjpeg-turbo_src/simd/jdcolor-sse2-64.asm',
					'libjpeg-turbo_src/simd/jdmerge-sse2-64.asm',
					'libjpeg-turbo_src/simd/jdsample-sse2-64.asm',
					'libjpeg-turbo_src/simd/jfdctfst-sse2-64.asm',
					'libjpeg-turbo_src/simd/jfdctint-sse2-64.asm',
					'libjpeg-turbo_src/simd/jidctflt-sse2-64.asm',
					'libjpeg-turbo_src/simd/jidctfst-sse2-64.asm',
					'libjpeg-turbo_src/simd/jidctint-sse2-64.asm',
					'libjpeg-turbo_src/simd/jidctred-sse2-64.asm',
					'libjpeg-turbo_src/simd/jquantf-sse2-64.asm',
					'libjpeg-turbo_src/simd/jquanti-sse2-64.asm',
					
					#'libjpeg-turbo_src/simd/jccolext-sse2-64.asm',
					#'libjpeg-turbo_src/simd/jcgryext-sse2-64.asm',
					#'libjpeg-turbo_src/simd/jdcolext-sse2-64.asm',
					#'libjpeg-turbo_src/simd/jdmrgext-sse2-64.asm',
				],
			}],
			# The ARM SIMD implementation can be used for devices that support
			# the NEON instruction set. This is done dynamically by probing CPU
			# features at runtime, so always compile it for ARMv7-A devices.
			[ 'target_arch=="arm"', {
				'defines':[
					'SIZEOF_SIZE_T=4',
				],
				'sources':[
					'libjpeg-turbo_src/simd/jsimd_arm.c',
					'libjpeg-turbo_src/simd/jsimd_arm_neon.S',
				],
			}],
			[ 'target_arch=="arm64"', {
				'defines':[
					'SIZEOF_SIZE_T=8',
				],
				'sources':[
					'libjpeg-turbo_src/simd/jsimd_arm64.c',
					'libjpeg-turbo_src/simd/jsimd_arm64_neon.S',				
				],

				
			}],
			[ 'target_arch=="mipsel"', {
				'sources': [
					'libjpeg-turbo_src/simd/jsimd_mips.c',
					'libjpeg-turbo_src/simd/jsimd_mips_dspr2.S',
					'libjpeg-turbo_src/simd/jsimd_mips_dspr2_asm.h',
				],
			}],
			['target_arch == "powerpc"',{
				'sources':[
					'libjpeg-turbo_src/simd/jsimd_powerpc.c',
					'libjpeg-turbo_src/simd/jccolor-altivec.c',
					'libjpeg-turbo_src/simd/jcgray-altivec.c',
					'libjpeg-turbo_src/simd/jcsample-altivec.c',
					'libjpeg-turbo_src/simd/jdcolor-altivec.c',
					'libjpeg-turbo_src/simd/jdmerge-altivec.c',
					'libjpeg-turbo_src/simd/jdsample-altivec.c',
					'libjpeg-turbo_src/simd/jfdctfst-altivec.c',
					'libjpeg-turbo_src/simd/jfdctint-altivec.c',
					'libjpeg-turbo_src/simd/jidctfst-altivec.c',
					'libjpeg-turbo_src/simd/jidctint-altivec.c',
					'libjpeg-turbo_src/simd/jquanti-altivec.c',
					#'libjpeg-turbo_src/simd/jsimd_altivec.h',
					#'libjpeg-turbo_src/simd/jccolext-altivec.c',
					#'libjpeg-turbo_src/simd/jcgryext-altivec.c',
					#'libjpeg-turbo_src/simd/jdcolext-altivec.c',
					#'libjpeg-turbo_src/simd/jdmrgext-altivec.c',
				],
				'cflags':[
					'-maltivec',
				],
			}],
		
		],
    },
	
	{
		'target_name': 'cjpeg',
		'type':'executable',
		'dependencies':[
			'libjpeg',
		],
		'defines':[
			'GIF_SUPPORTED',
			'PPM_SUPPORTED',
			
			#if not with_12bit
			#'BMP_SUPPORTED',
			#'TARGA_SUPPORTED',
		],
		'include_dirs': [
			'config',
		],
		'sources':[
			'libjpeg-turbo_src/cdjpeg.c',
			'libjpeg-turbo_src/cderror.h',
			'libjpeg-turbo_src/cdjpeg.h',
			'libjpeg-turbo_src/cjpeg.c',
			'libjpeg-turbo_src/rdswitch.c',
			'libjpeg-turbo_src/rdgif.c',
			'libjpeg-turbo_src/rdppm.c',
			
			#if not WITH_12BIT
			#'libjpeg-turbo_src/rdbmp.c',
			#'libjpeg-turbo_src/rdtarga.c',
			
		],
	},
	
	{
		'target_name': 'djpeg',
		'type':'executable',
		'dependencies':[
			'libjpeg',
		],
		'include_dirs': [
			'config',
		],
		'defines':[
			'GIF_SUPPORTED',
			'PPM_SUPPORTED',
			
			#if not with_12bit
			#'BMP_SUPPORTED',
			#'TARGA_SUPPORTED',
		],
		'sources':[
			'libjpeg-turbo_src/cderror.h',
			'libjpeg-turbo_src/rdcolmap.c',
			'libjpeg-turbo_src/djpeg.c',
			'libjpeg-turbo_src/cdjpeg.c',
			'libjpeg-turbo_src/cdjpeg.h',
			'libjpeg-turbo_src/rdswitch.c',
			'libjpeg-turbo_src/wrgif.c',
			'libjpeg-turbo_src/wrppm.c',
			
			#if not WITH_12BIT
			#'libjpeg-turbo_src/wrbmp.c',
			#'libjpeg-turbo_src/wrtarga.c',
			
		],
	},
	
	{
		'target_name': 'jcstest',
		'type':'executable',
		'dependencies':[
			'libjpeg',
		],
		'include_dirs': [
			'config',
		],
		'sources':[
			'libjpeg-turbo_src/jcstest.c',
		],
	},
	
	{
		'target_name': 'jpegtran',
		'type':'executable',
		'dependencies':[
			'libjpeg',
		],
		'include_dirs': [
			'config',
		],
		'sources':[
			'libjpeg-turbo_src/rdswitch.c',
			'libjpeg-turbo_src/jpegtran.c',
			'libjpeg-turbo_src/transupp.c',
			'libjpeg-turbo_src/transupp.h',
			'libjpeg-turbo_src/cdjpeg.c',
			'libjpeg-turbo_src/cdjpeg.h',
		],
	},
	
	{
		'target_name': 'rdjpgcom',
		'type':'executable',
		'dependencies':[
			'libjpeg',
		],
		'include_dirs': [
			'config',
		],
		'sources':[
			'libjpeg-turbo_src/rdjpgcom.c',
		],
	},
	
	#{
	#	'target_name': 'tjbench',
	#	'type':'executable',
	#	'dependencies':[
	#		'libjpeg',
	#	],
	#	'defines':[
	#		'BMP_SUPPORTED',
	#		'PPM_SUPPORTED',
	#	],
	#	'sources':[
	#		'libjpeg-turbo_src/tjbench.c',
	#		'libjpeg-turbo_src/bmp.c',
	#		'libjpeg-turbo_src/bmp.h',
	#		'libjpeg-turbo_src/rdppm.c',
	#		'libjpeg-turbo_src/tjutil.c',
	#		'libjpeg-turbo_src/tjutil.h',
	#	],
	#},
	
	#{
	#	'target_name': 'tjunittest',
	#	'type':'executable',
	#	'dependencies':[
	#		'libjpeg',
	#	],
	#	'sources':[
	#		'libjpeg-turbo_src/tjunittest.c',
	#		'libjpeg-turbo_src/tjutil.h',
	#		'libjpeg-turbo_src/tjutil.c',
	#	],
	#},
	
	{
		'target_name': 'wrjpgcom',
		'type':'executable',
		'dependencies':[
			'libjpeg',
		],
		'include_dirs': [
			'config',
		],
		'sources':[
			'libjpeg-turbo_src/wrjpgcom.c',
		],
	},
	
  ],
}



#'libjpeg-turbo_src/example.c',

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2: