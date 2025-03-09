export const myCustomTheme = {
	name: 'my-custom-theme',
	properties: {
		// =~= Theme Properties =~=
		'--theme-font-family-base': `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace`,
		'--theme-font-family-heading': `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace`,
		'--theme-font-color-base': '0 0 0',
		'--theme-font-color-dark': '255 255 255',
		'--theme-rounded-base': '4px',
		'--theme-rounded-container': '4px',
		'--theme-border-base': '1px',
		// =~= Theme On-X Colors =~=
		'--on-primary': '0 0 0',
		'--on-secondary': '255 255 255',
		'--on-tertiary': '0 0 0',
		'--on-success': '0 0 0',
		'--on-warning': '0 0 0',
		'--on-error': '255 255 255',
		'--on-surface': '255 255 255',
		// =~= Theme Colors  =~=
		// primary | #0FBA81
		'--color-primary-50': '219 245 236', // #dbf5ec
		'--color-primary-100': '207 241 230', // #cff1e6
		'--color-primary-200': '195 238 224', // #c3eee0
		'--color-primary-300': '159 227 205', // #9fe3cd
		'--color-primary-400': '87 207 167', // #57cfa7
		'--color-primary-500': '15 186 129', // #0FBA81
		'--color-primary-600': '14 167 116', // #0ea774
		'--color-primary-700': '11 140 97', // #0b8c61
		'--color-primary-800': '9 112 77', // #09704d
		'--color-primary-900': '7 91 63', // #075b3f
		// secondary | #4F46E5
		'--color-secondary-50': '229 227 251', // #e5e3fb
		'--color-secondary-100': '220 218 250', // #dcdafa
		'--color-secondary-200': '211 209 249', // #d3d1f9
		'--color-secondary-300': '185 181 245', // #b9b5f5
		'--color-secondary-400': '132 126 237', // #847eed
		'--color-secondary-500': '79 70 229', // #4F46E5
		'--color-secondary-600': '71 63 206', // #473fce
		'--color-secondary-700': '59 53 172', // #3b35ac
		'--color-secondary-800': '47 42 137', // #2f2a89
		'--color-secondary-900': '39 34 112', // #272270
		// tertiary | #0EA5E9
		'--color-tertiary-50': '219 242 252', // #dbf2fc
		'--color-tertiary-100': '207 237 251', // #cfedfb
		'--color-tertiary-200': '195 233 250', // #c3e9fa
		'--color-tertiary-300': '159 219 246', // #9fdbf6
		'--color-tertiary-400': '86 192 240', // #56c0f0
		'--color-tertiary-500': '14 165 233', // #0EA5E9
		'--color-tertiary-600': '13 149 210', // #0d95d2
		'--color-tertiary-700': '11 124 175', // #0b7caf
		'--color-tertiary-800': '8 99 140', // #08638c
		'--color-tertiary-900': '7 81 114', // #075172
		// success | #84cc16
		'--color-success-50': '237 247 220', // #edf7dc
		'--color-success-100': '230 245 208', // #e6f5d0
		'--color-success-200': '224 242 197', // #e0f2c5
		'--color-success-300': '206 235 162', // #ceeba2
		'--color-success-400': '169 219 92', // #a9db5c
		'--color-success-500': '132 204 22', // #84cc16
		'--color-success-600': '119 184 20', // #77b814
		'--color-success-700': '99 153 17', // #639911
		'--color-success-800': '79 122 13', // #4f7a0d
		'--color-success-900': '65 100 11', // #41640b
		// warning | #EAB308
		'--color-warning-50': '252 244 218', // #fcf4da
		'--color-warning-100': '251 240 206', // #fbf0ce
		'--color-warning-200': '250 236 193', // #faecc1
		'--color-warning-300': '247 225 156', // #f7e19c
		'--color-warning-400': '240 202 82', // #f0ca52
		'--color-warning-500': '234 179 8', // #EAB308
		'--color-warning-600': '211 161 7', // #d3a107
		'--color-warning-700': '176 134 6', // #b08606
		'--color-warning-800': '140 107 5', // #8c6b05
		'--color-warning-900': '115 88 4', // #735804
		// error | #D41976
		'--color-error-50': '249 221 234', // #f9ddea
		'--color-error-100': '246 209 228', // #f6d1e4
		'--color-error-200': '244 198 221', // #f4c6dd
		'--color-error-300': '238 163 200', // #eea3c8
		'--color-error-400': '225 94 159', // #e15e9f
		'--color-error-500': '212 25 118', // #D41976
		'--color-error-600': '191 23 106', // #bf176a
		'--color-error-700': '159 19 89', // #9f1359
		'--color-error-800': '127 15 71', // #7f0f47
		'--color-error-900': '104 12 58', // #680c3a
		// surface | #495a8f
		'--color-surface-50': '228 230 238', // #e4e6ee
		'--color-surface-100': '219 222 233', // #dbdee9
		'--color-surface-200': '210 214 227', // #d2d6e3
		'--color-surface-300': '182 189 210', // #b6bdd2
		'--color-surface-400': '128 140 177', // #808cb1
		'--color-surface-500': '73 90 143', // #495a8f
		'--color-surface-600': '66 81 129', // #425181
		'--color-surface-700': '55 68 107', // #37446b
		'--color-surface-800': '44 54 86', // #2c3656
		'--color-surface-900': '36 44 70' // #242c46
	}
};



export const myDeepTheme = {
    name: 'my-deep-theme',
    properties: {
		// =~= Theme Properties =~=
		"--theme-font-family-base": `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace`,
		"--theme-font-family-heading": `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace`,
		"--theme-font-color-base": "0 0 0",
		"--theme-font-color-dark": "255 255 255",
		"--theme-rounded-base": "12px",
		"--theme-rounded-container": "12px",
		"--theme-border-base": "1px",
		// =~= Theme On-X Colors =~=
		"--on-primary": "255 255 255",
		"--on-secondary": "0 0 0",
		"--on-tertiary": "0 0 0",
		"--on-success": "255 255 255",
		"--on-warning": "0 0 0",
		"--on-error": "255 255 255",
		"--on-surface": "0 0 0",
		// =~= Theme Colors  =~=
		// primary | #003092 
		"--color-primary-50": "217 224 239", // #d9e0ef
		"--color-primary-100": "204 214 233", // #ccd6e9
		"--color-primary-200": "191 203 228", // #bfcbe4
		"--color-primary-300": "153 172 211", // #99acd3
		"--color-primary-400": "77 110 179", // #4d6eb3
		"--color-primary-500": "0 48 146", // #003092
		"--color-primary-600": "0 43 131", // #002b83
		"--color-primary-700": "0 36 110", // #00246e
		"--color-primary-800": "0 29 88", // #001d58
		"--color-primary-900": "0 24 72", // #001848
		// secondary | #FFAB5B 
		"--color-secondary-50": "255 242 230", // #fff2e6
		"--color-secondary-100": "255 238 222", // #ffeede
		"--color-secondary-200": "255 234 214", // #ffead6
		"--color-secondary-300": "255 221 189", // #ffddbd
		"--color-secondary-400": "255 196 140", // #ffc48c
		"--color-secondary-500": "255 171 91", // #FFAB5B
		"--color-secondary-600": "230 154 82", // #e69a52
		"--color-secondary-700": "191 128 68", // #bf8044
		"--color-secondary-800": "153 103 55", // #996737
		"--color-secondary-900": "125 84 45", // #7d542d
		// tertiary | #FFF2DB 
		"--color-tertiary-50": "255 253 250", // #fffdfa
		"--color-tertiary-100": "255 252 248", // #fffcf8
		"--color-tertiary-200": "255 252 246", // #fffcf6
		"--color-tertiary-300": "255 250 241", // #fffaf1
		"--color-tertiary-400": "255 246 230", // #fff6e6
		"--color-tertiary-500": "255 242 219", // #FFF2DB
		"--color-tertiary-600": "230 218 197", // #e6dac5
		"--color-tertiary-700": "191 182 164", // #bfb6a4
		"--color-tertiary-800": "153 145 131", // #999183
		"--color-tertiary-900": "125 119 107", // #7d776b
		// success | #278245 
		"--color-success-50": "223 236 227", // #dfece3
		"--color-success-100": "212 230 218", // #d4e6da
		"--color-success-200": "201 224 209", // #c9e0d1
		"--color-success-300": "169 205 181", // #a9cdb5
		"--color-success-400": "104 168 125", // #68a87d
		"--color-success-500": "39 130 69", // #278245
		"--color-success-600": "35 117 62", // #23753e
		"--color-success-700": "29 98 52", // #1d6234
		"--color-success-800": "23 78 41", // #174e29
		"--color-success-900": "19 64 34", // #134022
		// warning | #e4950c 
		"--color-warning-50": "251 239 219", // #fbefdb
		"--color-warning-100": "250 234 206", // #faeace
		"--color-warning-200": "248 229 194", // #f8e5c2
		"--color-warning-300": "244 213 158", // #f4d59e
		"--color-warning-400": "236 181 85", // #ecb555
		"--color-warning-500": "228 149 12", // #e4950c
		"--color-warning-600": "205 134 11", // #cd860b
		"--color-warning-700": "171 112 9", // #ab7009
		"--color-warning-800": "137 89 7", // #895907
		"--color-warning-900": "112 73 6", // #704906
		// error | #c3082e 
		"--color-error-50": "246 218 224", // #f6dae0
		"--color-error-100": "243 206 213", // #f3ced5
		"--color-error-200": "240 193 203", // #f0c1cb
		"--color-error-300": "231 156 171", // #e79cab
		"--color-error-400": "213 82 109", // #d5526d
		"--color-error-500": "195 8 46", // #c3082e
		"--color-error-600": "176 7 41", // #b00729
		"--color-error-700": "146 6 35", // #920623
		"--color-error-800": "117 5 28", // #75051c
		"--color-error-900": "96 4 23", // #600417
		// surface | #00879E 
		"--color-surface-50": "217 237 240", // #d9edf0
		"--color-surface-100": "204 231 236", // #cce7ec
		"--color-surface-200": "191 225 231", // #bfe1e7
		"--color-surface-300": "153 207 216", // #99cfd8
		"--color-surface-400": "77 171 187", // #4dabbb
		"--color-surface-500": "0 135 158", // #00879E
		"--color-surface-600": "0 122 142", // #007a8e
		"--color-surface-700": "0 101 119", // #006577
		"--color-surface-800": "0 81 95", // #00515f
		"--color-surface-900": "0 66 77", // #00424d
		
	}
}