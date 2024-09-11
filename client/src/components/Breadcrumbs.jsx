import React from 'react';
import { Link, useLocation } from 'react-router-dom';

const Breadcrumbs = ({ breadcrumbs }) => {
    const location = useLocation();
    const currentLocationPath = location.pathname;

    const filteredBreadcrumbs = breadcrumbs.filter(breadcrumb => currentLocationPath.includes(breadcrumb.link));

    return (
        <div className="breadcrumbs mb-2">
            {filteredBreadcrumbs.map((breadcrumb, index) => (
                <span key={index}>
                    {index > 0 && <span className="separator">/</span>}
                    {breadcrumb.link ? (
                        <Link to={breadcrumb.link}>{breadcrumb.label}</Link>
                    ) : (
                        <span>{breadcrumb.label}</span>
                    )}
                </span>
            ))}
        </div>
    );
};

export default Breadcrumbs;
