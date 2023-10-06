import { useState, useEffect } from "react"
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Doughnut } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend);

const backgroundColor = [
    'rgba(255, 99, 132, 0.2)',
    'rgba(54, 162, 235, 0.2)',
    'rgba(255, 206, 86, 0.2)',
    'rgba(75, 192, 192, 0.2)',
    'rgba(153, 102, 255, 0.2)',
    'rgba(255, 159, 64, 0.2)',
]

const borderColor = [
    'rgba(255, 99, 132, 1)',
    'rgba(54, 162, 235, 1)',
    'rgba(255, 206, 86, 1)',
    'rgba(75, 192, 192, 1)',
    'rgba(153, 102, 255, 1)',
    'rgba(255, 159, 64, 1)',
]

export default () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const apiUrl = 'http://127.0.0.1:8000/stats/SAMPLE_100';

        fetch(apiUrl)
          .then(response => response.json())
          .then(data => setData(data))
          .catch(error => console.error('Error:', error));
    }, []);    

    const countPerType = [
        {
        label: 'Count per RNA type',
        data: data["count_per_type"],
        backgroundColor: backgroundColor,
        borderColor: borderColor,
        borderWidth: 1,
        },
    ];

    const uniqueCountPerType = [
        {
        label: 'Count per RNA type',
        data: data["unique_count_per_type"],
        backgroundColor: backgroundColor,
        borderColor: borderColor,
        borderWidth: 1,
        },
    ];

    return (
    <>
        <div className="max-w-screen-xl mx-auto px-4 md:px-8">
            <div className="items-start justify-between py-4 border-b md:flex">
                <div>
                    <h3 className="text-gray-800 text-2xl font-bold">
                        Short-RNA types
                    </h3>
                </div>
            </div>
        </div>
        <div className="relative max-w-xs mx-auto mt-12">
            <svg xmlns="http://www.w3.org/2000/svg" className="absolute top-0 bottom-0 w-6 h-6 my-auto text-gray-400 right-2.5" viewBox="0 0 20 20" fill="currentColor">
                <path fillRule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd" />
            </svg>
            <select className="w-full p-2.5 text-gray-500 bg-white border rounded-md shadow-sm outline-none appearance-none focus:border-indigo-600">
                <option>Project manager</option>
                <option>Software engineer</option>
                <option>IT manager</option>
                <option>UI / UX designer</option>
            </select>
        </div>
        <div>
            <h3 className="text-gray-800 text-2xl font-bold">
                % sequences/molecules across types
            </h3>
            <Doughnut data={{ labels: data["labels"], datasets: countPerType }} />
            <h3 className="text-gray-800 text-2xl font-bold">
                % unique sequences/molecule across types
            </h3>
            <Doughnut data={{ labels: data["labels"], datasets: uniqueCountPerType }} />
        </div>
    </>
    )
}