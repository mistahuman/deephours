export function formatDateLocale(timestamp, locale = 'it-IT') {
	const date = new Date(timestamp);

	const formattedDate = date.toLocaleDateString(locale, {
		day: '2-digit',
		month: 'long',
		year: 'numeric'
	});

	return `${formattedDate}`;
}

export function formatMonthLocale(timestamp, locale = 'it-IT') {
	const date = new Date(timestamp);

	const formattedDate = date.toLocaleDateString(locale, {
		month: 'long',
		year: 'numeric'
	});

	return `${formattedDate}`;
}
